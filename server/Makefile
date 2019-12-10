.PHONY: compile install

compile:
	mkdir bin
	go build -o bin/server .
	chmod +x bin/server

install: compile
	cp websocket-server.service /etc/systemd/systemd
	systemctl reload-daemon
	systemctl start websocket-server.service
	systemctl enable websocket-server.service
