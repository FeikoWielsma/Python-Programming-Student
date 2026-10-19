from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

handler = partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).resolve().parent))
server = ThreadingHTTPServer(("127.0.0.1", 4188), handler)
print(f"Open http://127.0.0.1:{server.server_address[1]}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
