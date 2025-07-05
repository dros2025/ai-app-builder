# 🛠️ AI App Builder

This project is a self-hosted AI-powered assistant that builds full-stack Python web apps on demand.

## 🚀 Features

- Accepts app ideas via Open WebUI
- Automatically structures and saves files to `/apps/{app_name}/`
- Flask-compatible layout with routes, templates, and static files
- Preview and edit generated projects locally

## 🧪 How to Use

1. Start Open WebUI and Ollama.
2. Make sure your Flask API is running:
   ```bash
   cd builder_api
   source ../venv/bin/activate
   python3 app.py

