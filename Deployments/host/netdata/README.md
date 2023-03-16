# Installation

Installing `netdata` is really simple.

```bash
wget -O /tmp/netdata-kickstart.sh https://my-netdata.io/kickstart.sh && sh /tmp/netdata-kickstart.sh
```

Yay! we can now monitor the `DevBox` !

## Configuration

To lower resources usage from netdata you need to adapt your `/etc/netdata/netdata.conf`.

In my case I just added:

```
update every = 7
```

Now `netdata` only updates metrics each 7secs which reduces CPU and Memory load.