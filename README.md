# yandex_dns_updater

A script that updates your dynamic IP address in the Yandex DNS service

## Chron row example

    4,9,14,19,24,29,34,39,44,49,54,59 * * * * sleep 13 ; cd /opt/service/scripts/yandex_pdd && /usr/bin/python3 update.py -d mydomain.com -t MY_YANDEX_TOKEN >> /tmp/yandex_pdd_my_domain.log 2>/dev/null
