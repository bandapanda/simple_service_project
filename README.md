# Project Deployment Overview

This project contains automation for deploying the `simple_service` FastAPI application and the `simple_service_client` Docker client. The deployment process includes setting up the necessary services, running playbooks with Ansible, and managing the build and deployment of Docker images.

## Deployment Instruction

### Step 1: Set Up Your Virtual Machine

This project assumes that you're using Vagrant to create and manage a local virtual machine (VM), typically running Ubuntu 22.04.

To start the VM, navigate to the `vagrant_project/` directory and run:

```bash
cd vagrant_project
vagrant up
```

This will initialize and boot up the VM defined in the Vagrantfile.

> For more details on the VM configuration and troubleshooting tips, refer to the [Vagrant Project README](vagrant_project/README.md).

### Step 2: Set Up Your Environment

To deploy the `simple_service` application, you need to have Ansible installed. You can use a standard **Python virtual environment (venv)**.

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r ansible/requirements.txt
```

Once the environment is set up and Ansible is installed, you can proceed to deploy the application using the deploy.sh script.


### Step 2: Run the deploy.sh Script
Execute the deploy.sh script from the root directory to deploy the application. This script will trigger the Ansible playbook to set up the environment and deploy the application on the remote VM.

```bash
./deploy.sh
```
This script runs the following command:
```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

### Step 3: Ansible Playbook Details
The ansible-playbook command uses the ansible/inventory.ini file to define the target system and the ansible/playbook.yml to describe the steps needed to deploy the application.

> For more detailed information about the Ansible setup and deployment steps, refer to the [Ansible README](ansible/README.md).

## Docker Build and Run Process

### Step 1: Build the Docker Image
Use the provided Makefile to build the Docker image for simple_service_client. This image is used for interacting with the deployed services.

To build the Docker image, run the following command:

```bash
make build
```
This will build the Docker image with the tag simple_service_client:1.0.0 by default.

### Step 2: Run the Docker Client
You can run the Docker client in two modes using the Makefile:

#### 1. Hello Mode
This mode is used for a simple test to ensure the client is working.

```bash
make run-hello
```
This command runs the client in "hello" mode.

#### 2. Random Mode
In this mode, the client interacts with the remote VM and runs operations in "random" mode.

```bash
make run-random
```
This command runs the client in "random" mode, passing the remote-user vagrant option to specify the user for the connection.

For more details on how the Docker client is configured and how it interacts with the services, refer to the simple_service_client README.

## Additional Documentation
For further explanations and in-depth details, you can refer to the following README files:

- [Simple Service README](simple_service/README.md): Information about the simple_service FastAPI application.

- [Simple Service Client README](simple_service_client/README.md): Information about the simple_service_client Docker client, including how to build and run it.
