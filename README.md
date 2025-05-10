# Zapier Flask Webhook Integration

This project is a Flask-based backend that receives webhook POST requests from Zapier, typically triggered by changes in a Google Sheet. The data is validated and stored in a local SQLite database, and a simple dashboard is provided to view all referrals.

## Features
- Receives data from Zapier via a webhook endpoint
- Validates and stores referral data in a SQLite database
- Simple web dashboard to view all referrals
- Integration-ready for Google Sheets via Zapier
- CORS enabled for easy integration
- Logging of all webhook requests

## Requirements
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- python-dotenv
- ngrok (for local development/testing with Zapier)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/zapier-flask-webhook.git
   cd zapier-flask-webhook
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database (optional test data):**
   ```bash
   python init_db.py
   ```

5. **Run the Flask app:**
   ```bash
   python app.py
   ```
   The app will run on `http://localhost:5001/` by default.

6. **(Optional) Expose your local server to the internet with ngrok:**
   ```bash
   ngrok http 5001
   ```
   Use the HTTPS URL provided by ngrok in your Zapier webhook configuration.

## Usage

- **Webhook Endpoint:**
  - `POST /webhook`
  - Expects JSON with the following fields:
    - `linkedin_profile` (string, required)
    - `full_name` (string, required)
    - `company_name` (string, required)
    - `description` (string, optional)

- **Dashboard:**
  - Visit `http://localhost:5001/` to view all referrals in a web dashboard.

- **View database in terminal:**
  - Run `python view_db.py` to print all referrals in the database.

## Zapier Setup

1. **Trigger:** Google Sheets (New or Updated Row)
2. **Formatter (optional):** Clean up or split fields as needed
3. **Webhooks by Zapier (POST):**
   - URL: `https://<your-ngrok-url>/webhook`
   - Payload Type: `json`
   - Data:
     - `linkedin_profile`: (map to LinkedIn URL field)
     - `full_name`: (map to Full Name field)
     - `company_name`: (map to Company Name field)
     - `description`: (optional)

## Deployment
- For production, deploy to a cloud service (Heroku, AWS, etc.) and use a production WSGI server (e.g., Gunicorn).
- Update the database URI and environment variables as needed.

## Security Notes
- Do not expose your local development server to the public internet except for testing.
- Consider adding authentication or secret validation for production use.

## License
MIT 