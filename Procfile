release: python backend/task_management/manage.py migrate
web: uvicorn task_management.asgi:application --host 0.0.0.0 --port ${PORT:-5000}