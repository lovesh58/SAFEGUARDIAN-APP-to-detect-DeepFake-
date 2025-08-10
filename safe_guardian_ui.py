from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='frontend/build')

# --- API Endpoints ---

@app.route('/api/scan_media', methods=['POST'])
def scan_media():
    """Scan uploaded media for deepfakes (mock implementation)."""
    file = request.files.get('media')
    # Here, integrate with real deepfake detection model
    result = {
        "detected": True,
        "confidence": 0.93,
        "clues": [
            {"type": "face_artifact", "description": "Unusual facial warping"},
            {"type": "audio_mismatch", "description": "Voice does not match lip movement"}
        ],
        "avatar": "detective_avatar_1.png",
        "next_steps": [
            "Review evidence cards",
            "Learn how to spot deepfakes",
            "Report if suspicious"
        ]
    }
    return jsonify(result)

@app.route('/api/evidence_board', methods=['GET'])
def evidence_board():
    """Return evidence board data (mock for UI demo)."""
    board = {
        "cases": [
            {"id": 1, "title": "Case File: Viral Meme", "status": "open"},
            {"id": 2, "title": "Case File: Celebrity Video", "status": "closed"},
        ],
        "clues": [
            {"id": 101, "type": "image", "description": "Magnified pixel anomaly"},
            {"id": 102, "type": "text", "description": "Suspicious comment pattern"},
        ]
    }
    return jsonify(board)

@app.route('/api/learning_modules', methods=['GET'])
def get_learning_modules():
    """Return detective-style learning modules and quizzes."""
    modules = [
        {"id": "quiz1", "name": "Spot the Deepfake", "type": "quiz", "badge": "Magnifier"},
        {"id": "mission1", "name": "Mission: Evidence Hunt", "type": "mission", "badge": "Evidence Folder"},
    ]
    return jsonify(modules)

@app.route('/api/case_stories', methods=['GET', 'POST'])
def case_stories():
    """Community stories and reporting."""
    if request.method == 'POST':
        # Accept story/report submission
        story = request.json
        return jsonify({"status": "received", "story": story}), 201
    else:
        # Return mock stories
        stories = [
            {"user": "TeenDetective42", "case": "Spotted a fake celeb vid", "upvotes": 12},
            {"user": "SafetySquad", "case": "Shared tips for safe browsing", "upvotes": 8},
        ]
        return jsonify(stories)

# --- Serve React Frontend ---

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve React frontend."""
    if path != "" and app.static_folder:
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# --- Accessibility & Metadata ---

@app.route('/api/accessibility', methods=['GET'])
def accessibility_info():
    """Accessibility guidelines for frontend (for devs/designers)."""
    info = {
        "color_contrast": "AA+ recommended",
        "iconography": "All icons have descriptive alt text",
        "alerts": "Popups are keyboard-navigable, readable by screen readers",
        "language": "Plain, inclusive, short sentences for teens"
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)