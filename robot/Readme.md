Raspberry Pi Setup Instructions
===============================

Clone the repository into the home folder of the Raspberry Pi:
```
$ git clone https://github.com/coditect/arch7210-fall2019
```

Copy the unit file to the systemd folder:
```
$ sudo cp arch7210-fall2019/robot/robot.service /etc/systemd/system
```

Enable the service:
```
$ sudo systemctl start robot.service
$ sudo systemctl enable robot.service
```
