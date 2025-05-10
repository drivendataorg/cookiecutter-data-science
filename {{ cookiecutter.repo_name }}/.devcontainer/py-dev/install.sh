#!/bin/sh
set -e

# Note the current directory where all the feature files are in case the script moves us.
FEATURE_BUNDLE="$PWD"

echo "Persist bash history across container restarts ..."
echo "export HISTFILE=/commandhistory/.bash_history" >>"${BASHRC_PATH}"
echo "export PROMPT_COMMAND='history -a'" >>"${BASHRC_PATH}"

if [ ! -d "$HOME/.oh-my-bash" ]; then
    echo "Oh-My-Bash is not installed. Installing now..."
    wget https://raw.github.com/ohmybash/oh-my-bash/master/tools/install.sh -O - | bash
else
    echo "Oh-My-Bash is already installed."
fi
