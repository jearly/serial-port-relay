Serial Port Relay Controller
===============================

Description:

This daemon was originally wriiten to serve a single purpose. You will have to modify the start() function to test against your own parameters and trigger the setDTR functionality.
# Installation

1.) Get Dependencies

Note: if you do not have pip already installed run the following:

CentOS/RedHat:
    
    sudo yum install python-setuptools 
    sudo easy_install pip
    
Debian/Ubuntu:
    
    sudo apt-get install python-setuptools
    sudo easy_install pip

Install Dependencies:
    
    sudo pip install pyserial

2.) Clone the project onto a linux host.
    
    git clone git@github.com:jearly/serial-port-relay.git

3.) Jump into the new serial-port-relay directory and run setup.sh
    
    cd serial-port-relay
    sudo sh setup.sh

4.) Start and stop the daemon with the following command:

    /etc/init.d/relay-control start|stop

