from flask import Blueprint, render_template, request, Response,redirect,url_for
import os
from flask_login import login_user, login_required, current_user
from .models import Mac

main = Blueprint('main', __name__)

local_ip = "192.168.1.1"

def get_controls( ):
    controls = []
    if current_user.admin:
        controls = Mac.query.all()
    else:
        controls = Mac.query.filter_by(admin=False)
    return controls

@main.route('/')
@login_required
def index():
    controls=get_controls()
    if controls is None:
        return render_template('control.html', message="No controllers have been regystered")
    return render_template( 'control.html', controls=controls)

@main.route('/control/<string:public_id>/<string:command>',methods=['POST'])
@login_required
def toggle_control(public_id, command):
    control = Mac.query.filter_by(public_id=public_id).first()
    if control is None:
        return render_template('control.html', message="No such controller found")
    
    if command == "on":
        os.system("/usr/local/bin/wol -r {} {}".format(local_ip, control.mac))
        return render_template('control.html', message="Turning {} on".format(control.name), controls=[control], redirect_home = True)
    else:
        return render_template('control.html', message="Invalid command", controls=[control], redirect_home = True)
