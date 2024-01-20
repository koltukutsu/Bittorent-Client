package main

import "fmt"

type bencodeInfo struct {
	Pieces      string `bencode:"pieces"`
	PieceLength int    `bencode:"piece length"`
	Length      int    `bencode`
}

func main() {
	fmt.Println("Starting the client...")

}
