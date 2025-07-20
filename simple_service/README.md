# Simple FastAPI Server

This project is a simple REST API server built with **FastAPI**.

## Features

- `GET /hello` – Returns a static "hello" string.
- `GET /random` – Returns a random string (from a predefined list).

---

## Requirements

All dependencies are listed in `requirements.txt`.

---

## Running the Application

> Make sure Python 3.10 is installed on your system.

1. Create and activate a virtual environment:

```bash
python3.10 -m venv simple_service_venv
source simple_service_venv/bin/activate
```

---

2. Install dependencies:

```bash
pip install -r simple_service/requirements.txt
```

3. Run the server:

```bash
uvicorn simple_service.app.main:app --host 0.0.0.0 --port 8000
```
