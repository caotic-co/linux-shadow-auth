
<p align="center">
    <h1 align="center">Linux Shadow Authentication</h1>
    <br>
    <p align="center">Python module to validate the credentials of a Linux user using the /etc/shadow file.</p>
</p>

Requirements
------------
For this project you need to have **Python >= 3.5** and the following list of programs installed in your Linux System:
* cat
* grep
* openssl
* passwd

Usually these programs come preinstalled in various linux distributions, but in case you need to install them you can use the following commands:

#### For CentOS, RHEL, Fedora
~~~
sudo yum install coreutils grep openssl passwd
~~~
#### For Debian, Ubuntu, Linux Mint
~~~
sudo apt install coreutils grep openssl passwd
~~~
Linux Permissions
------------
For this module to work your user requires access to the shadow group.
To do so you can execute the following command:

~~~
sudo usermod -a -G shadow <username>
~~~

If you are logged as the user that is going to be added to the group you might have to log out and log in again,
or reboot, in order for the changes to have effect.


Installation
------------
~~~
pip3 install linux-shadow-auth
~~~


Usage
------------
Once installed you can import the module in your programs

```python
import shadow_auth
``` 
