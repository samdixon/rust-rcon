import websocket

def websocket_connection(ip, port, password):
    return websocket.create_connection(f"ws://{ip}:{port}/{password}")
