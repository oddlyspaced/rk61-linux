# pip install hidapi

import hid

# from lsusb :
# Bus 001 Device 002: ID 258a:004a SINO WEALTH RK Bluetooth Keyboard
RK61_VID = 0x258a
RK61_PID = 0x004a

# LED Mode Feature Report
report = bytearray(65)
report[0] = 0x0a 
report[1] = 0x01
report[2] = 0x01
report[3] = 0x02 
report[4] = 0x29
report[5] = 0x01 # light mode [1 - 15] 
report[6] = 0x00
report[7] = 0x01 # speed [1 - 5]

report[8] = 0x05 # brightness [0 - 5]
report[9] = 0xff # Green [00 - ff]
report[10] = 0xff # Red [00 - ff]
report[11] = 0xff # Blue [00 - ff]
report[12] = 0x01 # rainbow colors [0, 1]
report[13] = 0x05 # sleep duration [1 - 5]

print("Sending Report to Keyboard: " + report.hex(" "))

rk61 = hid.enumerate(RK61_VID, RK61_PID)
kb_path = rk61[1].get('path') # serial path for keyboard usb

h = hid.device()
h.open_path(kb_path)

# send bytes
h.send_feature_report(bytes(report))
h.close()

# Reference :
#        00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
# 0000   0a 01 01 02 29 01 00 05 01 00 ff 00 01 05 00 00   ....)...........
# 0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
# 0020   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
# 0030   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
# 0040   00                                                .
