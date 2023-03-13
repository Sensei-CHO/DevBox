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

## Deployments

The [Deployments](Deployments/) folder contains the things I deployed on my raspberry and its platforms likes `k3s` or `lxd`.

[K3S](Deployments/k3s/)
- [K3S](Deployments/k3s/installation/README.md) Installation of `k3s`.
- [Ingress and SSL](Deployments/k3s/) Setup of Ingress controller and SSL certificates for our applications (comming soon).
- [Portainer](Deployments/k3s/) Deployments of `portainer` on our `k3s` node to deploy apps more easily (comming soon).

[Host](Deployments/host/)
- [Fail2Ban](Deployments/host/fail2ban/README.md) Installation of `fail2ban` to secure our server (comming soon).
- [Secure SSH](Deployments/host) Making `SSH` more secure for remote access (comming soon).

## Contribute

Comming soon

### License

This repository and all its contents are under `Creative Commons Attribution Share Alike 4.0 International` license.