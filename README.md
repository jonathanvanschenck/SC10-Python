# SC10-Python
Python class for controlling Thorlabs SC10 shutter.

At this point, the class can only change the state of the shutter from open to closed. Technically the serial connection allows for substantially more control, but the python "time" package should handle this just as well. See page 14-15 of this pdf (https://www.thorlabs.com/drawings/822433ba9fc93b20-C98289CE-9C23-AF3C-511FF9572C7CF9A6/SC10-Manual.pdf) for details on the serial connection.

Best practice is to use the ".openShutter" and ".closeShutter" methods rather than ".toggle" directly, so as to guarentee the state of the shutter at all points in the code.

See example.py for useage
