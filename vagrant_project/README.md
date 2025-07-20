# FastAPI Vagrant VM Setup

This project uses Vagrant to create a virtual machine with Ubuntu 22.04 and sets up the environment to run a FastAPI application using Ansible.

---

## Requirements

- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

---

## Starting the VM

1. Navigate to the `vagrant_project/` folder:

   ```bash
   cd vagrant_project
   ```
   
2. Start the VM:

    ```bash
   vagrant up
   ```

The VM will be created with the hostname: fastapi-vm-22.04
IP Address: 192.168.56.101

---

## Adding the VM to `/etc/hosts` (on the host machine)

To access the VM via the hostname (`ubuntu-vm-22.04`) from your host system (e.g., for `ping`, Ansible, curl, etc.), add the following entry in your `/etc/hosts` file:

Open the `/etc/hosts` file:

```bash
sudo nano /etc/hosts
```
   
Add this line at the end of the file:

```text
192.168.56.101 ubuntu-vm-22.04
```
