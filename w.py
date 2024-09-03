from flask import Flask, render_template_string, request
import hashlib

app = Flask(__name__)

# Sample data for demonstration
camera_data = {
    '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8': {'id': '11', 'status': 'Active', 'flag': 'flag{770a058a80a9bca0a87c3e2ebe1ee9b2}'},
    '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9': {'id': '0', 'status': 'Inactive', 'flag': ''}
}

# HTML templates
ACTIVE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iDoor</title>
    <style>
        body { background-color: white; font-family: Arial, sans-serif; color: black; }
        .container { display: flex; justify-content: space-between; padding: 20px; }
        .camera-view { width: 70%; height: 80vh; border: 2px solid #ccc; }
        .controls { display: flex; gap: 10px; margin-top: 20px; }
        .sidebar { width: 25%; padding: 20px; background-color: #f5f5f5; }
        button { padding: 10px 15px; font-size: 14px; cursor: pointer; }
        .active { color: green; }
    </style>
</head>
<body>
    <div class="container">
        <div class="camera-view">
            <!-- Placeholder for Camera View -->
        </div>
        <div class="sidebar">
            <h2>iDoor</h2>
            <p>Customer ID: <strong>{{ user_id }}</strong></p>
            <p>Camera Status: <strong class="active">{{ status }}</strong></p>
            <p>Flag: <strong>{{ flag }}</strong></p>
        </div>
    </div>
    <div class="controls">
        <button style="background-color: blue; color: white;">Zoom In</button>
        <button style="background-color: grey; color: white;">Zoom Out</button>
        <button style="background-color: green; color: white;">Capture</button>
        <button style="background-color: red; color: white;">Record</button>
        <button style="background-color: orange; color: white;">Pan Left</button>
        <button style="background-color: yellow; color: black;">Pan Right</button>
    </div>
</body>
</html>
"""

INACTIVE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iDoor</title>
    <style>
        body { background-color: white; font-family: Arial, sans-serif; color: black; }
        .container { display: flex; justify-content: space-between; padding: 20px; }
        .camera-view { width: 70%; height: 80vh; border: 2px solid #ccc; }
        .sidebar { width: 25%; padding: 20px; background-color: #f5f5f5; }
        .inactive { color: red; }
    </style>
</head>
<body>
    <div class="container">
        <div class="camera-view">
            <!-- Placeholder for Camera View -->
        </div>
        <div class="sidebar">
            <h2>iDoor</h2>
            <p>Customer ID: <strong>Inactive</strong></p>
            <p>Camera Status: <strong class="inactive">Inactive</strong></p>
        </div>
    </div>
</body>
</html>
"""

def sha256_to_id(sha256_hash):
    return camera_data.get(sha256_hash, {'id': 'Unknown', 'status': 'Unknown', 'flag': ''})

@app.route('/')
def index():
    camera_hash = request.args.get('camera', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9')
    camera_info = sha256_to_id(camera_hash)
    
    if camera_info['status'] == 'Active':
        return render_template_string(ACTIVE_PAGE, user_id=camera_info['id'], status=camera_info['status'], flag=camera_info['flag'])
    else:
        return render_template_string(INACTIVE_PAGE)

if __name__ == '__main__':
    app.run(debug=True)

