# AI Recipe Cart - Project Map Structure

```
📦 Ai_cart3/
│
├── 📜 app.py                  # Main Flask application
│   ├── Routes
│   │   ├── / (GET)            # Serves the main application page
│   │   └── /get_ingredients (POST) # API endpoint for fetching recipe ingredients
│   │
│   └── Services
│       └── Gemini AI          # Processes recipe requests to get ingredients list
│
├── 📜 README.md               # Project documentation
│
├── 📜 requirements.txt        # Python dependencies
│
├── 📜 vercel.json             # Vercel deployment configuration
│
└── 📂 templates/
    └── 📜 index.html          # Frontend application with CSS and JavaScript
        ├── UI Components
        │   ├── Recipe Input   # Search box with input field and Add button
        │   ├── Recipe Preview # Preview section for the requested recipe
        │   └── Cart Section   # Shopping cart with ingredients list
        │
        └── JavaScript
            ├── API Communication # Handles requests to the Flask backend
            ├── Cart Management   # Add/remove cart items functionality
            └── UI States         # Loading states and UI updates
```

## Application Flow

1. User enters a recipe name in the input field
2. Frontend sends request to `/get_ingredients` endpoint
3. Flask backend processes the request using Gemini AI
4. AI generates ingredient list and sends it back to frontend
5. Frontend displays ingredients in the shopping cart
6. User can manage items in the cart (remove items, clear cart)

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **AI**: Google Gemini AI (generative-2.0-flash model)
- **Deployment**: Vercel

## Key Features

- AI-powered ingredient extraction from recipe names
- Responsive design for mobile and desktop
- Visual representation of ingredients with images
- Simple and intuitive cart management
