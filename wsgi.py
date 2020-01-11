from wol_control import create_app

application = create_app()

if __name__ == "__main__":
    application.run(host="192.168.1.7",port="9090")
