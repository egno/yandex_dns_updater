#!/usr/bin/python3.6

import requests
import getopt
import sys

from pdd import Pdd

def main(**params):

    pdd = Pdd(**params)
    return(pdd.saveARecord())


def usage():
    print(sys.argv[0])
    print('''Usage:
{0} -t TOKEN -d DOMAIN -i IP
'''.format(sys.argv[0],))


if __name__ == "__main__":
    token = None
    domain = None
    ip = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:d:i:", [
                                   "token=", "domain=", "ip="])
    except (getopt.GetoptError) as e:
        print(e)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-t", "--token"):
            token = arg
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-i", "--ip"):
            ip = arg

    print(main(token=token, domain=domain, ip=ip))
