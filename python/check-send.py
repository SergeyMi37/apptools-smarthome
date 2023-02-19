# A program to regularly read the temperature sensor and send a message to the telebot and the iris server
#pip install requests
#pip install --upgrade pip
import requests
import threading
import datetime
import yaml
import socket

with open('/home/pi/repo/new-test/check-send.yml') as _fi:
    _param = yaml.safe_load(_fi)
print(_param["token"])


def send_telegram(text: str):
    _TOKEN=_param["token"]
    _url = "https://api.telegram.org/bot"
    _channel_id = _param["chat_id"]
    _method = _url + _TOKEN + "/sendMessage"

    r = requests.post(_method, data={
         "chat_id": _channel_id,
         "text": text
          })

    if r.status_code != 200:
        #raise Exception("post_text error")
        print("Error ",r.status_code)
    else:
        print("sent successfully")

def read_tempera():
    threading.Timer(_param["timeout"], read_tempera).start()  # Restart after 3600 seconds - every hour
    _dt=str(datetime.datetime.today().strftime("%Y-%m-%d_%H.%M"))
    tfile=open(_param["dirbus1w"])
    ttext=tfile.read()
    tfile.close()
    temp=ttext.split("\n")[1].split(" ")[9]
    _temp=float(temp[2:])/1000
    _msg="👉 температура "+str(_temp)

    #print(_temp)
    if _temp < _param["min_threshold"]:
        _msg=" 🚨🚨🚨🚨🚨 Attention limit lower temperature threshold "+str(_temp)
        send_telegram(_msg)
    elif _temp > _param["max_threshold"]:
        _msg=" 🚨🚨🚨🚨🚨 Attention upper temperature limit "+str(_temp)
        send_telegram(_msg)
    elif _param["debug_print"]:
        send_telegram(_msg)
    print(_dt+_msg)

    _username=_param["username"]
    _password=_param["password"]
    _base_url=_param["base_url"]+msg
    #print(_param)

    headers = {'Accept': 'application/json;odata=verbose'}
    responce = requests.get(_base_url,verify=False,auth=(_username,_password),headers=headers)

    respon_list=responce.json()
    print(respon_list)


if __name__ == '__main__':
    msg=" ✅ Старт мониторинга температурного датчика. Периодичность: "+str(_param["timeout"])+", пороги оповещения: "+str(_param["min_threshold"])+" <> "+str(_param["max_threshold"])
    send_telegram(msg+ " "+socket.gethostname()+" "+str(socket.gethostbyname(socket.gethostname())))
    print(msg)
    read_tempera()
