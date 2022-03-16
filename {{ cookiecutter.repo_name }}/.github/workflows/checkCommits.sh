#!/bin/bash
set -e

sourceBranch=${1:-$(git branch --show-current)}
targetBranch=${2-origin/master}
git fetch -p
echo "Checking diff between $sourceBranch and $targetBranch"
poetry run cz check --rev-range $targetBranch..$sourceBranch
