#!/bin/bash
export PATH=$PATH:/APP
if [ "$1" = "zap_vuln_scan" ]; then
    printf "passing args to zap: %s %s %s %s" "$2" "$3" "$4" "$5"
    owasp-zap -cmd -quickurl "$2" -quickout /RESULTS/zap_raw_results.json -silent -quickprogress
elif [ "$1" = "nmap_vuln_scan" ]; then
    printf "passing args to nmap: %s %s %s %s" "$2" "$3" "$4" "$5"
    nmap -oX /RESULTS/nmap_raw_results.xml -sV --script nmap-vulners/ "$2"
else
    printf "unrecognized command"
fi
