from attendance import db
from attendance.models import *

# This will create all tables defined in models.py
db.create_all()

print("✅ Database created successfully!")
