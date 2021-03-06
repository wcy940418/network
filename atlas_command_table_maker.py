#!/usr/bin/env python

import json

Command_Dict = {}

Command_Dict['Abort'] = {}
Command_Dict['Abort']['name'] = 'Abort'
Command_Dict['Abort']['cmd'] = 0x7F
Command_Dict['Abort']['writebits'] = 8
Command_Dict['Abort']['writedata'] = 0b1010
Command_Dict['Abort']['readbits'] = 0
Command_Dict['Abort']['readdata'] = 0x00
Command_Dict['Abort']['wmin'] = -1
Command_Dict['Abort']['wmax'] = -1
Command_Dict['Abort']['rmin'] = -1
Command_Dict['Abort']['rmax'] = -1
Command_Dict['Abort']['returnable'] = 'none'

Command_Dict['W/R Motor0'] = {}
Command_Dict['W/R Motor0']['name'] = 'W/R Motor0'
Command_Dict['W/R Motor0']['cmd'] = 0x01
Command_Dict['W/R Motor0']['writebits'] = 8
Command_Dict['W/R Motor0']['writedata'] = 0x00
Command_Dict['W/R Motor0']['readbits'] = 8
Command_Dict['W/R Motor0']['readdata'] = 0x00
Command_Dict['W/R Motor0']['wmin'] = -127
Command_Dict['W/R Motor0']['wmax'] = 128
Command_Dict['W/R Motor0']['rmin'] = -127
Command_Dict['W/R Motor0']['rmax'] = 128
Command_Dict['W/R Motor0']['returnable'] = 'depends'

Command_Dict['W/R Motor1'] = {}
Command_Dict['W/R Motor1']['name'] = 'W/R Motor1'
Command_Dict['W/R Motor1']['cmd'] = 0x02
Command_Dict['W/R Motor1']['writebits'] = 8
Command_Dict['W/R Motor1']['writedata'] = 0x00
Command_Dict['W/R Motor1']['readbits'] = 8
Command_Dict['W/R Motor1']['readdata'] = 0x00
Command_Dict['W/R Motor1']['wmin'] = -127
Command_Dict['W/R Motor1']['wmax'] = 128
Command_Dict['W/R Motor1']['rmin'] = -127
Command_Dict['W/R Motor1']['rmax'] = 128
Command_Dict['W/R Motor1']['returnable'] = 'depends'

Command_Dict['W/R Motor2'] = {}
Command_Dict['W/R Motor2']['name'] = 'W/R Motor2'
Command_Dict['W/R Motor2']['cmd'] = 0x03
Command_Dict['W/R Motor2']['writebits'] = 8
Command_Dict['W/R Motor2']['writedata'] = 0x00
Command_Dict['W/R Motor2']['readbits'] = 8
Command_Dict['W/R Motor2']['readdata'] = 0x00
Command_Dict['W/R Motor2']['wmin'] = -127
Command_Dict['W/R Motor2']['wmax'] = 128
Command_Dict['W/R Motor2']['rmin'] = -127
Command_Dict['W/R Motor2']['rmax'] = 128
Command_Dict['W/R Motor2']['returnable'] = 'depends'

Command_Dict['W/R Motor3'] = {}
Command_Dict['W/R Motor3']['name'] = 'W/R Motor3'
Command_Dict['W/R Motor3']['cmd'] = 0x04
Command_Dict['W/R Motor3']['writebits'] = 8
Command_Dict['W/R Motor3']['writedata'] = 0x00
Command_Dict['W/R Motor3']['readbits'] = 8
Command_Dict['W/R Motor3']['readdata'] = 0x00
Command_Dict['W/R Motor3']['wmin'] = -127
Command_Dict['W/R Motor3']['wmax'] = 128
Command_Dict['W/R Motor3']['rmin'] = -127
Command_Dict['W/R Motor3']['rmax'] = 128
Command_Dict['W/R Motor3']['returnable'] = 'depends'

