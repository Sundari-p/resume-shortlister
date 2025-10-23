from flask import Flask, request, jsonify
from parser import extract_skills

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    skills = extract_skills(file)
    return jsonify({"skills": skills})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
