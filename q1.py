"""
# -----------------------------
# File : q1.py
# Created : 15/10/2021
# Author : Rohit Mishra
# Version : v1.0.0
# Py Version : 2021.2.2
# Licensing : (C) 2021 Rohit Mishra, LYIT
#              Available under GNU Public License (GPL)
# Description : Display OS related information.
# -----------------------------
"""

from os import getcwd
from platform import uname

if __name__ == "__main__":
    print("Current Value of Path:", getcwd())
    print("Machine :", uname().machine)
    print("System :", uname().system)
    print("Node :", uname().node)

