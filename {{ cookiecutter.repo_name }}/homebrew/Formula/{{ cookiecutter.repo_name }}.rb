require "English"
class {{ cookiecutter.project_name.capitalize().replace(' ', '') }} < Formula
  include Language::Python::Virtualenv
  desc "{{ cookiecutter.description }}"
  homepage "https://github.com/{{ cookiecutter._github_username }}/{{ cookiecutter.repo_name }}"
  # Stable release
  url "https://github.com/{{ cookiecutter._github_username }}/{{ cookiecutter.repo_name }}.git",
    using:    :git,
    tag:      "v0.1.0",
    revision: "HEAD"
  license "{{ cookiecutter.open_source_license }}"
  # Development release
  head "https://github.com/{{ cookiecutter._github_username }}/{{ cookiecutter.repo_name }}.git",
    branch: "main"

  # Automatically check for new versions
  livecheck do
    url :stable
    regex(/^v?(\d+(?:\.\d+)+)$/i)
  end

  depends_on "python@{{ cookiecutter.python_version_number }}" => :build

  # TODO: Add bottle block for pre-built binaries
  # bottle do
  #   ...
  # end

  # Define python dependencies to be installed into the virtualenv
  # Add your dependencies here as needed
  # Example:
  # resource "requests" do
  #   url "https://files.pythonhosted.org/packages/..."
  #   sha256 "..."
  # end

  def install
    # Install documentation
    doc.install "README.md"
    doc.install "LICENSE" if File.exist?("LICENSE")
    
    # Install dependencies and the CLI in a virtualenv
    venv = virtualenv_create(libexec/"venv", "python{{ cookiecutter.python_version_number }}")
    # Install any resources defined above
    venv.pip_install resources
    # Install the package itself
    venv.pip_install_and_link buildpath
    
    # Create bin script
    bin.install libexec/"venv/bin/{{ cookiecutter.module_name }}"
  end

  def caveats
    <<~EOS
      {{ cookiecutter._project_emoji }} {{ cookiecutter.project_name }} has been installed.

      For more information, visit:
        https://github.com/{{ cookiecutter._github_username }}/{{ cookiecutter.repo_name }}
    EOS
  end

  test do
    # Check if the command-line tool is installed and runs without error
    system bin/"{{ cookiecutter.module_name }}", "--version"
    # Check if the documentation files are installed
    assert_predicate doc/"README.md", :exist?
  end
end
