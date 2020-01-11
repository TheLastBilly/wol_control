#!/bin/sh

pip install --user virtualenv
virtualenv ~/.flask_env

source ~/.flask_env/bin/activate

pip install -r requirements.txt

echo "Initializing database"
python3 init_db.py

python3 create_user.py
python3 add_mac.py