from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)
data_file = 'apps.json'

@app.route('/')
def serve_index():
    
    return send_from_directory('.', 'index.html')

@app.route('/add_app', methods=['POST'])
def add_app():
   
    new_app = request.get_json()
    apps = load_apps()
    category = new_app.get('category')
    if category not in apps:
        apps[category] = []
    apps[category].append(new_app)
    save_apps(apps)
    return jsonify({"status": "App added"}), 201

@app.route('/apps/<category>', methods=['GET'])
def get_apps(category):
    
    apps = load_apps()
    return jsonify(apps.get(category, []))

@app.route('/delete_app/<category>/<name>', methods=['DELETE'])
def delete_app(category, name):
    
    apps = load_apps()
    if category in apps:
        apps[category] = [app for app in apps[category] if app['name'] != name]
        save_apps(apps)
    return jsonify({"status": "App deleted"}), 200

def load_apps():
    
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return {}

def save_apps(apps):
    
    with open(data_file, 'w') as file:
        json.dump(apps, file)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
