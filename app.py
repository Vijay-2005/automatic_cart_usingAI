import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API key
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyBAtmmFhg7XjMCozgh_6paz-nBN-IUgXAQ')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ingredients', methods=['POST'])
def get_ingredients():
    data = request.get_json()
    user_input = data.get('user_input', '')
    prompt = f"List all the ingredients needed to make {user_input}. Respond with a simple comma-separated list only. No extra text."
    response = model.generate_content(prompt)
    ingredients = [item.strip() for item in response.text.split(',') if item.strip()]
    return jsonify({'ingredients': ingredients})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)