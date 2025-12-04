#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple HTTP server to run the ID Generator
Open your browser and go to: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n{'='*60}")
        print(f"  ID Generator Server đã khởi động!")
        print(f"{'='*60}")
        print(f"\n  Mở trình duyệt tại: {url}")
        print(f"\n  Nhấn Ctrl+C để dừng server")
        print(f"{'='*60}\n")
        
        # Tự động mở trình duyệt
        webbrowser.open(url)
        
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\nServer đã dừng. Tạm biệt!")
    sys.exit(0)
except OSError as e:
    if e.errno == 10048:  # Port already in use
        print(f"\nLỗi: Port {PORT} đã được sử dụng!")
        print(f"Vui lòng đóng ứng dụng khác đang dùng port {PORT} hoặc đổi port khác.")
    else:
        print(f"\nLỗi: {e}")
    sys.exit(1)

