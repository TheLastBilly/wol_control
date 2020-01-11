from wol_control import *
from wol_control.models import Mac
import re, base64
app = create_app()

with app.app_context():
    print("Add new Mac address:")
    name = input("Name: ")

    if name is None or len(name) >= 100:
        print("Invalid name")
        quit()

    mac = input("Mac address: ")
    is_admin = True

    if not re.match("[0-9a-f]{2}([:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        print("Invalid mac address")
        quit()
    

    admin_in = input("Only admin [Y/n]")

    if(admin_in == "N" or admin_in == "n"):
        is_admin = False

    new_mac = Mac(mac=mac, admin=is_admin, name=name, public_id=str(base64.b64encode(name.encode("utf-8")), "utf-8"))

    print("Mac address {} added succesfully".format(name))

    db.session.add(new_mac)
    db.session.commit()