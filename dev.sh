#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

echo "Creating dev environment in ./venv_chir..."
sudo apt-get install libmysqlclient-dev -y

python3 -m venv venv_chir
source venv_chir/bin/activate
pip3 install -U pip setuptools
pip3 install -r requirements.txt
source venv_chir/bin/activate
#TODO: pip3 sync
ls .git/||git init .
pre-commit install

echo ""
echo "  * Created virtualenv environment in ./venv_chir."
echo "  * Installed all dependencies into the virtualenv."
echo "  * You can now activate the $(python3 --version) virtualenv with this command: \`source venv_chir/bin/activate\`"
