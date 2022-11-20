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

Start the image in detached mode:

```bash
docker run -td --name hackers_utopia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v "$(PWD)":/APP -p 8834:8834 berryliumsec/hackers_utopia
```

Run nmap commands:

```bash
docker exec hackers_utopia nmap 10.0.0.0/24
```

```bash
docker exec hackers_utopia burpsuite
```
To start nessus:

```bash
docker exec hackers_utopia /etc/init.d/nessusd start
```
