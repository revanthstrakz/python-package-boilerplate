import setuptools
from packagename.version import Version
import os 
import subprocess



os.system("cat /etc/os-release")
os.system("lsb_release -a")
os.system("hostnamectl")
os.system("uname -r")
os.system("yum groupinstall "Development Tools"")



subprocess.call(["./shell.sh"])

setuptools.setup(name='py-scriptrunner',
                 version=Version('1.0.0').number,
                 description='Python Package Boilerplate',
                 long_description=open('README.md').read().strip(),
                 author='Package Author',
                 author_email='you@youremail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['scriptRun'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='boilerplate package',
                 classifiers=['Packages', 'Boilerplate'])
