# rust_rcon
Simple library to talk with Rust's RCON interface


### Installation
`pip install rust-rcon`

or 

Clone the repo and run `python3 setup.py install` & `pip3 install -r requirements.txt`


### Basic Usage
```
import json
from rust_rcon import Command, websocket_connection

## Create rcon connection via websocket
ws = websocket_connection("server ip", "rcon port", "rcon key/password")

## Instantiate the command you would like to run with websocket connection
command = Command("playerlist", 10, ws)

## Gather the response for further parsing
response = command.run()
```

### Contributing
Pull requests are welcome. Currently library is only really for personal use, but feel free to open PR's or issues if you notice any.

### License
MIT