Command_Dict['W/R Motor4'] = {}
Command_Dict['W/R Motor4']['name'] = 'W/R Motor4'
Command_Dict['W/R Motor4']['cmd'] = 0x05
Command_Dict['W/R Motor4']['writebits'] = 8
Command_Dict['W/R Motor4']['writedata'] = 0x00
Command_Dict['W/R Motor4']['readbits'] = 8
Command_Dict['W/R Motor4']['readdata'] = 0x00
Command_Dict['W/R Motor4']['wmin'] = -127
Command_Dict['W/R Motor4']['wmax'] = 128
Command_Dict['W/R Motor4']['rmin'] = -127
Command_Dict['W/R Motor4']['rmax'] = 128
Command_Dict['W/R Motor4']['returnable'] = 'depends'

Command_Dict['W/R Motor5'] = {}
Command_Dict['W/R Motor5']['name'] = 'W/R Motor5'
Command_Dict['W/R Motor5']['cmd'] = 0x06
Command_Dict['W/R Motor5']['writebits'] = 8
Command_Dict['W/R Motor5']['writedata'] = 0x00
Command_Dict['W/R Motor5']['readbits'] = 8
Command_Dict['W/R Motor5']['readdata'] = 0x00
Command_Dict['W/R Motor5']['wmin'] = -127
Command_Dict['W/R Motor5']['wmax'] = 128
Command_Dict['W/R Motor5']['rmin'] = -127
Command_Dict['W/R Motor5']['rmax'] = 128
Command_Dict['W/R Motor5']['returnable'] = 'depends'

Command_Dict['W/R Servo0'] = {}
Command_Dict['W/R Servo0']['name'] = 'W/R Servo0'
Command_Dict['W/R Servo0']['cmd'] = 0x07
Command_Dict['W/R Servo0']['writebits'] = 8
Command_Dict['W/R Servo0']['writedata'] = 0x00
Command_Dict['W/R Servo0']['readbits'] = 8
Command_Dict['W/R Servo0']['readdata'] = 0x00
Command_Dict['W/R Servo0']['wmin'] = 0
Command_Dict['W/R Servo0']['wmax'] = 255
Command_Dict['W/R Servo0']['rmin'] = 0
Command_Dict['W/R Servo0']['rmax'] = 255
Command_Dict['W/R Servo0']['returnable'] = 'depends'

Command_Dict['W/R Servo1'] = {}
Command_Dict['W/R Servo1']['name'] = 'W/R Servo1'
Command_Dict['W/R Servo1']['cmd'] = 0x08
Command_Dict['W/R Servo1']['writebits'] = 8
Command_Dict['W/R Servo1']['writedata'] = 0x00
Command_Dict['W/R Servo1']['readbits'] = 8
Command_Dict['W/R Servo1']['readdata'] = 0x00
Command_Dict['W/R Servo1']['wmin'] = 0
Command_Dict['W/R Servo1']['wmax'] = 255
Command_Dict['W/R Servo1']['rmin'] = 0
Command_Dict['W/R Servo1']['rmax'] = 255
Command_Dict['W/R Servo1']['returnable'] = 'depends'

Command_Dict['W/R Servo2'] = {}
Command_Dict['W/R Servo2']['name'] = 'W/R Servo2'
Command_Dict['W/R Servo2']['cmd'] = 0x09
Command_Dict['W/R Servo2']['writebits'] = 8
Command_Dict['W/R Servo2']['writedata'] = 0x00
Command_Dict['W/R Servo2']['readbits'] = 8
Command_Dict['W/R Servo2']['readdata'] = 0x00
Command_Dict['W/R Servo2']['wmin'] = 0
Command_Dict['W/R Servo2']['wmax'] = 255
Command_Dict['W/R Servo2']['rmin'] = 0
Command_Dict['W/R Servo2']['rmax'] = 255
Command_Dict['W/R Servo2']['returnable'] = 'depends'

