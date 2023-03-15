# Deployments

Here is the folder of all the deployments applied to the `Devbox`.

Here a deployment is the installation and setup, automatically or not, of an application.

[K3S](k3s/)
- [K3S](k3s/installation/README.md) Installation of `k3s`.
- [Ingress and SSL](k3s/) Setup of Ingress controller and SSL certificates for our applications (comming soon).
- [Portainer](k3s/portainer/README.md) Deployments of `portainer` on our `k3s` node to deploy apps more easily.

[Host](host/)
- [Fail2Ban](host/fail2ban/README.md) Installation of `fail2ban` to secure our server.
- [Secure SSH](host/secure_ssh/README.md) Making `SSH` more secure for remote access.