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

### 1. **Clone the Repository**

```powershell
git clone https://github.com/IbtissamBenabid/INFRALINKER.git
cd INFRALINKER
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
flask db upgrade
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