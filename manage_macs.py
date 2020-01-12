from wol_control import *
from wol_control.models import Mac
import re, base64
app = create_app()

with app.app_context():
    def display_macs():
        macs = Mac.query.all()
        if macs is None:
            print("No macs found")
            return None
        print("\nMac List:")
        number = 0
        for mac in macs:
            number+=1
            print("{}: {}{}".format(number, mac.name, "" if not mac.admin else " [ADMIN]" ))
        print("")
        return macs
    def add_mac():
        name = input("Name: ")

        if name is None or len(name) >= 100:
            print("Invalid name")
            quit()

        mac = input("Mac address: ")
        is_admin = True

        if not re.match("[0-9a-f]{2}([:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
            print("Invalid mac address")
            quit()
        
        ip = input("IP address: ")

        if not re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip.lower()):
            print("Invalid IP address")
            quit()

        admin_in = input("Only admin [Y/n]")

        if(admin_in == "N" or admin_in == "n"):
            is_admin = False

        new_mac = Mac(mac=mac, admin=is_admin, name=name, public_id=str(base64.b64encode(name.encode("utf-8")), "utf-8"), ip=ip)

        print("Mac address {} added succesfully".format(name))

        db.session.add(new_mac)
        db.session.commit()
    def delete_mac(mac):
        print("Deleting mac {}".format(mac.name))
        db.session.delete(mac)
        db.session.commit()
    while True:
        macs = display_macs()
        response = input("What would you like to do? [add/delete/exit]: ")
        if response == "add":
            add_mac()
            input("Press enter to continue")
            continue
        elif response == "delete":
            response = input("Which mac would you like to delete: ")
            deleted_mac = False
            for mac in macs:
                if response == mac.name:
                    delete_mac(mac)
                    deleted_mac = True
            if not deleted_mac:
                print("Mac {} not found".format(response))
            input("Press enter to continue")
            continue
        elif response == "exit":
            print("Exiting...")
            break
        else:
            print("Command {} not recognized".format(response))
            continue