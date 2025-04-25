# AI Recipe Cart

A simple Flask web app that uses Google Gemini API to generate and add recipe ingredients to your cart based on your input.

## Features
- Enter a dish name (e.g., "paneer curry") and get all required ingredients added to your cart.
- Powered by Gemini API for accurate ingredient lists.

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. (Optional) Set your Gemini API key as an environment variable:
   ```
   set GEMINI_API_KEY=your-api-key-here
   ```
   By default, the demo key in the code will be used.
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser and go to http://127.0.0.1:5000

## File Structure
- `app.py`: Flask backend and Gemini API logic
- `templates/index.html`: Frontend UI
- `requirements.txt`: Dependencies
- `README.md`: This file

## Notes
- For production, use your own Gemini API key for better security and quota.
- The app is for demonstration purposes.
