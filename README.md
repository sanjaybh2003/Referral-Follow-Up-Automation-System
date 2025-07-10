# 🤖 Referral Follow-Up Automation System

A full-stack automation system built with **Flask**, **SQLite**, **Zapier**, and **Google Forms**, designed to streamline referral tracking and networking follow-ups.

## 🚀 Features

- Automates storage of referral data from Google Forms to SQLite
- Sends follow-up reminders via Google Calendar using Zapier webhooks
- Custom dashboard to track referral status: pending, accepted, etc.
- Acts as a personal CRM to manage professional connections

## 🔧 Tech Stack

- **Frontend**: Google Forms (as input UI)
- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Automation**: Zapier Webhooks + Google Sheets + Google Calendar
- **IDE**: Cursor (for debugging & intelligent suggestions)

## 📸 Screenshots

### 🔍 Dashboard View  
![Dashboard](screenshots/dashboard.png)

### 📨 Submitted Referral Example  
![Referral](screenshots/referral.png)

> _Tip: Rename your images like `dashboard.png`, `referral.png` inside the `/screenshots` folder._

## 🛠️ Setup Instructions

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
