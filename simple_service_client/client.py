import os

import click
import requests
import paramiko


def save_local(response_text, output_file):
    with open(output_file, 'w') as f:
        f.write(response_text)
    print(f'Saved to {output_file}')


def save_remote(content, host, username, remote_path, key_filepath):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,
                username=username,
                key_filename=key_filepath)

    sftp = ssh.open_sftp()
    with sftp.open(remote_path, 'w') as f:
        f.write(content)
    sftp.close()
    ssh.close()
    print(f'Saved to remote: {remote_path}')


@click.command()
@click.option('--mode',
              type=click.Choice(['hello', 'random'], case_sensitive=False),
              required=True,
              help='Choose the mode of operation.')
@click.option('--remote-host',
              default='ubuntu-vm-22-04',
              help='Host for SSH connection to save content remotely.')
@click.option('--filename',
              default='filename.txt',
              help='Output filename.')
@click.option('--remote-user',
              default='vagrant',
              help='Username for SSH connection.')
@click.option('--key-filepath',
              default='/root/.ssh/id_rsa',
              help='Path to the private SSH key.')
def main(mode, filename, remote_host, remote_user, key_filepath):
    if mode == 'hello':
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)

        r = requests.get(f'http://{remote_host}:8000/hello')
        save_local(r.text, output_path)

    elif mode == 'random':
        r = requests.get(f'http://{remote_host}:8000/random')
        if remote_host and remote_user and key_filepath:
            save_remote(r.text,
                        remote_host,
                        remote_user,
                        f'/home/{remote_user}/{filename}',
                        key_filepath)
        else:
            print('Missing remote SSH credentials.')


if __name__ == '__main__':
    main()
