# INFRALINKER

InfraLinker is an IT infrastructure management platform.

---

## 🚩 Main Corrections & Modifications

- **Flask Routing:**  
  All `url_for('admin.new_project_document')` and similar calls now always include required parameters (e.g., `project_id`), fixing `BuildError` issues.
- **Form Handling:**  
  File uploads and form submissions are validated and errors are displayed in templates.
- **Database Alignment:**  
  SQLAlchemy models and MariaDB table structures are synchronized.
- **Error Handling:**  
  All `try:` blocks have matching `except` blocks to avoid syntax errors.
- **CSV Import:**  
  Bulk import for servers, devices, networks, racks, and applications via CSV is supported.
- **Sample Data:**  
  Example SQL scripts provided for populating `vulnerabilities` and `tickets` tables.
- **Windows Compatibility:**  
  All instructions and scripts are tested for Windows with MariaDB.

---

## 🖥️ How to Use on Windows with MariaDB

### 1. **Clone the updated  Repository**

```powershell
git clone https://github.com/IbtissamBenabid/INFRALINKER.git
cd INFRALINKER

# Source repo : 
git clone https://github.com/Infralinker/Infralinker.git
cd Infralinker

```


### 2. **Set Up Python Virtual Environment**

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### 2b. **Manual Python Package Installation (if `requirements.txt` fails or is incomplete)**

If you encounter errors with `pip install -r requirements.txt`, you can manually install the main dependencies with:

```powershell
pip install flask flask_sqlalchemy flask_login flask_wtf flask_bootstrap flask_migrate pymysql pandas plotly
```

If you use MariaDB and encounter issues, also run:

```powershell
pip install mysqlclient
```

**Other common packages you may need:**

```powershell
pip install python-dotenv email-validator
```

If you see an ImportError for any other package, install it using:

```powershell
pip install <package-name>
```

--- 
### 3. **Configure MariaDB**

- Install MariaDB and create a database (e.g., `infralinker_db`).
- Update your `instance/config.py` with the correct DB URI:
  ```
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/infralinker_db"
  ```

### 4. **Initialize the Database**

```powershell
# Initialize migrations directory (run once)
flask db init

# Generate a new migration after model changes
flask db migrate -m "Initial migration."

# Apply migrations to the database
flask db upgrade

# (Optional) Downgrade the database to the previous migration
flask db downgrade
```
Or run your custom install script if provided.

### 5. **Populate Sample Data (Optional)**

**For vulnerabilities:**
```sql
INSERT INTO vulnerabilities (
    title_vulnerability, date_vulnerability, cvs_code, severity, risk, impact,
    ticket_id, admin_id, recommanded_solution, vulnerabitlity_note, add_by, add_date
) VALUES
('SQL Injection', '2025-05-30', 'CVE-2025-0001', 'High', 'Critical', 'Database compromise', NULL, 1, 'Sanitize all user inputs.', 'Detected during routine scan.', 1, NOW());
```

**For tickets:**
```sql
INSERT INTO tickets (
    ticket_number, open_date, description, supplier_id, platform_id, admin_id,
    priority, impact, status, resolution_date, comments, add_by, add_date
) VALUES
('TCK-2025-001', '2025-05-30', 'Server not responding after update.', 1, 1, 1, 'High', 'Service Down', 'OPEN', NULL, 'Urgent attention needed.', 1, NOW());
```
---

### 5b. **Créer un utilisateur admin (obligatoire pour la première connexion)**

Après avoir initialisé la base, créez un utilisateur admin directement en SQL :

```sql
INSERT INTO admins (
    firstname, lastname, email, phone, function, password_hash, is_admin, is_manager, add_date
) VALUES (
    'Admin', 'User', 'admin@infralinker.com', '0600000000', 'Administrateur',
    '<mot_de_passe_hashé>', 1, 1, NOW()
);
```

> **Remarque :**  
> - Remplacez `<mot_de_passe_hashé>` par le hash du mot de passe généré avec Flask (par exemple avec `werkzeug.security.generate_password_hash('votre_mot_de_passe')` dans un shell Python).
> - Vous pouvez aussi créer l’admin via un script Python utilisant vos modèles SQLAlchemy, par exemple :

```python
from app import create_app, db
from app.models import Admin
from werkzeug.security import generate_password_hash
import datetime

app = create_app('development')
with app.app_context():
    admin = Admin(
        firstname="Admin",
        lastname="User",
        email="admin@infralinker.com",
        phone="0600000000",
        function="Administrateur",
        password_hash=generate_password_hash("votre_mot_de_passe"),
        is_admin=True,
        is_manager=True,
        add_date=datetime.datetime.now()
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin créé avec succès.")
```


### 6. **Run the Application**

```powershell
python run.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🛠️ Notable Project Modifications

- All Flask routes requiring parameters now enforce them in both Python and templates.
- Error handling and flash messages improved for all forms and database actions.
- File upload and CSV import logic fixed for Windows paths.
- Added sample SQL for quick database population.
- README and documentation updated for Windows/MariaDB usage.

---

## 📝 Contribution

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

---

## 📧 Support

For issues, please use the [GitHub Issues](https://github.com/IbtissamBenabid/INFRALINKER/issues) page.

---

**Enjoy managing your infrastructure with InfraLinker!**