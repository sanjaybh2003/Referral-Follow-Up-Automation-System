# Zapier Webhook Receiver

A simple Flask application that receives and logs webhook data from Zapier.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file (optional):
```
PORT=5000
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. The webhook endpoint will be available at:
```
http://localhost:5000/webhook
```

## Webhook Endpoint

- **URL**: `/webhook`
- **Method**: POST
- **Content-Type**: application/json

The endpoint will:
1. Receive JSON data from Zapier
2. Log the data to both console and `webhook.log` file
3. Return a success response

## Logging

All webhook data is logged to:
- Console output
- `webhook.log` file in the project directory

## Zapier Integration

In your Zapier workflow:
1. Add a "Webhook" action
2. Set the method to POST
3. Enter your webhook URL (e.g., `http://your-server:5000/webhook`)
4. Configure the data you want to send in the request body 