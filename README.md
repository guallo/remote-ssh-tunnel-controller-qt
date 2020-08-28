# remote-ssh-tunnel-controller-qt

## Installation

### Manual

#### Windows 10

1.  Download and install [Python 3.7.5](https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe), select option "**Add Python 3.7 to PATH**".

2.  Install *Qt for Python* (*PySide2*) and *Paramiko*, execute in *Command Prompt* as **Administrator**:

    ```shell
    pip install PySide2==5.14.2.2
    pip install paramiko==2.7.1
    ```

3. Download and install [Git](https://git-scm.com/download/win).

4. Download the source code, execute in *Git Bash* (**NOT** the *Command Prompt*):

    ```bash
    cd Desktop
    git clone --recurse-submodules https://github.com/guallo/remote-ssh-tunnel-controller-qt.git
    cd remote-ssh-tunnel-controller-qt
    ```

5. Generate the public/private rsa key pair the *controller* will use to connect to the *intermediate SSH server*, replace `<YOUR-NICKNAME-WITHOUT-SPACE-CHARACTERS>` accordingly, execute in *Git Bash* (**NOT** the *Command Prompt*):

    ```bash
    ssh-keygen -C <YOUR-NICKNAME-WITHOUT-SPACE-CHARACTERS> -N "" -f id_rsa
    ```

6. Copy the public key to the *intermediate SSH server*, replace `<INTERMEDIATE-SSH-USER>`, `<INTERMEDIATE-SSH-SERVER>` and `<INTERMEDIATE-SSH-PORT>` accordingly (see [the configuration of the intermediate SSH server](https://github.com/guallo/remote-ssh-tunnel-agent/blob/master/README.md#manual-1)), execute in *Git Bash* (**NOT** the *Command Prompt*):

    ```bash
    ssh-copy-id -i id_rsa.pub <INTERMEDIATE-SSH-USER>@<INTERMEDIATE-SSH-SERVER> -p <INTERMEDIATE-SSH-PORT>
    ```

7. Execute the *controller* double clicking the `__main__.pyw` file.

8. Adjust the *controller* settings in the corresponding toolbar button.

#### Ubuntu 18.04

1.  Install *Python 3*:

    ```bash
    sudo apt-get install python3
    ```

2. Install *Qt for Python* (*PySide2*) and *Paramiko*:

    ```bash
    sudo pip install PySide2==5.14.2.2
    sudo pip install paramiko==2.7.1
    ```

3.  Install *Git*:

    ```bash
    sudo apt-get install git
    ```

4. Download the source code:

    ```bash
    cd Desktop
    git clone --recurse-submodules https://github.com/guallo/remote-ssh-tunnel-controller-qt.git
    cd remote-ssh-tunnel-controller-qt
    ```

5. Generate the public/private rsa key pair the *controller* will use to connect to the *intermediate SSH server*, replace `<YOUR-NICKNAME-WITHOUT-SPACE-CHARACTERS>` accordingly:

    ```bash
    ssh-keygen -C <YOUR-NICKNAME-WITHOUT-SPACE-CHARACTERS> -N "" -f id_rsa
    ```

6. Copy the public key to the *intermediate SSH server*, replace `<INTERMEDIATE-SSH-USER>`, `<INTERMEDIATE-SSH-SERVER>` and `<INTERMEDIATE-SSH-PORT>` accordingly (see [the configuration of the intermediate SSH server](https://github.com/guallo/remote-ssh-tunnel-agent/blob/master/README.md#manual-1)):

    ```bash
    ssh-copy-id -i id_rsa.pub <INTERMEDIATE-SSH-USER>@<INTERMEDIATE-SSH-SERVER> -p <INTERMEDIATE-SSH-PORT>
    ```

7. Execute the *controller*:

    ```bash
    python3 __main__.py
    ```

8. Adjust the *controller* settings in the corresponding toolbar button.

## Installation upgrade

### Manually

**NOTICE:** For *Windows 10* users, the below commands should be executed in *Git Bash* (**NOT** the *Command Prompt*).

```bash
cd Desktop/remote-ssh-tunnel-controller-qt
git config user.name temp
git config user.email temp
git add -A
git commit -m 'temp'
git pull --rebase
# Resolve any conflicts (if any) that could arise from previous command.
git reset HEAD~1
chmod 600 id_rsa
git config --unset user.name
git config --unset user.email

cd lib/rssht_controller_lib/
git config user.name temp
git config user.email temp
git stash push -a
cd ../../
git submodule update --checkout -- lib/rssht_controller_lib/
cd lib/rssht_controller_lib/
git stash apply
# Resolve any conflicts (if any) that could arise from previous command.
git stash drop
git config --unset user.name
git config --unset user.email
cd ../../
```

## Development

### Generate rssht_controller_qt/resources.py file

```bash
pyside2-rcc -o rssht_controller_qt/resources.py rssht_controller_qt/resources.qrc
```
