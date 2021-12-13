import webbrowser
import os


def iniciar_hugo():
    #os.chdir("./Restaurant_Web")
    url = "http://localhost:1313"
    webbrowser.open(url)
    os.system("hugo server --bind=0.0.0.0 --baseUrl=localhost -D -F")
