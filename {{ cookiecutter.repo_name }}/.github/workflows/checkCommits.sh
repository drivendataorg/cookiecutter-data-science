#!/bin/bash
sourceBranch=${1:-$(git branch --show-current)}
targetBranch=${2-origin/master}
echo "Checking diff between $sourceBranch and $targetBranch"
commits=$(git log --pretty=%B $sourceBranch...$targetBranch | grep -v -e '^$')
echo -e "Checking commits:\n$commits"
IFS='
'
exitCode=0
for commit in $commits
do
    poetry run cz check -m "$commit"
    lastExitCode="$?"
    if [ $lastExitCode -ne 0 ] ; then
        exitCode=$lastExitCode
    fi
done
exit $exitCode
