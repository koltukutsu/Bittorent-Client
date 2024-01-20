'use strict'
const fs = require('fs')
const path = fs.readFileSync('puppy.torrent')
const bencode = require('bencode')
const tracker = require('./tracker');

const torrent = bencode.decode(path)
tracker.getPeers(torrent, peers => {
    console.log('list of peers: ', peers)
})

console.log(torrent.announce.toString('utf8'))
// announce url is the tracker's url

