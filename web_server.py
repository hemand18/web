import http.server
import socketserver

# Define the port you want to use
PORT = 8000

# Create a handler that serves files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Bind the server to the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()