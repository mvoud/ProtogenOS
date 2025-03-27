import http.server
import socketserver
import os 
import threading

class HTTPSocketWebPageHoster:
    def __init__(self, ip, port, path):
        self.ip = ip
        self.port = int(port)  # Ensure port is an integer
        self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path or "")
        self.httpd = None
        self.server_thread = None

    class HTTPSocketWebPageRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/":
                self.path = "/index.html"  # Default to index.html for root requests
            return super().do_GET()  # Calls the base class method

    def start(self):
        print(f"[PROTOGEN/INFO] Starting web server in path {self.path}")
        if self.httpd is None:
            try:
                # Ensure the path is absolute
                self.path = os.path.abspath(self.path)
                print(f"Resolved path: {self.path}")
                
                # Check if the directory exists
                if not os.path.exists(self.path):
                    print(f"[PROTOGEN/ERROR] The path {self.path} does not exist!")
                    return

                print(f"Changing directory to {self.path}")
                os.chdir(self.path)  # Change directory to serve files from the specified path
                
                # Use the handler class correctly
                handler = self.HTTPSocketWebPageRequestHandler
                # Ensure you're passing the correct handler to TCPServer
                self.httpd = socketserver.TCPServer((self.ip, self.port), handler)
                
                # Start the server in a separate thread
                self.server_thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
                self.server_thread.start()
                print(f"Serving HTTP on {self.ip}:{self.port} from {self.path}")
                
                # Block the main thread so it remains open for logging
                self.server_thread.join()  # This will keep the main thread alive

            except Exception as e:
                print(f"[PROTOGEN/ERROR] Failed to start server: {e}")

    def stop(self):
        if self.httpd:
            try:
                self.httpd.shutdown()
                self.httpd.server_close()
                print(f"Server on {self.ip}:{self.port} stopped")
            except Exception as e:
                print(f"[PROTOGEN/ERROR] Failed to stop server: {e}")
            finally:
                self.httpd = None
        else:
            print("[PROTOGEN/INFO] Server is not running.")