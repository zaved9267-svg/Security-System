# Security Event System

A Django REST project for tracking security events and alerts. This README covers setup, development, running (local and Docker), tests, and common maintenance tasks.

## Requirements
- Python 3.10+ (recommended)
- pip
- Optional: Docker & Docker Compose (for containerized runs)

## Quick setup (local, virtualenv)
1. Create and activate a virtual environment
   ```powershell
   python -m venv .venv
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   # Windows cmd
   .venv\Scripts\activate.bat
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations and create a superuser
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run the development server
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/` by default.

## Docker (recommended for production-like environment)
Build and run with Docker Compose:
```bash
docker-compose up --build
```
This uses the repository's `docker-compose.yml` and Dockerfiles present under `docker/`. Adjust environment variables in the compose file or `.env` as needed.

## Database
- Default: SQLite (`db.sqlite3`) for local development.
- If switching to Postgres, update `security_monitoring/settings.py` or set environment variables as required and ensure the Postgres service in Docker (see `docker/postgres/init.sql`).

## Running tests
Run Django's test suite:
```bash
python manage.py test
```

## Important files & structure
- `manage.py` — Django CLI
- `security_monitoring/settings.py` — project settings
- `events/` — events app (models, serializers, views, permissions)
- `alerts/` — alerts app
- `accounts/` — user/account management
- `docker/` — Dockerfiles and DB init SQL

## API overview
- Endpoints are defined in each app's `urls.py`. Example (adjust path prefixes if your project uses a base `/api/`):
  - Create event (admin only): `POST /events/` — see `events/views.py` and `events/permissions.py`
  - Alerts and other resources: check `alerts/urls.py` and `events/urls.py`
- Example curl to create an event (replace host, path, credentials and payload):
  ```bash
  curl -X POST http://127.0.0.1:8000/events/ \
    -H "Content-Type: application/json" \
    -u admin:password \
    -d '{"name":"Example event","event_type":"intrusion","timestamp":"2025-12-25T12:00:00Z"}'
  ```

## Development notes
- Permissions: some endpoints require specific permissions (see `events/permissions.py` and `alerts/permissions.py`).
- Serializers: request/response shapes are defined in each app's `serializers.py`.
- When adding models, create migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- Recommended: use pre-commit hooks / linters (black, flake8) for style consistency.

## Debugging & common commands
- Run shell: `python manage.py shell`
- Show migrations status: `python manage.py showmigrations`
- List URLs: `python manage.py show_urls` (requires `django-extensions`) or inspect `urls.py` files directly.

## Contributing
- Fork, create a feature branch, add tests for new behavior, open a PR describing changes.
- Keep changes focused, run tests locally before submitting.

## Contact / Maintainer
- For issues or feature requests, open an issue in the repository or contact the maintainer listed in project metadata.
