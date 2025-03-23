#!/bin/bash

# Exit on error
set -e

# Check if {{ cookiecutter.project_name }} is already installed
if command -v {{ cookiecutter.module_name }} &>/dev/null; then
	echo "
✅ {{ cookiecutter.project_name }} is already installed!
Current version: $({{ cookiecutter.module_name }} --version 2>/dev/null || echo "unknown")

Would you like to reinstall or update {{ cookiecutter.project_name }}?
"
	read -p "Reinstall/update {{ cookiecutter.project_name }}? (y/N) " reinstall
	if [[ ! $reinstall =~ ^[Yy]$ ]]; then
		echo "Installation cancelled. {{ cookiecutter.project_name }} is already installed."
		exit 0
	fi
fi

echo "
🚀 {{ cookiecutter.project_name }} Installation Script {{ cookiecutter._project_emoji }}
================================

This script will:
{% if cookiecutter.environment_manager == 'uv' %}
1. Install the uv package manager if not already installed
2. Install {{ cookiecutter.project_name }} using uv
{% elif cookiecutter.environment_manager == 'virtualenv' %}
1. Install virtualenv if not already installed
2. Create and activate a virtual environment
3. Install {{ cookiecutter.project_name }} using pip
{% elif cookiecutter.environment_manager == 'conda' %}
1. Check for conda installation
2. Create and activate a conda environment
3. Install {{ cookiecutter.project_name }} using conda
{% elif cookiecutter.environment_manager == 'pipenv' %}
1. Install pipenv if not already installed
2. Install {{ cookiecutter.project_name }} using pipenv
{% else %}
1. Install {{ cookiecutter.project_name }} using pip
{% endif %}
{% if 'paper' in cookiecutter.include_code_scaffold %}
3. Check for and install LaTeX (pdflatex) if needed:
   - On macOS: Using Homebrew and MacTeX
   - On Linux: Using apt-get and texlive packages
{% endif %}
4. Set up your {{ cookiecutter.project_name }} environment

Note: This may require sudo privileges for some installations.
"

# Ask for confirmation
read -p "Would you like to proceed with the installation? (y/N) " proceed
if [[ ! $proceed =~ ^[Yy]$ ]]; then
	echo "Installation cancelled."
	exit 0
fi

echo "📦 Installing {{ cookiecutter.project_name }}..."

{% if cookiecutter.environment_manager == 'uv' %}
# Check if uv is installed, install if not
if ! command -v uv &>/dev/null; then
	echo "📦 Installing uv package manager..."
	curl -LsSf https://astral.sh/uv/install.sh | sh
	source $HOME/.local/bin/env
fi

# Install {{ cookiecutter.project_name }} using uv tool
echo "📚 Installing {{ cookiecutter.project_name }}..."
uv pip install {{ cookiecutter.module_name }}
{% elif cookiecutter.environment_manager == 'virtualenv' %}
# Check if virtualenv is installed, install if not
if ! command -v virtualenv &>/dev/null; then
	echo "📦 Installing virtualenv..."
	pip install virtualenv
fi

# Create and activate virtual environment
echo "🔧 Creating virtual environment..."
virtualenv venv
source venv/bin/activate

# Install {{ cookiecutter.project_name }}
echo "📚 Installing {{ cookiecutter.project_name }}..."
pip install {{ cookiecutter.module_name }}
{% elif cookiecutter.environment_manager == 'conda' %}
# Check if conda is installed
if ! command -v conda &>/dev/null; then
	echo "❌ Conda is not installed. Please install Conda first."
	exit 1
fi

# Create and activate conda environment
echo "🔧 Creating conda environment..."
conda create -n {{ cookiecutter.module_name }} python={{ cookiecutter.python_version_number }} -y
conda activate {{ cookiecutter.module_name }}

# Install {{ cookiecutter.project_name }}
echo "📚 Installing {{ cookiecutter.project_name }}..."
conda install {{ cookiecutter.module_name }} -y
{% elif cookiecutter.environment_manager == 'pipenv' %}
# Check if pipenv is installed, install if not
if ! command -v pipenv &>/dev/null; then
	echo "📦 Installing pipenv..."
	pip install pipenv
fi

# Install {{ cookiecutter.project_name }}
echo "📚 Installing {{ cookiecutter.project_name }}..."
pipenv install {{ cookiecutter.module_name }}
{% else %}
# Install {{ cookiecutter.project_name }} using pip
echo "📚 Installing {{ cookiecutter.project_name }}..."
pip install {{ cookiecutter.module_name }}
{% endif %}

{% if 'paper' in cookiecutter.include_code_scaffold %}
# Check if pdflatex is installed
if ! command -v pdflatex &>/dev/null; then
	echo "⚠️ LaTeX (pdflatex) is not installed."

	# Check if running on macOS
	if [[ $OSTYPE == "darwin"* ]]; then
		if ! command -v brew &>/dev/null; then
			echo "🍺 Homebrew not found. Installing Homebrew..."
			/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

			# Add Homebrew to PATH based on chip architecture
			if [[ $(uname -m) == "arm64" ]]; then
				echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >>~/.zprofile
				eval "$(/opt/homebrew/bin/brew shellenv)"
			else
				echo 'eval "$(/usr/local/bin/brew shellenv)"' >>~/.zprofile
				eval "$(/usr/local/bin/brew shellenv)"
			fi
		fi

		echo "🍺 Installing MacTeX using Homebrew..."
		brew install --cask mactex
	# Check if running on Linux with apt-get
	elif command -v apt-get &>/dev/null; then
		echo "📦 Installing LaTeX using apt-get..."
		sudo apt-get update
		sudo apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-latex-extra
	else
		echo "❌ Please install LaTeX (pdflatex) manually for your operating system."
		exit 1
	fi
fi
{% endif %}

# Verify installation
echo "✅ Verifying installation..."
{{ cookiecutter.module_name }} --help

# Ask user about project setup
read -p "Would you like to set up a {{ cookiecutter.project_name }} project now? (y/N) " setup_project

if [[ $setup_project =~ ^[Yy]$ ]]; then
	echo "📁 Setting up project..."
	mkdir -p ~/{{ cookiecutter.project_name }}_projects
	cd ~/{{ cookiecutter.project_name }}_projects
	{{ cookiecutter.module_name }} init
	open .
fi

echo "
🎉 Installation complete! You can now use {{ cookiecutter.project_name }}.

Quick start:
1. Create a new project:       {{ cookiecutter.module_name }} init
2. Run your first command:     {{ cookiecutter.module_name }} --help

For more information, see the documentation at:
https://github.com/{{ cookiecutter._github_username }}/{{ cookiecutter.repo_name }}
"
