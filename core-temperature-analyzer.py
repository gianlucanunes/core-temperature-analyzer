# ----------------------------------------------------------
# Core Temperature Analyzer
# by Gianluca Nunes
# March 1, 2023
#
# This program analyzes the core temperature of a computer
# using the software Core Temp. Core Temp creates the log files 
# (.csv) and this program organizes the data from the log files 
# in order to make a more intuitive chart with the Date and its
# measures. After that, it returns you with an average CPU
# temperature of the last five days.
#
# ----------------------------------------------------------


# Importing libraries
import datetime
import numpy as np
import pandas as pd
import time
import os
from termcolor import colored


# Header
os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 50)
print("{:^50}".format("Core Temperature Analyzer"))
print("{:^50}".format("by Gianluca Nunes"))
print("=" * 50)


# Warning
print(colored("\n\nWarning: before using the program, make sure Core Temp is closed and not running in your background.\n", "red", "on_white", attrs=["bold"]))
input("\nWhen ready, press any key to start the Core Temperature Analyzer.\nRemember: you should not open any file related to this program during the analysis process.\n")

time.sleep(1)
print("Please wait...")
time.sleep(1)