#! /usr/bin/env bash
if [ -d "pyenv" ]; then
    echo "pyenv directory exists"
    rm -r "pyenv"
fi
echo "Create virtual env directory for python 3.5"
mkdir -p pyenv
echo "setup virtualenv"
virtualenv -p python3.5 pyenv
source pyenv/bin/activate
pip install -r requirement.txt