Command_Dict['W/R Servo3'] = {}
Command_Dict['W/R Servo3']['name'] = 'W/R Servo3'
Command_Dict['W/R Servo3']['cmd'] = 0x0a
Command_Dict['W/R Servo3']['writebits'] = 8
Command_Dict['W/R Servo3']['writedata'] = 0x00
Command_Dict['W/R Servo3']['readbits'] = 8
Command_Dict['W/R Servo3']['readdata'] = 0x00
Command_Dict['W/R Servo3']['wmin'] = 0
Command_Dict['W/R Servo3']['wmax'] = 255
Command_Dict['W/R Servo3']['rmin'] = 0
Command_Dict['W/R Servo3']['rmax'] = 255
Command_Dict['W/R Servo3']['returnable'] = 'depends'

Command_Dict['W/R Servo4'] = {}
Command_Dict['W/R Servo4']['name'] = 'W/R Servo4'
Command_Dict['W/R Servo4']['cmd'] = 0x0b
Command_Dict['W/R Servo4']['writebits'] = 8
Command_Dict['W/R Servo4']['writedata'] = 0x00
Command_Dict['W/R Servo4']['readbits'] = 8
Command_Dict['W/R Servo4']['readdata'] = 0x00
Command_Dict['W/R Servo4']['wmin'] = 0
Command_Dict['W/R Servo4']['wmax'] = 255
Command_Dict['W/R Servo4']['rmin'] = 0
Command_Dict['W/R Servo4']['rmax'] = 255
Command_Dict['W/R Servo4']['returnable'] = 'depends'

Command_Dict['W/R Servo5'] = {}
Command_Dict['W/R Servo5']['name'] = 'W/R Servo5'
Command_Dict['W/R Servo5']['cmd'] = 0x0c
Command_Dict['W/R Servo5']['writebits'] = 8
Command_Dict['W/R Servo5']['writedata'] = 0x00
Command_Dict['W/R Servo5']['readbits'] = 8
Command_Dict['W/R Servo5']['readdata'] = 0x00
Command_Dict['W/R Servo5']['wmin'] = 0
Command_Dict['W/R Servo5']['wmax'] = 255
Command_Dict['W/R Servo5']['rmin'] = 0
Command_Dict['W/R Servo5']['rmax'] = 255
Command_Dict['W/R Servo5']['returnable'] = 'depends'

Command_Dict['W/R Servo6'] = {}
Command_Dict['W/R Servo6']['name'] = 'W/R Servo6'
Command_Dict['W/R Servo6']['cmd'] = 0x0d
Command_Dict['W/R Servo6']['writebits'] = 8
Command_Dict['W/R Servo6']['writedata'] = 0x00
Command_Dict['W/R Servo6']['readbits'] = 8
Command_Dict['W/R Servo6']['readdata'] = 0x00
Command_Dict['W/R Servo6']['wmin'] = 0
Command_Dict['W/R Servo6']['wmax'] = 255
Command_Dict['W/R Servo6']['rmin'] = 0
Command_Dict['W/R Servo6']['rmax'] = 255
Command_Dict['W/R Servo6']['returnable'] = 'depends'

Command_Dict['W/R Servo7'] = {}
Command_Dict['W/R Servo7']['name'] = 'W/R Servo7'
Command_Dict['W/R Servo7']['cmd'] = 0x0e
Command_Dict['W/R Servo7']['writebits'] = 8
Command_Dict['W/R Servo7']['writedata'] = 0x00
Command_Dict['W/R Servo7']['readbits'] = 8
Command_Dict['W/R Servo7']['readdata'] = 0x00
Command_Dict['W/R Servo7']['wmin'] = 0
Command_Dict['W/R Servo7']['wmax'] = 255
Command_Dict['W/R Servo7']['rmin'] = 0
Command_Dict['W/R Servo7']['rmax'] = 255
Command_Dict['W/R Servo7']['returnable'] = 'depends'

