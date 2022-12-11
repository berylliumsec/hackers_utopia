
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

### Enable displays

Go to XQuartz preferences -> Security
Enable "Allow connections from network clients"
Restart XQuartz

To confirm that the display server is now running on port 6000 run:

```bash
netstat -an | grep -F 6000
```

Run the following command to allow local X11 connections:

```bash
xhost +localhost
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

