.PHONY: compile install

compile:
	go build -o server .
	chmod +x server

install:
	cp websocket-server.service /etc/systemd/system
	systemctl daemon-reload
	systemctl start websocket-server.service
	systemctl enable websocket-server.service
