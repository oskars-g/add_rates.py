#-------------------------------------------------------------------------------
# Name:        Add RATES to branch
# Version:     0.5
# Purpose:
#
# Author:      oskars.g
#
# Created:     26.06.2023
# Copyright:   (c) oskars.g 2023
# Licence:     Free to modify and use
#-------------------------------------------------------------------------------

import os, sys, csv
import psse3503
import psspy
import pssexcel

PSSE_PATH = r'C:\Program Files\PTI\PSSE35\35.3\PSSBIN'
sys.path.append(PSSE_PATH)
os.environ['PATH'] += ';' + PSSE_PATH

psspy.psseinit(7000)

RATE_DATA_FILE = './rate_list.csv'
CASE = './case.sav'

with open(RATE_DATA_FILE) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        line, busfrm, busto, ckt, *rates_str = row

        busfrm = int(busfrm)
        busto = int(busto)
        ckt = str(ckt)

        rates = [float(rate) for rate in rates_str]

        psspy.case(CASE)
        psspy.branch_chng_3(busfrm, busto, ckt, [],[],rates)

psspy.save(CASE)

