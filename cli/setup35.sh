
#! /usr/bin/env bash
echo "Create virtual env directory for python 3.5"
mkdir -p pyenv3.5
echo "setup virtualenv"
virtualenv -p python3.5 pyenv3.5
source pyenv3.5/bin/activate
pip install -r requirement.txt
echo "Setup tests to run against 3.5"
if [ -L pyenv ]; then
    echo "Delete existing pyenv simlink"
fi
echo "Create simlink to pyenv"
ln -s pyenv pyenv3.5

