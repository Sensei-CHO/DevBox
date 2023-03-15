# Installation

For the installation of `k0s` I mainly followed [this steps](https://docs.k0sproject.io/v1.26.2+k0s.1/raspberry-pi4/#optional-create-a-swap-file) and applied some changes.

- Set `vm.swappiness` to `60`
- modprobe `overlay` `nf_conntrack` `br_netfilter`
- Added `cgroup_memory=1 cgroup_enable=memory cgroup_enable=cpuset` to `/boot/firmware/cmdline.txt`

I'v also done what's in `k3s` [updates](../k3s/README.md#updates) sections.

## Remote management

To manage the cluster remotely you have to create a new configuration:

```bash
k0s kubeconfig create username
```

And paste the output to your `~/.kube/config` on your computer.

### Updates