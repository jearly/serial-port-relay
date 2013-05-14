#!/bin/bash
# 
# Quick setup script to put serial-port-controller in place and ready to run.
#
# Once installed, you can run the relay controller daemonized with 
# the following command:
#    /etc/init.d/relay-control start|stop
#
mkdir -p /relay-control
cp -fr ./relay-control/* /relay-control/
cp -fr ./init.d/relay-control /etc/init.d/

chmod +x /etc/init.d/relay-control
chmod +x -R /relay-control/*