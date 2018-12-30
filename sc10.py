"""
This class controls a Thorlabs SC10 shutter controller through a serial connection.

Jonathan Van Schenck, 11/14/18
"""
import serial
class SC10:
    def __init__(self,comport='COM1'):
        """
        Initialized hardware with a closed shutter
        """
        self.ser = serial.Serial(comport,9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
        if self.qopenShutter():
            self.toggleShutter()
        
    def toggleShutter(self):
        """
        toggles the state of the shutter
        """
        jump = self.ser.write('ens\r'.encode())
        self.ser.read(size=jump+2)
        
    def qopenShutter(self):
        """
        Checks if shutter is open
        """
        jump = self.ser.write('ens?\r'.encode())
        #print(jump)
        self.ser.read(size=jump)
        res = self.ser.read()
        self.ser.read(size=3)
        #print(res)
        if  res == b'1':
            return True
        elif res == b'0':
            return False
        else:
            print('Something\'s amiss, closing serial connection...')
            self.shutdown()
    
    def qcloseShutter(self):
        """
        checks if shutter is closed
        """
        return not self.qopenShutter()
    
    def openShutter(self):
        """
        opens shutter, if closed
        """
        if not self.qopenShutter():
            self.toggleShutter()
    
    def closeShutter(self):
        """
        closes shutter if opened
        """
        if self.qopenShutter():
            self.toggleShutter()
        
    def shutdown(self):
        """
        closes the serial connection. MUST EXICUTED BEFORE CALLING ANOTHER 
        INSTANCE OF THIS CLASS, otherwise you need restart your kernel.
        """
        self.ser.close()
