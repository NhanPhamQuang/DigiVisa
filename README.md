# Visa Service UI - FastAPI

Full UI prototype for VisaHub:

- Public homepage, visa detail, application flow, profile, sign in/sign up
- Admin dashboard with dropdown sidebar
- Visa orders tabs + pagination
- Destination management list view
- Create destination
- Edit destination
- Archive destination
- Restore destination
- Delete destination

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Admin:

```text
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/admin/destinations
http://127.0.0.1:8000/admin/destinations/create
```
