from flask import Flask, render_template_string, request

app = Flask(__name__)

# Sample data for demonstration
camera_data = {
    '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8': {'id': '11', 'status': 'Inactive', 'flag': ''},
    '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9': {'id': '0', 'status': 'Active', 'flag': 'root@localhost{770a058a80a9bca0a87c3e2ebe1ee9b2}'},
    '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b': {'id': '1', 'status': 'Inactive', 'flag': ''},
    'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35': {'id': '2', 'status': 'Inactive', 'flag': ''},
    '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce': {'id': '3', 'status': 'Inactive', 'flag': ''},
    '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce': {'id': '4', 'status': 'Inactive', 'flag': ''},
    'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d': {'id': '5', 'status': 'Inactive', 'flag': ''},
    'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683': {'id': '6', 'status': 'Inactive', 'flag': ''},
    '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451': {'id': '7', 'status': 'Inactive', 'flag': ''},
    '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3': {'id': '8', 'status': 'Inactive', 'flag': ''},
    '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7': {'id': '9', 'status': 'Inactive', 'flag': ''},
    '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5': {'id': '10', 'status': 'Inactive', 'flag': ''},
    '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918': {'id': '12', 'status': 'Inactive', 'flag': ''},
    '3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278': {'id': '13', 'status': 'Inactive', 'flag': ''},
    '8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61': {'id': '14', 'status': 'Inactive', 'flag': ''},
    'e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb': {'id': '15', 'status': 'Inactive', 'flag': ''},
    'b17ef6d19c7a5b1ee83b907c595526dcb1eb06db8227d650d5dda0a9f4ce8cd9': {'id': '16', 'status': 'Inactive', 'flag': ''},
    '4523540f1504cd17100c4835e85b7eefd49911580f8efff0599a8f283be6b9e3': {'id': '17', 'status': 'Inactive', 'flag': ''},
    '4ec9599fc203d176a301536c2e091a19bc852759b255bd6818810a42c5fed14a': {'id': '18', 'status': 'Inactive', 'flag': ''},
    '9400f1b21cb527d7fa3d3eabba93557a18ebe7a2ca4e471cfe5e4c5b4ca7f767': {'id': '19', 'status': 'Inactive', 'flag': ''},
    'f5ca38f748a1d6eaf726b8a42fb575c3c71f1864a8143301782de13da2d9202b': {'id': '20', 'status': 'Inactive', 'flag': ''},
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
    # Handling IDs 0 to 20, with only ID 0 having an active status and a flag
    if sha256_hash in camera_data:
        return camera_data[sha256_hash]
    return {'id': 'Unknown', 'status': 'Inactive', 'flag': ''}

@app.route('/')
def index():
    camera_hash = request.args.get('camera', 'f5ca38f748a1d6eaf726b8a42fb575c3c71f1864a8143301782de13da2d9202b')
    camera_info = sha256_to_id(camera_hash)
    
    if camera_info['status'] == 'Active':
        return render_template_string(ACTIVE_PAGE, user_id=camera_info['id'], status=camera_info['status'], flag=camera_info['flag'])
    else:
        return render_template_string(ACTIVE_PAGE,user_id=camera_info['id'], status=camera_info['status'], flag=camera_info['flag'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5)
