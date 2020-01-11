#!/bin/bash

python3 -m pip install --user virtualenv
python3 -m virtualenv ~/.flask_env

source ~/.flask_env/bin/activate

python3 -m pip install -r requirements.txt

echo "Initializing database"

python3 init_db.py

python3 create_user.py
python3 add_mac.py

echo "Copying nginx and systemd files"

sudo cp wol_control.service /etc/systemd/system/wol_control.service
sudo systemctl daemon-reload
sudo systemctl start wol_control
sudo systemctl enable wol_control

sudo cp wol_control.nginx /etc/nginx/sites-available/wol_control.nginx
sudo ln -s /etc/nginx/sites-available/wol_control.nginx /etc/nginx/sites-enabled/wol_control.nginx
sudo systemctl restart nginx

