Raspberry Pi Setup Instructions
===============================

Clone the repository into the home folder of the Raspberry Pi:
```
$ git clone https://github.com/coditect/arch7210-fall2019
```

Install the [Lomond](https://github.com/wildfoundry/dataplicity-lomond) WebSocket library:
```
$ sudo pip3 install lomond
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
