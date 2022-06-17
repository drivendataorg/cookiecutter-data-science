## This code was created by 


# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

"""
Cookiecutter-Git Post Project Generation Hook Module.
"""
import base64
from contextlib import contextmanager
import errno
import getpass
import json
import os
import re
import shutil

if os.name == "nt":

    def quote(arg):
        # https://stackoverflow.com/a/29215357
        if re.search(r'(["\s])', arg):
            arg = '"' + arg.replace('"', r"\"") + '"'
        meta_chars = '()%!^"<>&|'
        meta_re = re.compile(
            "(" + "|".join(re.escape(char) for char in list(meta_chars)) + ")"
        )
        meta_map = {char: "^%s" % char for char in meta_chars}

        def escape_meta_chars(m):
            char = m.group(1)
            return meta_map[char]

        return meta_re.sub(escape_meta_chars, arg)


else:
    try:  # py34, py35, py36, py37
        from shlex import quote
    except ImportError:  # py27
        from pipes import quote

from invoke import Result, run, UnexpectedExit
import requests


class MockResult(Result):
    mock_stdout = {
        "github.com": """Password for 'https://NathanUrwin@github.com':
Counting objects: 18, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (18/18), 6.24 KiB | 0 bytes/s, done.
Total 18 (delta 0), reused 0 (delta 0)
To https://github.com/NathanUrwin/cookiecutter-git-demo.git
* [new branch]      master -> master
Branch master set up to track remote branch master from origin.""",
        "gitlab.com": """Password for 'https://NathanUrwin@gitlab.com':
Counting objects: 13, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (10/10), done.
Writing objects: 100% (13/13), 5.25 KiB | 0 bytes/s, done.
Total 13 (delta 0), reused 0 (delta 0)
remote:
remote: The private project NathanUrwin/cookiecutter-git-demo was successfully created.
remote:
remote: To configure the remote, run:
remote:   git remote add origin https://gitlab.com/NathanUrwin/cookiecutter-git-demo.git
remote:
remote: To view the project, visit:
remote:   https://gitlab.com/NathanUrwin/cookiecutter-git-demo
remote:
To https://gitlab.com/NathanUrwin/cookiecutter-git-demo.git
* [new branch]      master -> master
Branch master set up to track remote branch master from origin.""",
        "bitbucket.org": """Password for 'https://NathanUrwin@bitbucket.org':
Counting objects: 13, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (10/10), done.
Writing objects: 100% (13/13), 5.26 KiB | 0 bytes/s, done.
Total 13 (delta 0), reused 0 (delta 0)
To https://bitbucket.org/NathanUrwin/cookiecutter-git-demo.git
* [new branch]      master -> master
Branch master set up to track remote branch master from origin.""",
    }

    def __init__(self, remote_provider, **kwargs):
        stdout = self.mock_stdout.get(remote_provider, "")
        super(MockResult, self).__init__(stdout, **kwargs)


@contextmanager
def git_disable_gpgsign():
    """
    Disables git commit GPG signing temporarily.
    """
    try:
        result = run("git config --global --get commit.gpgSign", hide=True)
    # throws only on travis-ci. unknown reason
    except UnexpectedExit:

        class ResultNone:
            stdout = ""

        result = ResultNone()
    if result.stdout.strip() == "true":
        # turn off gpg signing commits
        try:
            run("git config --global --unset commit.gpgSign")
            yield
        # turn gpg signing back on
        except KeyboardInterrupt:
            run("git config --global --bool commit.gpgSign true")
        finally:
            run("git config --global --bool commit.gpgSign true")
    else:
        yield


