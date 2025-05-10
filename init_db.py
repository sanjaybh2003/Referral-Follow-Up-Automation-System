from app import app, db, Referral
from datetime import datetime

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Add some test data
        test_referrals = [
            Referral(
                linkedin_profile="https://linkedin.com/test1",
                full_name="Test User 1",
                company_name="Test Company 1",
                description="Test Description 1",
                created_at=datetime.utcnow(),
                status="pending"
            ),
            Referral(
                linkedin_profile="https://linkedin.com/test2",
                full_name="Test User 2",
                company_name="Test Company 2",
                description="Test Description 2",
                created_at=datetime.utcnow(),
                status="accepted"
            )
        ]
        
        # Add test data to database
        for referral in test_referrals:
            db.session.add(referral)
        
        # Commit the changes
        db.session.commit()
        
        print("Database initialized with test data!")

if __name__ == "__main__":
    init_db() 