Checking the temperature reading and sending a notification to telegrams and to the Iris server if the temperature is below or above the threshold
Raspberry pi launched a service for regularly reading the temperature sensor (in python) and sending a message to the cart to my bot.
Raspberry pi in the country house is included in the local network. The temperature sensor DS18B20 with 4.7k resist is soldered and screwed to the 4th pin of the Raspberry pi.

# Instructions for launching

1. python -v venv <venv_name>
2. source venv_name/bin/activate # (`deactivate`)
3. pip install -r requirements.txt
4. Edit the configuration file `check-send.yml`

```
# Options
version: '1.0.0'

# Send regular message to bot
debug_print: yes
# frequency of polling the sensor in seconds
#timeout: 3600
timeout: 15
# Minimum notification threshold in degrees Celsius
min_threshold: 15
# Maximum notification threshold in degrees Celsius
max_threshold: 25


# Options telebot
token: 1111111
chat_id: 1111111

# Sensor parameters
# the path to the file
#dirbus1w: /tmp/
dirbus1w: temp-test.txt

# parameters for registering and sending a message to the iris server
username='superuser'
password='SYS'
base_url="http://127.0.0.1:52773/apptoolsrest/custom-task/user/run&class=apptools.core.rest&met=SaveLog&par="
```

# You can write a systemd daemon if your operating system uses one.

Create a daemon file:
sudo touch /etc/systemd/system/bot.service

## Paste the following into it:
```
[unit]
Description=My bot
After=multi-user.target

[Service]
type=idle
ExecStart=/usr/bin/python3 /path/to/script/check-send.py /path/to/script/check-send.yml
Restart=always
 
[Install]
WantedBy=multi-user.target
```

## After that, in the console we execute:
sudo systemctl daemon-reload
sudo systemctl enable bot.service
sudo systemctl start bot.service


## To stop the bot:
sudo systemctl stop bot.service
## To remove from startup:
sudo systemctl disable bot.service
## To test the daemon:
sudo systemctl status bot.service

# Thanks

https://myraspberrypi.ru/2018/10/24/%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-ds18b20-%D0%BA-raspberry-pi/

https://qna.habr.com/q/520860

http://slugg.spb.ru/ubuntu/ubuntu_setting/36-ubuntu-server-i-set-1-wire.html

https://sameak.ru/nastrojka-i-ispolzovanie-shiny-1-wire-na-raspberry-pi-3b-s-serverom-owserver/

