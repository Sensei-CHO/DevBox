# Auto DNS and SSL

Here we are going to configure automatic domain name attribution for our deployments and automatic SSL for security.

Steps:
- Install `metallb`
- Install `nginx-ingress`
- Install `external-dns`

## Metallb

Metallb is a kubernetes load balancer that attributes LAN IP to our services.

Steps to install are pretty simple:

Namespace manifest:

```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.10.2/manifests/namespace.yaml
```

Metallb manifest:

```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.10.2/manifests/metallb.yaml
```

IP Pool manifest (don't forget to configure it):

```bash
kubectl apply -f metallb-configmap.yaml
```

Now that `metallb` is setup we can test it!

```bash
kubectl apply -f httpd-test-metallb.yaml
```

Get the service external IP attributed by `metallb`:

```bash
kubectl get service -n web


NAMESPACE     NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                  AGE
web           web-server-service   LoadBalancer   10.98.176.182   192.168.1.200   80:30314/TCP             63s
```

And test!

```bash
curl 192.168.1.200

<html><body><h1>It works!</h1></body></html>
```

## Nginx ingress

The Ingress is a Kubernetes resource that lets you configure an HTTP load balancer for applications running on Kubernetes.

Installation:

```bash
https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.3/deploy/static/provider/baremetal/deploy.yaml
```

Add the annotatoin to specify that this is the only instance of Ingress Nginx:

```bash
kubectl -n ingress-nginx annotate ingressclasses nginx ingressclass.kubernetes.io/is-default-class="true"
```

Edit the service to switch from NodePort(by default in the manifest) to LoadBalancer:

```bash
KUBE_EDITOR="nano" kubectl edit service ingress-nginx-controller -n ingress-nginx
```

```yml
spec:
  allocateLoadBalancerNodePorts: true
  clusterIP: 10.97.71.207
  clusterIPs:
  - 10.97.71.207
  externalTrafficPolicy: Cluster
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - appProtocol: http
    name: http
    nodePort: 32762
    port: 80
    protocol: TCP
    targetPort: http
  - appProtocol: https
    name: https
    nodePort: 31191
    port: 443
    protocol: TCP
    targetPort: https
  selector:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
  sessionAffinity: None
  type: NodePort ###Change to LoadBalancer###
```

Check the IP attributed by `metallb`:

```
kubectl get services -n ingress-nginx

NAMESPACE       NAME                                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
ingress-nginx   ingress-nginx-controller             LoadBalancer   10.97.71.207    192.168.1.200   80:32762/TCP,443:31191/TCP   4m12s
```

And test:

```bash
curl 192.168.1.200

<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

Even if the reply is a 404 the `ingress-controller` is working

## External-DNS

