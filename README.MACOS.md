
# Hackers Utopia

A collection of hacking tools in a docker image.
  
## Supported Applications

- OWASP Zap
- NMAP
- Nessus
- Burpsuite Community
- Burpsuite Professional
- Cobalt Strike
  
## Getting Started

### Dependencies

- Docker
- Display Server (Xquartz)

### Usage (Docker)

Build the image

```bash
docker-compose build
```

Get the display id of the running display

Linux:

```bash
w -oush
```

The output will be similar to the below where `:1` is the id of the display:

```bash
$YOUR_HOSTNAME     :1       :1               ?xdm?  /usr/lib/gdm3/gdm-x-session --run-script env GNOME_SHELL_SESSION_MODE=ubuntu gnome-session --session=ubuntu
```

Set the display env as follows in:

```bash
export DISPLAY=:1
```

Allow docker use localhost display:

```bash
xhost +local:docker 
```

Start the image in detached mode:

```bash
docker run -it --rm --name hackers_utopia -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix -v "$PWD":/APP -p 8834:8834 berryliumsec/hackers_utopia /usr/local/bin/BurpSuiteCommunity 
```




Access the container's CLI

```bash
docker exec -it hackers_utopia /bin/bash
```

Run nmap commands:

```bash
docker exec hackers_utopia nmap YOUR-NNMAP-COMMAND
```

To start nessus:

```bash
docker exec hackers_utopia /etc/init.d/nessusd start
```

Start Burpsuite Pro

Note that to use the in-built browser for manual testing, you have to
allow it to run outside of the sandbox-b


Project Options -> Misc -> Allow Browser to run without a sandbox

```bash
docker exec hackers_utopia /usr/local/bin/BurpSuitePro
```

Start Burpsuite Community

```bash
docker exec hackers_utopia /usr/local/bin/BurpSuiteCommunity
```

Stop the container

```bash
docker stop hackers_utopia 
```

Remove the container

```bash
docker rm hackers_utopia
```

### Usage (discover_aws_services)

```bash
python3 discover_aws_services.py --Region="your_region" --Serial_number="arn:aws:iam::123456789012:mfa/user" --Token="your_mfa_token"
```
## TODO

- bloodhound

From the XQuartz preferences, in the security tab, make sure Allow connections from network clients is enabled. Restart XQuartz.
NB: After restarting XQuartz, you can run netstat -an | grep -F 6000 to find that XQuartz has opened port 6000. This is actually how your docker container will be communicating with XQuartz on the host. The volume mount is not (and cannot due to an ongoing issue -- more details in the original link) be used.

In a terminal on the host, run xhost +localhost.
NB: This will allow network X11 connections from localhost only, which is fine. Also if XQuartz is not running, xhost will start it.

Pass -e DISPLAY=host.docker.internal:0 to any docker image you want to forward X to the host.