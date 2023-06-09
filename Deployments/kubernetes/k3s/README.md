# Installation

Installing `k3s` is as easy as pie ! All you need installed is the `curl` package.

```bash
apt install curl
curl -sfL https://get.k3s.io | sh -
```

After the installation is done, we need to check that everything is up and running:

Checking openned ports

```bash
lsof -i | grep LISTEN

systemd       1            root  115u  IPv6  15263      0t0  TCP *:ssh (LISTEN)
systemd-r 54280 systemd-resolve   14u  IPv4 111797      0t0  TCP localhost:domain (LISTEN)
systemd-r 54280 systemd-resolve   16u  IPv4 111799      0t0  TCP localhost:domain (LISTEN)
sshd      54285            root    3u  IPv6  15263      0t0  TCP *:ssh (LISTEN)
k3s-serve 56641            root   15u  IPv6 128136      0t0  TCP *:6443 (LISTEN)
k3s-serve 56641            root   16u  IPv4 129059      0t0  TCP localhost:sge-qmaster (LISTEN)
container 56682            root   16u  IPv4 125891      0t0  TCP localhost:10010 (LISTEN)
```

Here we can see that `k3s` has successfully openned port `6443` which is the kubernetes api server.

Now we have to check that all the nodes (only 1 here) are running

```bash
k3s kubectl get node

NAME     STATUS     ROLES                  AGE   VERSION
devbox   NotReady   control-plane,master   11m   v1.25.6+k3s1
```

## Remote management

Now that our `k3s` node is up and running, we can setup remote management.

Frist of all we have to install `kubectl` on our computer:

Ubuntu

```bash
snap install kubectl --classic
```

For Other linux distributions follow: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

Now we can export the `kubeconfig` from our `k3s` server:

```bash
cat /etc/rancher/k3s/k3s.yaml
```

:warning: In some cases you'll have to edit the `server:` value to your `k3s` server's LAN IP :warning:.

To get your `k3s` server's LAN IP:

```bash
ip -c --brief a
```

Transfer the content of this file to `~/.kube/config` on your computer.

We can now run `kubectl` on our computer and manage our remote `k3s` node.

## Recommendations

I strongly recommend new users to install `kubernetes-dashbord` and `weave-scope` to to have a better overview of your cluster.

- Kubernetes-dashabord: https://docs.k3s.io/installation/kube-dashboard
- Weave Scope: https://www.weave.works/docs/scope/latest/installing/#k8s

### Updates

> Update from 14 March 2023

`DevBox` runs on a raspberry 3B+ so you'll have to add `cgroup_memory=1 cgroup_enable=memory` to `/boot/firmware/cmdline.txt` and disable `ufw` if you are using `ubuntu` 
like I do.

> Update from 15 March 2023

I encountered a LOT of issues with `k3s`:
- High CPU Load `17.82 15.20 8.06`
- 800 / ~1024MB RAM Used
- Reinstallation issues (Pods not running, Services Unavailable, Server refuses connections)

What I did:
- Disable all `snap` services (`snapd.service`, `snapd.socket`, `snapd.seeded.service`)
- Installed `runc`
- Installed `linux-modules-extra-raspi`

And things are getting better but i'll try to make it more efficient.

> Update from 15 March 2023 10:12

After all this issues I decide to rollback on `k3s` and install `k0s`.

:warning: This installation works and have been tested this rollbak is not necessary :warning: