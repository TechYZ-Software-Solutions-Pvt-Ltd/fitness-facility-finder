"""
Initialize database tables for JustList application.
Run this once before starting the app for the first time.
"""

from src.app.database.connection import engine, Base
from src.app.database.models import User, SearchHistory, Facility

def init_db():
    """Create all database tables."""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        print("   - users")
        print("   - search_history")
        print("   - facilities")
        print("\n🎉 Database is ready! You can now start the application.")
    except Exception as e:
        print(f"❌ Error creating database tables: {e}")
        print("\nPlease check:")
        print("  - Database file permissions")
        print("  - data/ directory exists")
        print("  - SQLite is installed")

if __name__ == "__main__":
    init_db()

