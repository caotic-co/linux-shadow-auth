Clone the Repo
------------
Clone the repository using the following command:
~~~
git clone https://github.com/ospinakamilo/linux-shadow-auth
~~~

Unit Testing
------------
To run the unit tests for the source code go the 'src' folder of the cloned project "linux-shadow-auth/src/" and run
~~~
python3 -m unittest discover ./tests
~~~

Manual Install
------------
Install the Dependencies
~~~
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo python3 -m pip install tqdm
sudo python3 -m pip install --user --upgrade twine
~~~

In the location where you cloned the repository run the next command:
~~~
python3 setup.py sdist bdist_wheel
~~~
This will create a folder called 'dist' which contains the module to install.
To install the module in your local system use the following command (be sure to validate the version number in the file):
~~~
python3 -m pip install dist/shadow_auth-x.x-py3-none-any.whl
~~~

