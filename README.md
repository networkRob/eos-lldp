##Get LLDP Neighbors

This script will update the interface descriptions on a switch based off of the received LLDP information.

###Setup
This script can be ran from a remote device or on the switch itself.  The following libraries are needed for Python to run this script:
- jsonrpclib
- argparse

#####Script setup
To use this script basic user credentials will need to be modified/provided within the file. Modify the getNeighbors.py file.

    #credentials to login to device
    eUser = 'arista'
    ePwd = 'arista'

#####Target Device Setup
For this script to successfully execute on the targeted switch, we will need to make sure eapi access is enabled.  Within EOS, enter the following commands:

    # config
    (config)# management api http-commands
    (config)# no shut
    (config)# end

###Execution
When calling the script, specify the target device to run this script on:

    $ ./getNeighbors.py --host 10.0.0.1

If a target host is not specified, it will run against the local machine's 127.0.0.1 loopback ip.