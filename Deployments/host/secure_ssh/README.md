# Secure SSH

This document is in fact more of a configuration than a deployment.

Here we're goingo to see how to secure a `ssh` server by configuring access.
You can also have a look to [Fail2ban](../fail2ban/README.md) deployment and configuration.

## Configuration

By default a `ssh` server is using user / pass authentication which is easily hackable using brute force attacks.

We'll see how to configure ssh to use keys instead of default user / pass login.

First, we're going to create new keys using `ssh-keygen` on our computer.

```bash
ssh-keygen

Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): /home/user/.ssh/id_rsa_devbox
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa_devbox
Your public key has been saved in /home/user/.ssh/id_rsa_devbox.pub
```

We can now export our public key (id_rsa_devbox.pub) to the desired user on our machine.


On our computer:

```bash
cat /home/user/.ssh/id_rsa_devbox.pub

<output>
```

On our machine:

```bash
echo <content> >> /home/user/.ssh/authorized_keys #change user to the user you want 
```

We can now try to connect:

```bash
ssh -i ~/.ssh/id_rsa_devbox user@devbox.local
```

I recommand adding this to your `~/.ssh/config` to connect more easily using `ssh DevBox`:

```
Host DevBox
    HostName devbox.local
    User user
    Port 22
    IdentityFile ~/.ssh/id_rsa_devbox
```

Now that ou keys ar set, we can update our `ssh` server config file:

```
#/etc/ssh/sshd_config
PasswordAuthentication no
```

P.S. Sometimes the `PasswordAuthentication` rule is set in other files located at `/etc/ssh/sshd_config.d/`

Restart the service to apply configuration changes:

```bash
service ssh restart
```

And that's it! our `ssh` server is now accessible and secure !