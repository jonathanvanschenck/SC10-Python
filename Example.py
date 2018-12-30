import time, sc10
try:
    bb.shutdown()
except:
    pass
bb = sc10.SC10()
bb.openShutter()
print('Shutter Open? '+str(bb.qopenShutter()))
time.sleep(1)
bb.closeShutter()
print('Shutter Closed? '+str(bb.qcloseShutter()))
