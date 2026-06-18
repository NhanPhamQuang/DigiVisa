# Visa Service UI - FastAPI

## Run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000

## Pages

- `/` Home page
- `/visa-services` Visa services page
- `/travel-resources` Travel resources page
- `/countries` View all visa countries with search
- `/profile` Profile placeholder
