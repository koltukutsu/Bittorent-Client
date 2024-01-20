from bencoding import Encoder, Decoder

def getTorrent(filename):
    with open(filename, 'rb') as f:
        meta_info = f.read()
        torrent = Decoder(meta_info).decode()

    return torrent


def main():
    torrentFile = "./torrents/ubuntu-22.04.3-desktop-amd64.iso.torrent"
    torrent = getTorrent(torrentFile)
    print(len(torrent.keys()))
    torrent["info"]["pieces"] = "test"
if __name__ == "__main__":
    main()