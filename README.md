
```bash
pip install RPi.GPIO
```

Выдаем права на использование GPIO

```bash
sudo groupadd gpio # create the group
sudo usermod -a -G gpio user_name # add the user to the group
sudo grep gpio /etc/group
sudo chown root:gpio /dev/gpiomem # change the owner and group of /dev/mem to root and gpio
sudo chmod g+rw /dev/gpiomem

sudo reboot
```