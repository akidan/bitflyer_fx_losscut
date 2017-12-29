#-*- coding: UTF-8 -*-
import os,sys
needDeposit = float(sys.argv[1])
hasDeposit  = float(sys.argv[2])
btcFx = float(sys.argv[3])
if len(sys.argv)<5:
  times = 2.0
else:
  times = float(sys.argv[4])
sellFlg = 1.0
if len(sys.argv)>6:
  sellFlg = -1.0
print "Add-deposit: " + str((hasDeposit*(times+sellFlg*0.8)-sellFlg*needDeposit)/btcFx)
print "Loss-cut   : " + str((hasDeposit*(times+sellFlg*0.5)-sellFlg*needDeposit)/btcFx)
