# Hackers Utopia

The purpose of the project is to:

TO DO
  
## Supported Open Source Applications

- OWASP Zap
- NMAP
- Nessus
  
## Getting Started

### Dependencies

- Docker

### Usage

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
docker run -itd --name hackers_utopia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v "$PWD":/APP -p 8834:8834 berryliumsec/hackers_utopia 
```

Run nmap commands:

```bash
docker exec YOUR_PREFERRED_CONTAINER_NAME nmap YOUR-NNMAP-COMMAND
```

To start nessus:

```bash
docker exec YOUR_PREFERRED_CONTAINER_NAME /etc/init.d/nessusd start
```

Start Burpsuite Pro

```bash
/usr/local/bin/BurpSuitePro
```

Start Burpsuite Community

```bash
/usr/local/bin/BurpSuiteCommunity
```