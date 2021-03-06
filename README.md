# remote-ssh-tunnel-controller-qt

![Run tests](https://github.com/guallo/remote-ssh-tunnel-controller-qt/workflows/Run%20tests/badge.svg)
![Upload release assets](https://github.com/guallo/remote-ssh-tunnel-controller-qt/workflows/Upload%20release%20assets/badge.svg)

Download an [AppImage](https://github.com/guallo/remote-ssh-tunnel-controller-qt/releases/) (for linux only), give execution permission and run it:

```shell
# replace version (<X.Y.Z>) and architecture (<ARCH>) accordingly
$ wget https://github.com/guallo/remote-ssh-tunnel-controller-qt/releases/download/v<X.Y.Z>/remote-ssh-tunnel-controller-qt-<X.Y.Z>-<ARCH>.AppImage

$ chmod +x remote-ssh-tunnel-controller-qt-*.AppImage

$ ./remote-ssh-tunnel-controller-qt-*.AppImage
```

Or `pip install` (for any plattform that support `pip`) and run it:

```shell
$ pip install remote-ssh-tunnel-controller-qt

$ rssht-controller-qt
```

Generate the public/private rsa key pair the *controller* will use to connect to the *intermediate SSH server*, replace `<YOUR-NICKNAME-WITHOUT-SPACE-CHARACTERS>` accordingly:

```shell
$ ssh-keygen -C <YOUR-NICKNAME-WITHOUT-SPACE-CHARACTERS> -N "" -f id_rsa
```

Copy the public key to the *intermediate SSH server*, replace `<SSH-USER>`, `<SSH-SERVER>` and `<SSH-PORT>` accordingly (see [the configuration of the intermediate SSH server](https://github.com/guallo/remote-ssh-tunnel-agent/blob/master/README.md#manual-1)):

```shell
$ ssh-copy-id -i id_rsa.pub <SSH-USER>@<SSH-SERVER> -p <SSH-PORT>
```

## Development

### Generate rssht_controller_qt/resources.py file

```shell
$ pyside2-rcc -o rssht_controller_qt/resources.py resources.qrc
```
