from wol_control import *
from wol_control.models import User
from werkzeug.security import generate_password_hash, check_password_hash

app = create_app()

with app.app_context():
    print("Create new user:")
    username = input("Username: ")
    raw_password = input("Password: ")
    is_admin = True
    admin_in = input("Is admin [Y/n]")

    if(admin_in == "N" or admin_in == "n"):
        is_admin = False

    if raw_password is None or len(raw_password) >= 100 or username is None or len(username) >= 100:
        print("Username/Password not valid")
        quit()

    hash_passwd = generate_password_hash(raw_password, method='sha256')
    new_user = User(name=username, password=hash_passwd , admin=is_admin)

    print("New user {} created succesfuly".format(username))

    db.session.add(new_user)
    db.session.commit()

