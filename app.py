from flask import Flask, request, jsonify, send_from_directory
import json
import os
import time

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))

@app.route('/')
def home():
    return "Debug Server - Resource OK", 200

# Resource - Debug
@app.route('/resource/')
@app.route('/resource/<path:path>')
def serve_resource(path=""):
    directory = 'static/resource'
    try:
        if not path:
            return "Resource root OK", 200
        full = os.path.join(directory, path)
        print(f"[RESOURCE] Requested: {path} | Exists: {os.path.exists(full)}")
        if os.path.exists(full):
            if os.path.isdir(full):
                return f"Dir OK: {path}", 200
            return send_from_directory(directory, path)
        return f"Missing: {path}", 404
    except Exception as e:
        return f"Res Error: {str(e)}", 404

# Static
@app.route('/static/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('static', path)
    except:
        return "Static Error", 404

@app.route('/<path:path>')
def serve_other(path):
    try:
        return send_from_directory('static', path)
    except:
        return "Not Found", 404

# API - Debug chi tiết
@app.route('/api/<path:endpoint>', methods=['GET', 'POST'])
def fake_api(endpoint):
    print(f"[API DEBUG] {request.method} /api/{endpoint} | Query: {request.args.to_dict()} | Body: {request.get_json(silent=True)}")
    
    # Fake hầu hết các endpoint game hay gọi
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "user_id": 1000001,
            "nickname": "DebugPlayer",
            "level": 999,
            "vip_level": 12,
            "token": "debug_token_123",
            "server_time": int(time.time())
        }
    })

if __name__ == '__main__':
    print("=== DEBUG SERVER STARTED ===")
    app.run(host='0.0.0.0', port=PORT, debug=True)
