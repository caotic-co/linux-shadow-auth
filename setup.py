from setuptools import find_packages, setup

full_description = '''\
This is a Python module to validate the credentials of a Linux user using the Pluggable Authentication Modules (PAM)

Please take a look at the full documentation for how to install and use pam-linux:    
* GitHub page: <https://github.com/ospinakamilo/pam-linux/>

How to use pam-linux:
```python
print()
```  

'''


setup(
    name="pam_linux",
    version="0.1",
    author="Camilo A. Ospina A.",
    author_email="camilo.ospinaa@gmail.com",
    description="Python module to validate the credentials of a Linux user using the Pluggable Authentication Modules (PAM)",
    long_description=full_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ospinakamilo/pam-linux/",
    keywords='pam-linux pam linux authentication credentials shadow passwd',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],

    package_dir={"": "src"},

    packages=find_packages(
        where="src",
        exclude=["tests"],
    ),

    python_requires=">3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*,  <4",
    
 )
