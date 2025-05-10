from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from datetime import datetime
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('webhook.log'),
        logging.StreamHandler()
    ]
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

def validate_webhook_data(data):
    """Validate webhook data and return any validation errors"""
    errors = []
    
    # Check if data is empty
    if not data:
        errors.append("No data received in request")
        return errors
    
    # Check if data is a dictionary
    if not isinstance(data, dict):
        errors.append("Data must be a JSON object")
        return errors
    
    # Check for required fields
    required_fields = ['linkedin_profile', 'full_name', 'company_name']
    missing_fields = [field for field in required_fields if not data.get(field)]
    
    if missing_fields:
        errors.append(f"Missing required fields: {', '.join(missing_fields)}")
    
    # Validate field types and lengths
    if data.get('linkedin_profile') and not isinstance(data['linkedin_profile'], str):
        errors.append("linkedin_profile must be a string")
    if data.get('full_name') and not isinstance(data['full_name'], str):
        errors.append("full_name must be a string")
    if data.get('company_name') and not isinstance(data['company_name'], str):
        errors.append("company_name must be a string")
    if data.get('description') and not isinstance(data['description'], str):
        errors.append("description must be a string")
    
    return errors

@app.route('/')
def home():
    referrals = Referral.query.order_by(Referral.created_at.desc()).all()
    return render_template('dashboard.html', referrals=referrals)

@app.route('/webhook', methods=['POST', 'OPTIONS'])
def webhook():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        # Log request details
        logging.info(f"Request headers: {dict(request.headers)}")
        logging.info(f"Content-Type: {request.content_type}")
        logging.info(f"Request method: {request.method}")
        
        # Handle different content types
        if request.is_json:
            data = request.get_json(force=True, silent=True)
        elif request.form:
            data = request.form.to_dict()
        elif request.data:
            try:
                data = json.loads(request.data)
            except json.JSONDecodeError:
                data = request.get_data(as_text=True)
        else:
            data = {}
            
        logging.info(f"Received webhook data: {data}")
        
        # Validate the data
        validation_errors = validate_webhook_data(data)
        if validation_errors:
            error_message = "; ".join(validation_errors)
            logging.error(f"Validation errors: {error_message}")
            return jsonify({
                "status": "error",
                "message": error_message
            }), 400
            
        # Create referral
        referral = Referral(
            linkedin_profile=data.get('linkedin_profile', '').strip(),
            full_name=data.get('full_name', '').strip(),
            company_name=data.get('company_name', '').strip(),
            description=data.get('description', '').strip()
        )
        
        try:
            db.session.add(referral)
            db.session.commit()
            logging.info(f"Successfully created referral with ID: {referral.id}")
        except Exception as db_error:
            db.session.rollback()
            logging.error(f"Database error: {str(db_error)}")
            return jsonify({
                "status": "error",
                "message": f"Database error: {str(db_error)}"
            }), 500
        finally:
            db.session.close()
        
        return jsonify({
            "status": "success",
            "message": "Webhook received and data stored successfully",
            "referral_id": referral.id,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logging.error(f"Error processing webhook: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/referrals')
def get_referrals():
    try:
        referrals = Referral.query.order_by(Referral.created_at.desc()).all()
        return render_template('referrals.html', referrals=referrals)
    except Exception as e:
        logging.error(f"Error fetching referrals: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/referrals/<int:id>/status', methods=['POST'])
def update_referral_status(id):
    try:
        data = request.get_json()
        new_status = data.get('status')
        
        if not new_status or new_status not in ['pending', 'accepted', 'rejected']:
            return jsonify({
                "status": "error",
                "message": "Invalid status"
            }), 400
            
        referral = Referral.query.get_or_404(id)
        referral.status = new_status
        
        try:
            db.session.commit()
            return jsonify({
                "status": "success",
                "message": f"Referral status updated to {new_status}"
            })
        except Exception as db_error:
            db.session.rollback()
            raise Exception(f"Database error: {str(db_error)}")
        finally:
            db.session.close()
            
    except Exception as e:
        logging.error(f"Error updating referral status: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Use port 5001 to avoid conflicts
    port = int(os.environ.get('PORT', 5001))
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True) 