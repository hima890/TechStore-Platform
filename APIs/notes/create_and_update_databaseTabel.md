### **1. Set Up the Project Structure**

### **2. Create the model Model**

1. **Navigate to the `models.py` file in your `APIs/v1/` directory** (create this file if it doesn’t exist). This file will contain the SQLAlchemy models for your app.


4. **Define the Model** in `models.py`:

```python
# APIs/v1/models.py

from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(50), unique=True, nullable=True)
    profile_image = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```

### **3. Configure the Application to Use the Database**

Make sure your `config.py` (both in the main config and instance config) includes the database configuration:

```python
# APIs/v1/config.py

import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'databases', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### **4. Run the Migration and Create the Table**

1. **Initialize Flask-Migrate** by running the following command:
   ```bash
   flask db init
   ```

2. **Create a migration** for the `User` model:
   ```bash
   flask db migrate -m "Create User table"
   ```

3. **Apply the migration** to create the table in the database:
   ```bash
   flask db upgrade
   ```

### **5. Verify the Setup**

1. **Run the application** and ensure that no errors occur during startup.
   ```bash
   flask run
   ```

2. **Check the database** to confirm that the `users` table has been created in the `databases/app.db` file.

This process sets up the `User` model using best practices, ensuring a well-organized, scalable, and maintainable codebase.