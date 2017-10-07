# srewu
Python based Site Reliability Engineer Working Utilities (designed to be used as a module in SaltStack)

:codeauthor Stephan Looney <slooney@stephanlooney.com>

REQUIREMENTS:
* Requests (pip install requests)

INSTALLATION:
* For use with SaltStack add this repo to your _modules directory. Default /srv/salt/_modules

USE:
* sync your salt modules after installing
* salt 'my great target' srewu.latency
* salt 'my great target' srewu.tcp_check address='servername to target' port=80

GEO LOCATION SERVICES:
* This module is designed to help determine which location a given server is located in. This is based of the external IP of the node/minion

Network Test:
* This is designed to test network speeds and latency
