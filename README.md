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

### Usage

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
docker exect -it hackers_utopia /bin/bash
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

```bash
docker exec hackers_utopia /usr/local/bin/BurpSuitePro
```

Start Burpsuite Community

```bash
docker exec hackers_utopia /usr/local/bin/BurpSuiteCommunity
```


## TODO

- bloodhound