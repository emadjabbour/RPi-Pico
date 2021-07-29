#to write single line you just use the 
lcd.LCDPrint("")
#to write 2 lines you just write  
lcd.LCDPrint("",2,"")
# and fill the second Str
import lcd
lcd.i2cinit() //before while 
lcd.LCDPrint("yes",2,"its me")   //in while
