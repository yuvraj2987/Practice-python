#! /usr/bin/env bash
echo "Create virtual env directory"
mkdir -p pyenv2.7
echo "setup virtualenv"
virtualenv -p python2.7 pyenv2.7
source python2.7/bin/activate
pip install -r requirements.txt
