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

### Usage (Docker)

Build the image

```bash
docker-compose build
```

Get the display id of the running display

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
docker run -itd --restart unless-stopped --name hackers_utopia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v "$PWD":/APP -p 8834:8834 berryliumsec/hackers_utopia 
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

### Usage (set_aws_envs)

```bash
python3 set_aws_envs.py --Region="your_region" --Serial_number="your_serial_number" --Token="your_mfa_token"
``
## TODO

- bloodhound