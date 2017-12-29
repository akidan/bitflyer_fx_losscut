#-*- coding: UTF-8 -*-
import os,sys
if len(sys.argv) < 4 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
  print "Usage: Parameter[0] [1]       [2]        [3]       [4]      [5]"
  print "python loss-cut.py 預入証拠金 必要証拠金 btcFX数量 [倍数=2] [買/売フラグ]"
else:
  needDeposit = float(sys.argv[1])
  hasDeposit  = float(sys.argv[2])
  btcFx = float(sys.argv[3])
  if len(sys.argv)<5:
    times = 2.0
  else:
    times = float(sys.argv[4])
  sellFlg = 1.0
  if len(sys.argv)>5:
    sellFlg = -1.0
  print "Add-deposit: " + str((hasDeposit*(times+sellFlg*0.8)-sellFlg*needDeposit)/btcFx)
  print "Loss-cut   : " + str((hasDeposit*(times+sellFlg*0.5)-sellFlg*needDeposit)/btcFx)
