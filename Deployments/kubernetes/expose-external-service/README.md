# Exposing external services

As we deployed `Kcert` and `nginx-ingress` in [this](../auto-dns-ssl/README.md) document, we can now expose service that are external to our `k0s` node.

## Exposing

The only thing you need is to edit the [external-service.yaml](./external-service.yaml) with your service's `ip` and `port`.

```bash
kubectl apply -f external-service.yaml
```