class PostGenProjectHook(object):
    """
    Post Project Generation Class Hook.
    """

    bitbucket_repos_url_base = (
        "https://api.bitbucket.org/2.0/repositories/{}/{}"
    )
    create_remote_url = None
    github_repos_url = "https://api.github.com/user/repos"
    git_ignore_url_base = "https://www.gitignore.io/api/{}"
    headers = {}
    json_header = {"Content-Type": "application/json; charset=utf-8"}
    password_prompt_base = "Password for 'https://{}@{}': "
    remote_message_base = "Also see: https://{}/{}/{}"
    success_message_base = "\n\nSuccess! Your project was created here:\n{}\n{}\nThanks for using cookiecutter-git! :)\n\n"
    repo_dirpath = os.getcwd()
    cookiecutter_json_filepath = os.path.join(
        repo_dirpath, "cookiecutter.json"
    )
    raw_repo_name_dirpath = os.path.join(
        repo_dirpath, "{% raw %}{{cookiecutter.repo_name}}{% endraw %}"
    )
    github_dirpath = os.path.join(repo_dirpath, ".github")
    git_ignore_filepath = os.path.join(repo_dirpath, ".gitignore")
    hooks_dirpath = os.path.join(repo_dirpath, "hooks")
    licenses_dirpath = os.path.join(repo_dirpath, "LICENSES")
    license_filepath = os.path.join(repo_dirpath, "LICENSE")
    notice_filepath = os.path.join(repo_dirpath, "NOTICE")

    def __init__(self, *args, **kwargs):
        """
        Initializes the class instance.
        """
        self.result = self._get_cookiecutter_result()
        self.copyright_holder = self.result.get("copyright_holder")
        self.copyright_license = self.result.get("copyright_license")
        self.git_email = self.result.get("git_email")
        self.git_ignore = self.result.get("git_ignore")
        self.git_name = self.result.get("git_name")
        self.make_dirs = self.result.get("make_dirs")
        self.remote_namespace = self.result.get("remote_namespace")
        self.remote_protocol = self.result.get("remote_protocol")
        self.remote_provider = str(self.result.get("remote_provider")).lower()
        self.remote_username = self.result.get("remote_username")
        self.repo_name = self.result.get("repo_name")
        self.repo_summary = self.result.get("repo_summary")
        self.repo_tagline = self.result.get("repo_tagline")
        self._testing = str(self.result.get("_testing")).lower() == "true"
        #
        self.apache_license = self.copyright_license == "Apache-2.0"
        self.bitbucket_repos_url = self.bitbucket_repos_url_base.format(
            self.remote_namespace, self.repo_name
        )
        self.git_ignore_url = self.git_ignore_url_base.format(self.git_ignore)
        self.nested_license_filepath = os.path.join(
            self.licenses_dirpath, "{}.txt".format(self.copyright_license)
        )
        self.new_git_ignore = self.git_ignore != "windows,macos,linux,git"
        self.password_prompt = self.password_prompt_base.format(
            self.remote_username, self.remote_provider
        )
        self.project_dirpaths = [
            os.path.join(self.repo_dirpath, dirname.strip())
            for dirname in self.make_dirs.split(",")
            if dirname.strip()
        ]
        self.remote_data = {
            "name": self.repo_name,
            "description": self.repo_tagline,
        }
        self.create_remote_url = self._get_create_remote_url()
        self.encoded_data = json.dumps(self.remote_data).encode()
        self.remote_password = ""
        self.remote_repo = self.remote_provider != "none"
        if self.remote_repo:
            self.remote_password = self._get_remote_password()
        self.remote_origin_url = self._get_remote_origin_url()
        self.remote_origin_url_with_pass = self._get_remote_origin_url(
            with_pass=True
        )
        self.remote_message = (
            self.remote_message_base.format(
                self.remote_provider, self.remote_namespace, self.repo_name
            )
            if self.remote_repo
            else ""
        )
        self.success_message = self.success_message_base.format(
            self.repo_dirpath, self.remote_message
        )

    @staticmethod
    def format_basic_auth(username, password):
        """
        Formats HTTP Basic auth with base64 encoding.

        :param username:
        :param password:
        """
        auth_data = "{}:{}".format(username, password)
        return base64.b64encode(auth_data.encode())

    @staticmethod
    def git_init():
        """
        Runs git init.
        """
        run("git init")

    @staticmethod
    def git_add():
        """
        Runs git add all.
        """
        # `git add -A`
        run("git add --all")

    @staticmethod
    def git_commit(message="Initial commit"):
        """
        Runs git commit with an initial message.

        :param message:
        """
        command = "git commit --message {}".format(quote(message))
        if os.name == "nt":
            # See https://github.com/NathanUrwin/cookiecutter-git/issues/43
            with git_disable_gpgsign():
                run(command)
        else:
            # `git commit -m "Initial commit"`
            run(command)

    @staticmethod
    def _get_cookiecutter_result():
        """
        Removes as much jinja2 templating from the hook as possible.
        """
        # http://flask.pocoo.org/docs/latest/templating/#standard-filters
        try:
            result = json.loads("""{{ cookiecutter | tojson() }}""")
        # current temp hack around for `pipenv run pytest -s`
        except json.JSONDecodeError:
            result = {}
            repo_dirpath = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
            json_filepath = os.path.join(repo_dirpath, "cookiecutter.json")
            with open(json_filepath) as f:
                for k, v in json.loads(f.read()).items():
                    result[k] = v
                    if isinstance(v, list):
                        result[k] = v[0]
        return result

    def _get_create_remote_url(self):
        """
        Gets the create remote URL.
        """
        create_remote_url = None
        if self.remote_username != self.remote_namespace:
            self.github_repos_url = "https://api.github.com/orgs/{}/repos".format(
                self.remote_namespace
            )
        if self.remote_provider == "bitbucket.org":
            create_remote_url = self.bitbucket_repos_url
            self.headers.update(self.json_header)
            self.remote_data.update({"has_issues": True, "is_private": True})
        elif self.remote_provider == "github.com":
            create_remote_url = self.github_repos_url
        return create_remote_url

    def _get_remote_origin_url(self, with_pass=False):
        """
        Gets the remote origin URL.
        """
        if with_pass:
            remote_origin_url = "https://{}:{}@{}/{}/{}.git".format(
                requests.utils.quote(self.remote_username, safe=""),
                requests.utils.quote(self.remote_password, safe=""),
                self.remote_provider,
                self.remote_namespace,
                self.repo_name,
            )
        else:
            remote_origin_url = "https://{}@{}/{}/{}.git".format(
                requests.utils.quote(self.remote_username, safe=""),
                self.remote_provider,
                self.remote_namespace,
                self.repo_name,
            )
        if self.remote_protocol == "ssh":
            remote_origin_url = "git@{}:{}/{}.git".format(
                self.remote_provider, self.remote_namespace, self.repo_name
            )
        return remote_origin_url

    def _get_remote_password(self):
        """
        Gets the remote password with getpass.
        """
        # current hack for tests. better work around ?
        if self._testing:
            remote_password = "notmypassword"
        else:
            # prompt CLI users for password
            remote_password = getpass.getpass(self.password_prompt).strip()
        return remote_password

    def _git_remote_set(self):
        """
        Sets the git remote origin url.
        """
        run(
            "git remote set-url origin {}".format(
                quote(self.remote_origin_url)
            )
        )

    def _git_push(self):
        """
        Pushes the git remote and sets as upstream.
        """
        command = "git push --set-upstream origin master"
        if self._testing:
            print("_testing _git_push")
            r = MockResult(self.remote_provider, command=command)
            print(r.stdout)
            return r
        else:
            # `git push -u origin master`
            run(command)

    def _git_remote_add(self):
        """
        Adds the git remote origin url with included password.
        """
        run(
            "git remote add origin {}".format(
                quote(self.remote_origin_url_with_pass)
            )
        )

    def _git_remote_repo(self):
        """
        Creates a remote repo if needed.
        """
        if self.remote_provider in ["bitbucket.org", "github.com"]:
            # http basic auth if needed
            auth_base64 = self.format_basic_auth(
                self.remote_username, self.remote_password
            )
            self.headers["Authorization"] = "Basic {}".format(
                auth_base64.decode()
            )
            # create remote POST request
            requests.post(
                self.create_remote_url,
                data=self.encoded_data,
                headers=self.headers,
            )

    def _git_ignore(self):
        """
        Creates a new .gitignore if needed from gitignore.io.
        """
        if self.new_git_ignore:
            # gitignore.io/api -> {{cookiecutter.repo_name}}/.gitignore
            response = requests.get(self.git_ignore_url)
            with open(self.git_ignore_filepath, "w") as f:
                f.write(response.text)

    def _git_repo(self):
        """
        Adds a .gitignore, initial commit, and remote repo.
        """
        self._git_ignore()
        self.git_init()
        self.git_add()
        self.git_commit()
        if self.remote_repo:
            self._git_remote_repo()
            self._git_remote_add()
            self._git_push()
            self._git_remote_set()

    def _github_dir(self):
        """
        Removes the .github dir if GitHub is not the remote provider.
        """
        if not self.remote_provider == "github.com":
            shutil.rmtree(self.github_dirpath, ignore_errors=True)

    def _make_dirs(self):
        """
        Makes dirs and adds .gitkeep files to them.
        """
        for dirpath in self.project_dirpaths:
            # equal to bash `mkdir -p $dirpath`
            try:
                os.makedirs(dirpath)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                    pass
                else:
                    raise
            # equal to bash `touch $dirpath/.gitkeep`
            gitkeep = os.path.join(dirpath, ".gitkeep")
            with open(gitkeep, "a"):
                os.utime(gitkeep, None)

    def _copyright_license(self):
        """
        Adds the chosen LICENSE and removes the rest.
        """
        if not self.apache_license:
            os.remove(self.notice_filepath)
        shutil.move(self.nested_license_filepath, self.license_filepath)
        shutil.rmtree(self.licenses_dirpath, ignore_errors=True)

    def run(self):
        """
        Sets up the project license, dirs, and git repo.
        """
        self._copyright_license()
        self._make_dirs()
        self._github_dir()
        self._git_repo()
        print(self.success_message)


def main():
    """
    Runs the post gen project hook main entry point.
    """
    PostGenProjectHook().run()


# This is required! Don't remove!!
if __name__ == "__main__":
    main()