Command_Dict['W/R Switches'] = {}
Command_Dict['W/R Switches']['name'] = 'W/R Switches'
Command_Dict['W/R Switches']['cmd'] = 0x0f
Command_Dict['W/R Switches']['writebits'] = 8
Command_Dict['W/R Switches']['writedata'] = 0x00
Command_Dict['W/R Switches']['readbits'] = 8
Command_Dict['W/R Switches']['readdata'] = 0x00
Command_Dict['W/R Switches']['wmin'] = 0	
Command_Dict['W/R Switches']['wmax'] = 255
Command_Dict['W/R Switches']['rmin'] = 0
Command_Dict['W/R Switches']['rmax'] = 255
Command_Dict['W/R Switches']['returnable'] = 'depends'

Command_Dict['Read Voltage'] = {}
Command_Dict['Read Voltage']['name'] = 'Read Voltage'
Command_Dict['Read Voltage']['cmd'] = 0x10
Command_Dict['Read Voltage']['writebits'] = 8
Command_Dict['Read Voltage']['writedata'] = 0x00
Command_Dict['Read Voltage']['readbits'] = 16
Command_Dict['Read Voltage']['readdata'] = 0x00
Command_Dict['Read Voltage']['wmin'] = 0	
Command_Dict['Read Voltage']['wmax'] = 255
Command_Dict['Read Voltage']['rmin'] = 0	
Command_Dict['Read Voltage']['rmax'] = 65536
Command_Dict['Read Voltage']['returnable'] = 'required'

Command_Dict['Read Current'] = {}
Command_Dict['Read Current']['name'] = 'Read Current'
Command_Dict['Read Current']['cmd'] = 0x11
Command_Dict['Read Current']['writebits'] = 8
Command_Dict['Read Current']['writedata'] = 0x00
Command_Dict['Read Current']['readbits'] = 16
Command_Dict['Read Current']['readdata'] = 0x00
Command_Dict['Read Current']['wmin'] = 0	
Command_Dict['Read Current']['wmax'] = 255
Command_Dict['Read Current']['rmin'] = 0	
Command_Dict['Read Current']['rmax'] = 65536
Command_Dict['Read Current']['returnable'] = 'required'

Command_Dict['W/R Report Rate'] = {}
Command_Dict['W/R Report Rate']['name'] = 'W/R Report Rate'
Command_Dict['W/R Report Rate']['cmd'] = 0x12
Command_Dict['W/R Report Rate']['writebits'] = 8
Command_Dict['W/R Report Rate']['writedata'] = 0x00
Command_Dict['W/R Report Rate']['readbits'] = 8
Command_Dict['W/R Report Rate']['readdata'] = 0x00
Command_Dict['W/R Report Rate']['wmin'] = 0
Command_Dict['W/R Report Rate']['wmax'] = 255
Command_Dict['W/R Report Rate']['rmin'] = 0
Command_Dict['W/R Report Rate']['rmax'] = 255
Command_Dict['W/R Report Rate']['returnable'] = 'depends'

Command_Dict['W/R Single Switch'] = {}
Command_Dict['W/R Single Switch']['name'] = 'W/R Single Switch'
Command_Dict['W/R Single Switch']['cmd'] = 0x13
Command_Dict['W/R Single Switch']['writebits'] = 8
Command_Dict['W/R Single Switch']['writedata'] = 0x00
Command_Dict['W/R Single Switch']['readbits'] = 8
Command_Dict['W/R Single Switch']['readdata'] = 0x00
Command_Dict['W/R Single Switch']['wmin'] = 0	
Command_Dict['W/R Single Switch']['wmax'] = 255
Command_Dict['W/R Single Switch']['rmin'] = 0
Command_Dict['W/R Single Switch']['rmax'] = 255
Command_Dict['W/R Single Switch']['returnable'] = 'depends'

f = open('atlas_commands.json','w')
json.dump(Command_Dict, f, indent = 2)
f.close()