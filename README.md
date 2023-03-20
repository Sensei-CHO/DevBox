# DevBox

DevBox is a test server hosted on a [RPI 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/).

This repository is follows the updates and new deployments on this DevBox.

# Configuration

As said before, `DevBox` is hosted on a [RPI 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) running [Ubuntu Server 22.04](https://ubuntu.com/download/server) as its OS.

The `RPI 3B+` specs are:
- 1024 MB Ram
- Quad Cores 1.4GHz 64-bit
- 32 GiB SD card

## Apps

The [Apps](Apps/) folder contains the apps I created and tested on the `DevBox`.
These will probably have their own dedicated repository in the future.

- [DDNS Updater](Apps/DDNS_Updater/README.md) Simple DNS record updater for cloudflare.
- [Website](Apps/website/README.md) Created a simple `vuejs` web page for `DevBox`

## Deployments

The [Deployments](Deployments/) folder contains the things I deployed on my raspberry and its platforms likes `k3s` or `lxd`.

[Kubernetes](Deployments/kubernetes/)
- [K3S](Deployments/kubernetes/k3s/README.md) Installation of `k3s`.
- [Auto DNS and SSL](Deployments/kubernetes/auto-dns-ssl/README.md) Setup of Automatic DNS and SSL.
- [Portainer](Deployments/kubernetes/portainer/README.md) Deployments of `portainer` on our `kubernetes` node to deploy apps more easily.
- [K0S](Deployments/kubernetes/k0s/README.md) Installation of `k0s`.

[Host](Deployments/host/)
- [Fail2Ban](Deployments/host/fail2ban/README.md) Installation of `fail2ban` to secure our server.
- [Secure SSH](Deployments/host/secure_ssh/README.md) Making `SSH` more secure for remote access.
- [Netdata](Deployments/host/netdata/README.md) Monitoring with `netdata`

## Contribute

Comming soon

### License

This repository and all its contents are under `Creative Commons Attribution Share Alike 4.0 International` license.

#### Updates

- Reinstalled the `DevBox` OS (Still ubuntu server 22.04)
- Switched from `k3s` to `k0s` for ressources issues
- Installed `netdata`
- Deployed `ingress`
- Scaled down to 0 `metrics-server` to lower CPU load