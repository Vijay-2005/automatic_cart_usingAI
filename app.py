import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from flask_cors import CORS  # Import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure Gemini API key from environment variables
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ingredients', methods=['POST'])
def get_ingredients():
    try:
        data = request.get_json()
        user_input = data.get('user_input', '')
        if not user_input:
            return jsonify({'error': 'No input provided', 'ingredients': []}), 400
        
        prompt = f"List all the ingredients needed to make {user_input}. Respond with a simple comma-separated list only. No extra text."
        response = model.generate_content(prompt)
        ingredients = [item.strip() for item in response.text.split(',') if item.strip()]
        
        print(f"Successfully processed request for: {user_input}")
        print(f"Found {len(ingredients)} ingredients: {ingredients}")
        
        return jsonify({'ingredients': ingredients})
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e), 'ingredients': []}), 500

# Remove the app.run() code for production deployment
if __name__ == '__main__':
    # This section will only run when testing locally
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Flask app on http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)