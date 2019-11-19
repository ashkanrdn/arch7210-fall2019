package main

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"os"
	"path/filepath"
	"sync"
	"time"

	"github.com/gobwas/ws"
	"github.com/gobwas/ws/wsutil"
)

// Message represents a message sent through a channel.
type Message struct {
	Data []byte
	From *Client
	Time time.Time
}

// Client represents an agent that is subscribed to a channel.
type Client struct {
	Name string
	Conn net.Conn
}

// A Channel accepts messages and broadcasts them to its subscribers.
type Channel struct {
	Name        string
	Subscribers []*Client
	Log         []Message
	mutex       sync.Mutex
	server      *Server
}

// ServeHTTP responds to HTTP requests.
func (c *Channel) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if r.Header.Get("Upgrade") == "websocket" {
		conn, _, _, err := ws.UpgradeHTTP(r, w)
		if err != nil {
			http.Error(w, "Internal Server Error", 500)
			fmt.Println("Unable to upgrade connection:", err)
			return
		}

		name, _, _ := r.BasicAuth()
		client := &Client{name, conn}
		go c.Subscribe(client)
	} else {
		serveTemplate(w, r, filepath.Dir(os.Args[0])+"/channel.html", c)
	}
}

// Subscribe adds the given connection to the channel
func (c *Channel) Subscribe(client *Client) {
	c.mutex.Lock()
	c.Subscribers = append(c.Subscribers, client)
	c.mutex.Unlock()
	defer c.Unsubscribe(client)

	c.Broadcast(createNotification(client.Name+" has connected"), nil)

	for {
		msg, _, err := wsutil.ReadClientData(client.Conn)
		if err != nil {
			return
		}

		err = c.Broadcast(msg, client)
		if err != nil {
			return
		}
	}
}

// Unsubscribe removes the given client from the channel.
func (c *Channel) Unsubscribe(client *Client) {
	client.Conn.Close()
	c.mutex.Lock()

	for i, subscriber := range c.Subscribers {
		if subscriber == client {
			c.Subscribers = append(c.Subscribers[:i], c.Subscribers[i+1:]...)
			break
		}
	}

	c.mutex.Unlock()

	if len(c.Subscribers) == 0 {
		delete(c.server.Channels, c.Name)
	} else {
		c.Broadcast(createNotification(client.Name+" has disconnected"), nil)
	}
}

// Broadcast sends a message to all of the channel's subscribers except the sender.
func (c *Channel) Broadcast(message []byte, sender *Client) error {
	c.mutex.Lock()
	defer c.mutex.Unlock()

	for _, subscriber := range c.Subscribers {
		if subscriber != sender {
			err := wsutil.WriteServerMessage(subscriber.Conn, ws.OpText, message)
			if err != nil {
				return err
			}
		}
	}

	c.AppendLog(message, sender)
	return nil
}

// AppendLog adds a message to the channel's log.
func (c *Channel) AppendLog(message []byte, sender *Client) {
	c.Log = append(c.Log, Message{message, sender, time.Now()})

	if len(c.Log) > 20 {
		c.Log = c.Log[1:]
	}
}

func createNotification(content string) []byte {
	n, _ := json.Marshal(map[string]interface{}{
		"result": content,
	})
	return n
}
