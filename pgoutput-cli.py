#!/usr/bin/env python

import os
import sys
import getopt
import pypgoutput

def print_help():
    print("Usage: pgoutput-cli --host=<host> --port=<port> --database=<database> --user=<user> --password=<password> --publication<publication> --slot=<slot>", file=sys.stderr)

def main(argv):
    host = ''
    port = 0
    database = ''
    user = ''
    password = ''
    publication = ''
    slot = ''

    try:
        opts, args = getopt.getopt(argv,"h",["help","host=","port=","database=","user=","password=","publication=","slot="])
    except getopt.GetoptError:
        print_help()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", '--help'):
            print_help()
            sys.exit(0)
        elif opt in ("--host"):
            host = arg
        elif opt in ("--port"):
            port = arg
        elif opt in ("--database"):
            database = arg
        elif opt in ("--user"):
            user = arg
        elif opt in ("--password"):
            password = arg
        elif opt in ("--publication"):
            publication = arg
        elif opt in ("--slot"):
            slot = arg

    if (host == '' or port == 0):
        print_help()
        sys.exit(1)

    cdc_reader = pypgoutput.LogicalReplicationReader(
                    publication_name=publication,
                    slot_name=slot,
                    host=host,
                    database=database,
                    port=port,
                    user=user,
                    password=password,
                )
    for message in cdc_reader:
        print(message.model_dump_json(indent=2))

    cdc_reader.stop()

if __name__ == "__main__":
   main(sys.argv[1:])
