# Fail2Ban

Fail2Ban is an open-source tool to help you secure your linux server against malicious access.

## Explanation

If you take a look to `/var/log/auth.log`, you'll see that a lot of ssh connections appears.

```
Mar 13 17:58:24 DevBox sshd[171483]: Failed password for root from XX.XX.XX.XX port 23075 ssh2
Mar 13 17:58:27 DevBox sshd[171483]: Failed password for root from XX.XX.XX.XX port 23075 ssh2
Mar 13 17:58:29 DevBox sshd[171525]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=XX.XX.XX.XX  user=root
Mar 13 17:58:31 DevBox sshd[171483]: Failed password for root from XX.XX.XX.XX port 23075 ssh2
Mar 13 17:58:32 DevBox sshd[171525]: Failed password for root from XX.XX.XX.XX port 12576 ssh2
Mar 13 17:58:33 DevBox sshd[171483]: Received disconnect from XX.XX.XX.XX port 23075:11:  [preauth]
Mar 13 17:58:33 DevBox sshd[171483]: Disconnected from authenticating user root XX.XX.XX.XX port 23075 [preauth]
Mar 13 17:58:33 DevBox sshd[171483]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=XX.XX.XX.XX  user=root
Mar 13 17:58:35 DevBox sshd[171525]: Failed password for root from XX.XX.XX.XX port 12576 ssh2
Mar 13 17:58:40 DevBox sshd[171525]: Failed password for root from XX.XX.XX.XX port 12576 ssh2
Mar 13 17:58:41 DevBox sshd[171525]: Received disconnect from XX.XX.XX.XX port 12576:11:  [preauth]
Mar 13 17:58:41 DevBox sshd[171525]: Disconnected from authenticating user root XX.XX.XX.XX port 12576 [preauth]
Mar 13 17:58:41 DevBox sshd[171525]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=XX.XX.XX.XX  user=root
Mar 13 18:01:16 DevBox sshd[171759]: error: kex_exchange_identification: Connection closed by remote host
Mar 13 18:01:16 DevBox sshd[171759]: Connection closed by 185.225.74.53 port 38132
Mar 13 18:01:30 DevBox sshd[171799]: Accepted password for user from 192.168.1.254 port 56992 ssh2
Mar 13 18:01:30 DevBox sshd[171799]: pam_unix(sshd:session): session opened for user user(uid=1000) by (uid=0)
Mar 13 18:01:30 DevBox sshd[171801]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=XX.XX.XX.XX  user=root
Mar 13 18:01:31 DevBox sshd[171799]: pam_env(sshd:session): deprecated reading of user environment enabled
Mar 13 18:01:32 DevBox sshd[171803]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=XX.XX.XX.XX  user=root
Mar 13 18:01:32 DevBox sshd[171801]: Failed password for root from XX.XX.XX.XX port 37254 ssh2
Mar 13 18:01:34 DevBox sshd[171803]: Failed password for root from XX.XX.XX.XX port 56028 ssh2
Mar 13 18:01:36 DevBox sshd[171801]: Failed password for root from XX.XX.XX.XX port 37254 ssh2
Mar 13 18:01:36 DevBox sshd[171803]: Failed password for root from XX.XX.XX.XX port 56028 ssh2
Mar 13 18:01:38 DevBox sshd[171801]: Failed password for root from XX.XX.XX.XX port 37254 ssh2
```

Theses are bots or hackers trying to break into our machine. That's why we need to protect our machine using `fail2ban`.


## Installation

Run this:

```bash
apt install fail2ban
```

And nothing else!

## Configuration

`fail2ban` itslef is already configure to protect `ssh`. For more configuration options you'll have to configure `jails`. For now the `DevBox` do not need more protection from `fail2ban`.