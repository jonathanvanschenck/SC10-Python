import time
try:
    bb.shutdown()
except:
    pass
bb = SC10()
bb.openShutter()
print('Shutter Open? '+str(bb.qopenShutter()))
time.sleep(1)
bb.closeShutter()
print('Shutter Closed? '+str(bb.qcloseShutter()))
