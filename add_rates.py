#-------------------------------------------------------------------------------
# Name:        Add RATES to branch
# Version:     0.3
# Purpose:
#
# Author:      oskars.g
#
# Created:     26.06.2023
# Copyright:   (c) oskars.g 2023
# Licence:     Free to modify and use
#-------------------------------------------------------------------------------

import os, sys, csv
PSSE_PATH = r'C:\Program Files\PTI\PSSE35\35.3\PSSBIN'
sys.path.append(PSSE_PATH)
os.environ['PATH'] += ';' + PSSE_PATH
import psse3503
import psspy
import pssexcel
psspy.psseinit(7000)

RATE_DATAFILE = './rate_list.csv'
CASE = './D040723_10_LVLTV2_2.sav'

data = list(csv.reader(open(RATE_DATAFILE)))  # read csv
for line, busfrm, busto, ckt, r1, r2, r3,r4,r5,r6,r7,r8,r9 in data:
    busfrm = int(busfrm)
    busto = int(busto)
    ckt = str(ckt)
    rate1 = float(r1)
    rate2 = float(r2)
    rate3 = float(r3)
    rate4 = float(r4)
    rate5 = float(r5)
    rate6 = float(r6)
    rate7 = float(r7)
    rate8 = float(r8)
    rate9 = float(r9)
    psspy.case(CASE)
    psspy.branch_chng_3(busfrm, busto, ckt, [],[],[rate1,rate2,rate3,rate4,rate5,rate6,rate7,rate8,rate9])

psspy.save(CASE)

