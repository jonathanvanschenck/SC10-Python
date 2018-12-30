# SC10-Python
Python class for controlling Thorlabs SC10 shutter.

At this point, the class can only change the state of the shutter from open to closed. Technically the serial connection allows for substantially more control, but the python "time" package should handle this just as well. See page 14-15 of the attached pdf for details on the serial connection.

Best practice is to use the ".openShutter" and ".closeShutter" methods rather than ".toggle" directly, so as to guarentee the state of the shutter at all points in the code.

See example.py for useage
