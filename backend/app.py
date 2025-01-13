from flask import Flask
from routes.routes import init_routes
from db.db import init_app
from flask_cors import CORS
# Initialize Flask app
app = Flask(__name__)

cors = CORS(app, resources={
    r"/*": {
        "origins": "https://quizzzer-app.netlify.app/",  # Frontend URL
        # Allow sending cookies
        "supports_credentials": True 
        }
})
# Initialize database functions
init_app(app)

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
