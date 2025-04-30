from flask import Flask, request, jsonify
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure logging - only file handler to reduce overhead
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='webhook.log',
    filemode='a'
)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "active", "message": "Webhook server is running"}), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the data from the request
        data = request.get_json(force=True, silent=True) or request.form.to_dict()
        
        # Log the received data
        logging.info(f"Received webhook data: {data}")
        
        return jsonify({
            "status": "success",
            "message": "Webhook received successfully",
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logging.error(f"Error processing webhook: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    # Disable debug mode for production-like performance
    app.run(host='0.0.0.0', port=port, debug=False) 