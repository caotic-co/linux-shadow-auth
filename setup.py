from setuptools import find_packages, setup

full_description = '''\
This is a Python module to validate the credentials of a Linux user using the /etc/shadow file.

Please take a look at the full documentation for how to install and use shadow_auth:    
* GitHub page: <https://github.com/ospinakamilo/linux_shadow_authentication/>

How to use Linux Shadow Authentication:
```python
print()
```  

'''


setup(
    name="shadow_auth",
    version="0.1",
    author="Camilo A. Ospina A.",
    author_email="camilo.ospinaa@gmail.com",
    description="Python module to validate the credentials of a Linux user using the /etc/shadow file",
    long_description=full_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ospinakamilo/linux_shadow_authentication/",
    keywords='shadow_auth linux authentication credentials shadow passwd pam',
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
