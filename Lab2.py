import subprocess
import os
def echo(text):
    print(text)

def ping(text):
    pin = subprocess.getoutput(f"ping 192.168.1.1")
    print(pin)

def login(text):
    text = text.split()
    str = "Success" if(text[1] == "true" and text[2] == "true") else "fail"
    print(str)

def list(text):
    print(os.listdir("."))

def msg(text):
    text = text.split()
    print(text[2] + " was sent to " + text[1])

def file(text):
    text = text.split()
    print(text[2] + " was sent to " + text[1])

def exit(text):
    os._exit(0)

#------------------
cmd={"echo": echo,"ping": ping,"login": login,"list": list,"msg": msg,"file": file,"exit": exit}
while(True):
    try:
        text = input("Enter command:\n")
        cmd[text.split()[0]](text)
    except:
        print("Wrong input")


