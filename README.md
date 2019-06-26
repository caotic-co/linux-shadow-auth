
<p align="center">
    <h1 align="center">PAM Linux</h1>
    <br>
    <p align="center">Python module to validate the credentials of a Linux user using the Pluggable Authentication Modules (PAM).</p>
</p>

Requirements
------------
For this project to work you need to have installed **Python >= 3.5**.
 
Linux Dependencies 
------------
You need to have the following list of programs installed in your Linux System:
* cat
* grep
* openssl

Linux Permissions
------------
For this project to work your user needs to have access to the shadow group.
To do so you can execute the following command:

~~~
sudo usermod -a -G shadow <your_username>
~~~


Installation
------------
~~~
pip3 install pam_linux
~~~


Usage
------------
Once installed you can import the module in your programs

```python
import pam_linux
``` 
