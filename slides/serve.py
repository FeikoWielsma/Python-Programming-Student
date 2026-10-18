from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

handler = partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).resolve().parent))
print("Open http://localhost:4188")
ThreadingHTTPServer(("127.0.0.1", 4188), handler).serve_forever()
