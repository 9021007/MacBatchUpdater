from distutils.cmd import Command
import subprocess

print("updating brew")
subprocess.run(["brew", "upgrade"])
print("updating macports with admin rights")
subprocess.run(["sudo", "port", "selfupdate"])
subprocess.run(["sudo", "port", "upgrade", "outdated"])
print("updating pip")
subprocess.run(["pip3", "install", "--upgrade", "pip"])
print("updating pip packages")
subprocess.run(["pip3", "list", "--outdated", "--format=freeze"])
print("updating npm")
subprocess.run(["npm", "install", "-g", "npm"])
print("updating npm packages")
subprocess.run(["npm", "update", "-g"])
