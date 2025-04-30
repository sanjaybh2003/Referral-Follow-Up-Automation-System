from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging - only file handler to reduce overhead
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='webhook.log',
    filemode='a'
)

# Define Referral model
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linkedin_profile = db.Column(db.String(500))
    full_name = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='pending')
    
    def to_dict(self):
        return {
            'id': self.id,
            'linkedin_profile': self.linkedin_profile,
            'full_name': self.full_name,
            'company_name': self.company_name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'status': self.status
        }

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "active",
        "message": "Webhook server is running",
        "endpoints": {
            "webhook": "/webhook",
            "referrals": "/referrals"
        }
    }), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the data from the request
        data = request.get_json(force=True, silent=True) or request.form.to_dict()
        
        # Log the received data
        logging.info(f"Received webhook data: {data}")
        
        # Create new referral record
        referral = Referral(
            linkedin_profile=data.get('linkedin_profile', ''),
            full_name=data.get('full_name', ''),
            company_name=data.get('company_name', ''),
            description=data.get('description', '')
        )
        
        # Save to database
        db.session.add(referral)
        db.session.commit()
        
        return jsonify({
            "status": "success",
            "message": "Webhook received and data stored successfully",
            "referral_id": referral.id,
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logging.error(f"Error processing webhook: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/referrals', methods=['GET'])
def get_referrals():
    try:
        referrals = Referral.query.order_by(Referral.created_at.desc()).all()
        return jsonify({
            "status": "success",
            "referrals": [referral.to_dict() for referral in referrals]
        }), 200
    except Exception as e:
        logging.error(f"Error fetching referrals: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    # Disable debug mode for production-like performance
    app.run(host='0.0.0.0', port=port, debug=False) 