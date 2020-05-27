#!/usr/bin/python3

import argparse
import os


def main(args):
    if args.type == 'Host':
        message = 'Notification Type: {} \
                \
                Customer: {} \
                Host: {} \
                Address: {} \
                State: {} \
                
                Date/Time: {}'.format(args.notificationtype, args.customer, args.display-name, args.hostname, args.state, args.date )
        
        signal_send(message)
    else:
        message = 'Notification Type: {} \
                \
                Customer: {} \
                Host: {} \
                Address: {} \
                Service: {} \
                State: {} \
                
                Date/Time: {}\

                Additional Info: {}'.format(args.notificationtype, args.customer, args.display-name, args.hostname, args.service, args.state, args.date, agrs.service-output )
            
        signal_send(message)





def signal_send(string):
    
    os.system('/usr/bin/printf "%b" "{}" | signal-cli -u {} send {}'.format(string, args.icinga-number, args.target-number))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Notification command for Signalcli')

    parser.add_argument('-t', '--type', help='Check type: Host or Serice ', default='Host')
    parser.add_argument('-nt', '--notificationtype', help='Notification type', required=True)
    parser.add_argument('-H', '--hostname', help='Hostname as in Icinga2', required=True)
    parser.add_argument('-D', '--display-name', help='Display name as in Icinga2', required=True)
    parser.add_argument('-S', '--service-name', help='Serivce name as in Icinga2', required=True)
    parser.add_argument('-s', '--host-state', help='Host state as "WARNING", "CRITICAL" or "UNKNOWN"', required=True)
    parser.add_argument('-d', '--date', help='As icinga.long_date_time in Icinga2', required=True )
    parser.add_argument('-inum', '--icinga-number', help='Signal user for Icinga2', required=True)
    parser.add_argument('-tnum', '--target-number', help='Target User to send notification to', required=True)
    parser.add_argument('-C', '--customer', help='Customer ID from Icinga2', required=True)
    parser.add_argument('-o', '--service-output', help='Service output from Icinga2')

    
    main(parser.parse_args())
