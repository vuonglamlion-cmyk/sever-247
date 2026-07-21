from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

# ====================== CẤU HÌNH ======================
PORT = int(os.environ.get('PORT', 5000))
DATA_FOLDER = "data"

# Load dữ liệu sự kiện
def load_activity_data():
    try:
        with open(f"{DATA_FOLDER}/full/all_activity_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Không load được activity data:", e)
        return {}

activity_data = load_activity_data()

@app.route('/')
def home():
    return "Tiên Nghịch Private Server - Đang chạy ổn định", 200

# Phục vụ file tĩnh (index.html, resource, js, hình ảnh...)
@app.route('/<path:path>')
def serve_static(path):
    try:
        if path.startswith('resource/'):
            return send_from_directory('static', path)
        return send_from_directory('static', path)
    except:
        return "File not found", 404

# Fake API cho game
@app.route('/api/<path:endpoint>', methods=['GET', 'POST'])
def fake_api(endpoint):
    print(f"[API] {request.method} /api/{endpoint}")
    
    # Fake login
    if "login" in endpoint or "auth" in endpoint or "user/info" in endpoint:
        return jsonify({
            "code": 0,
            "msg": "success",
            "data": {
                "user_id": 999999,
                "nickname": "TestPlayer",
                "level": 999,
                "vip_level": 12,
                "server_id": 1,
                "token": "private_server_token_123"
            }
        })
    
    # Fake activity / event
    if any(x in endpoint for x in ["activity", "event", "task", "reward"]):
        return jsonify({
            "code": 0,
            "data": activity_data
        })
    
    # Mặc định trả về thành công
    return jsonify({"code": 0, "msg": "success", "data": {}})

if __name__ == '__main__':
    print(f"Server chạy tại port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)