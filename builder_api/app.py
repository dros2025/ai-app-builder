print("Flask app is starting...")
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_ai_model(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # gpt-4o Mini is served through same endpoint
        messages=[
            {"role": "system", "content": "You are a senior fullstack developer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']

@app.route('/generate-project', methods=['POST'])
def generate_project():
    data = request.json
    project_name = data.get("project_name", "my_fullstack_app")
    base_path = os.path.join("generated_projects", project_name)
    
    # Folder structure
    paths = [
        f"{base_path}/backend/routes",
        f"{base_path}/frontend/public",
        f"{base_path}/frontend/src"
    ]
    for path in paths:
        os.makedirs(path, exist_ok=True)

    # Files to generate
    files = {
        f"{base_path}/README.md": "Create a README for a fullstack app using React and Flask.",
        f"{base_path}/backend/app.py": "Write a Flask backend app with CORS enabled and one sample /api/hello route returning JSON.",
        f"{base_path}/backend/routes/api.py": "Write a route /hello that returns {'message': 'Hello from the backend!'} as JSON.",
        f"{base_path}/backend/requirements.txt": "List requirements for Flask and flask-cors.",
        f"{base_path}/frontend/public/index.html": "Basic HTML5 entry file for React app.",
        f"{base_path}/frontend/src/App.jsx": "React component that fetches from /api/hello and displays the result.",
        f"{base_path}/frontend/src/main.jsx": "ReactDOM entry point rendering App.jsx.",
        f"{base_path}/frontend/package.json": "React app config using Vite with dependencies and scripts."
    }

    for path, prompt in files.items():
        content = call_ai_model(prompt)
        with open(path, "w") as f:
            f.write(content)

    return jsonify({"status": "success", "project_path": base_path})

    if __name__ == '__main__':
        app.run(debug=True)
