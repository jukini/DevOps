package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
    log.Println("starting Web Server")

    http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "Hello World!!")
    })

    err := http.ListenAndServe(":7070", nil)
    if err != nil {
        log.Fatalln(err)
    }
}
