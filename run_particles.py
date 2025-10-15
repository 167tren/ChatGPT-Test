#!/usr/bin/env python3
"""Launch a local web server and open the particle simulator in your browser."""
from __future__ import annotations

import contextlib
import http.server
import os
import socket
import threading
import webbrowser
from functools import partial
from pathlib import Path


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that suppresses log spam."""

    def log_message(self, format: str, *args) -> None:  # noqa: A003 - inherited signature
        pass


def find_free_port(start: int = 8000, end: int = 9000) -> int:
    """Return an available TCP port in the given range."""
    for port in range(start, end + 1):
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise OSError("No free port available")


def serve(directory: Path, port: int) -> http.server.ThreadingHTTPServer:
    handler = partial(QuietHandler, directory=str(directory))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    return httpd


def main() -> None:
    root = Path(__file__).resolve().parent
    os.chdir(root)

    if not (root / "particles.html").exists():
        raise FileNotFoundError("particles.html not found next to run_particles.py")

    port = find_free_port()
    httpd = serve(root, port)
    url = f"http://127.0.0.1:{port}/particles.html"

    print("Serving Particle Bloom Simulator")
    print(f"  Local URL: {url}")
    print("Press Ctrl+C to stop the server.")

    # Open the simulator in the default browser on a separate thread so the
    # server can start without blocking.
    threading.Thread(target=webbrowser.open, args=(url,), daemon=True).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
