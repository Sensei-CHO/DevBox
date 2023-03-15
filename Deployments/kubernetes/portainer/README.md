# Portainer

[Portainer](https://www.portainer.io/) is a WebUI for [Docker](https://docker.com/) and [Kubernetes](https://kubernetes.io/). It is made to facilitate deployments on your infrastructure.

## Installation

Kubernets often uses `manifests` to apply changes or deploy app in your infrastructure.

To install `portainer` the only thing you have to do is run:

```bash
kubectl apply -n portainer -f https://raw.githubusercontent.com/portainer/k8s/master/deploy/manifests/portainer/portainer.yaml
```

> Update from March 15 2023

:warning: This document will change :warning:
