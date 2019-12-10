package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "80"
	}

	server := &Server{Channels: make(map[string]*Channel), Password: "********"}
	log.Fatal(http.ListenAndServe(":"+port, server))
}

// A Server is a collection of channels.
type Server struct {
	Channels map[string]*Channel
	Password string
}

// GetChannel returns the named channel, creating it if it does not already exist.
func (s *Server) GetChannel(name string) *Channel {
	if channel, ok := s.Channels[name]; ok {
		return channel
	}

	channel := &Channel{
		Name:        name,
		Subscribers: make([]*Client, 0),
		Log:         make([]Message, 0),
		server:      s,
	}

	s.Channels[name] = channel
	return channel
}

// ServeHTTP responds to incoming HTTP requests.
//
// First, the request is checked for appropriate credentials.
// If the request URL corresponds to a file in the public folder, that file is served.
// Otherwise the URL is assumed to refer to a channel, and control is passed to that channel.
func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if _, password, ok := r.BasicAuth(); !ok || password != s.Password {
		w.Header().Set("WWW-Authenticate", "Basic realm=WebSocket Server")
		http.Error(w, "Unauthorized", 401)
		return
	}

	publicPath := filepath.Dir(os.Args[0]) + "/public" + r.URL.Path
	if info, err := os.Stat(publicPath); err == nil && !info.IsDir() {
		fmt.Println("Serving", publicPath)
		http.ServeFile(w, r, publicPath)
		return
	}

	name := strings.TrimPrefix(r.URL.Path, "/")
	channel := s.GetChannel(name)
	channel.ServeHTTP(w, r)
}

func serveTemplate(w http.ResponseWriter, r *http.Request, path string, data interface{}) {
	fmt.Println("Serving template", path)
	t, err := template.ParseFiles(path)
	if err != nil {
		http.Error(w, "Internal Server Error", 500)
		fmt.Println(err)
		return
	}

	w.Header().Add("Content-Type", "text/html; charset=utf-8")
	err = t.Execute(w, data)
	if err != nil {
		fmt.Fprint(w, err)
		fmt.Println(err)
	}
}
