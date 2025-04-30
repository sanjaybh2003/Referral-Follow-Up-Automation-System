# Zapier-Flask Webhook Integration

A Flask-based webhook server that receives and logs data from Zapier integrations. This project is specifically designed to handle form submissions and LinkedIn profile data through Zapier workflows.

## Features

- Webhook endpoint for receiving Zapier data
- Automatic logging of received data
- Support for both JSON and form data
- Easy deployment options (local, Heroku, etc.)
- Configurable port settings

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sanjaybh2003/Zapier-Flask-Webhook.git
cd Zapier-Flask-Webhook
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## Usage with Zapier

1. Start the Flask server locally
2. Use a tunnel service (like localtunnel) to expose your local server:
```bash
npx localtunnel --port 3000
```

3. In your Zapier workflow:
   - Add a Webhook action
   - Set the method to POST
   - Use the provided tunnel URL + "/webhook"
   - Configure your form data fields

## Environment Variables

Create a `.env` file with:
```
PORT=3000  # Optional, defaults to 3000
```

## Logging

All webhook data is logged to:
- `webhook.log` file in the project directory

## License

MIT License 