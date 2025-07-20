# Simple Service Deployment with Ansible

This project provides an automated way to deploy the `simple_service` FastAPI application to a Linux-based virtual machine (e.g., Ubuntu 22.04) using **Ansible**.

---

# Ansible Details

## Inventory (inventory.ini)

Defines the target VM and SSH access details.

## Playbook (ansible/playbook.yml)

Uses the simple_service role to handle deployment steps.

## Role: simple_service (ansible/roles/simple_service/tasks/main.yml)
This role performs the following:

1. Copies the simple_service source code to the VM.

2. Installs python3.10-venv via apt.

3. Creates a virtual environment.

4. Installs Python packages from requirements.txt using pip.

5. Starts the app with uvicorn in the background.

---

# Notes

- The app is started with uvicorn and listens on port 8000.

- The process is started with nohup to run in the background.

- Deployment is intended for development/testing VMs, not production use.