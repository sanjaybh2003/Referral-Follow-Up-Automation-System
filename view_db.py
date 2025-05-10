from app import app, db, Referral

def view_referrals():
    with app.app_context():
        referrals = Referral.query.all()
        print("\nAll Referrals in Database:")
        print("-" * 80)
        print(f"{'ID':<5} {'Full Name':<20} {'Company':<20} {'Status':<10} {'Created At'}")
        print("-" * 80)
        
        for ref in referrals:
            print(f"{ref.id:<5} {ref.full_name:<20} {ref.company_name:<20} {ref.status:<10} {ref.created_at}")
        
        print("-" * 80)
        print(f"Total referrals: {len(referrals)}")

if __name__ == "__main__":
    view_referrals() 