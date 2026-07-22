from flask import Flask, request, jsonify, send_from_directory
import json
import os
import time

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))

activity_data = {}

@app.route('/')
def home():
    return "Private Server Debug Mode", 200

# Resource
@app.route('/resource/')
@app.route('/resource/<path:path>')
def serve_resource(path=""):
    try:
        if not path:
            return "Resource OK", 200
        return send_from_directory('static/resource', path)
    except Exception as e:
        return f"Resource Error: {str(e)}", 404

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

# API Debug
@app.route('/api/<path:endpoint>', methods=['GET', 'POST'])
def fake_api(endpoint):
    print(f"[DEBUG API] {request.method} /api/{endpoint} | Args: {request.args} | Body: {request.get_json(silent=True)}")
    
    if any(x in endpoint.lower() for x in ["login", "auth", "user", "player", "init", "get_ver", "server"]):
        return jsonify({
            "code": 0,
            "data": {
                "user_id": 1000001,
                "nickname": "DebugPlayer",
                "level": 999,
                "vip_level": 12,
                "token": "debug_token",
                "server_time": int(time.time())
            }
        })
    
    if any(x in endpoint.lower() for x in ["activity", "event", "task", "reward"]):
        return jsonify({"code": 0, "data": activity_data})
    
    return jsonify({"code": 0, "data": {}})

if __name__ == '__main__':
    print("=== DEBUG SERVER STARTED ===")
    app.run(host='0.0.0.0', port=PORT, debug=True)
