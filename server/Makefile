.PHONY: compile install

compile:
	mkdir -p bin
	go build -o bin/server .
	chmod +x bin/server

install:
	cp websocket-server.service /etc/systemd/system
	systemctl daemon-reload
	systemctl start websocket-server.service
	systemctl enable websocket-server.service
