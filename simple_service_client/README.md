# Simple Service Client

This is a command-line client that communicates with a REST API service (`simple_service`) and saves the response either locally or remotely over SSH.

## Contents

- `client.py` – Main CLI script
- `Dockerfile` – Containerization setup for the client
- `requirements.txt` – Python dependencies

---

## Requirements

- A running `simple_service` API server (listening on port `8000`)
- SSH access to a remote machine

---

## Local Installation

```bash
pip install -r requirements.txt
```

---

## CLI Options

- `--mode`  
  **Required.** Operation mode.  
  Choices: `hello` (save API response locally) or `random` (save remotely via SSH).

- `--remote-host`  
  Hostname or IP address for the API server.  
  Default: `ubuntu-vm-22-04`.

- `--filename`  
  Output file name.  
  Default: `filename.txt`.

- `--remote-user`  
  SSH username used for remote connection.  
  Default: `vagrant`.

- `--key-filepath`  
  Path to the private SSH key used for authentication.  
  Default: `/root/.ssh/id_rsa`.

---

## Examples
1. Save /hello response locally

```bash
python client.py --mode hello --filename response.txt
```
2. Save /random response remotely via SSH

```bash
python client.py --mode random --remote-user vagrant --remote-host 192.168.56.10 --filename data.txt
```
---