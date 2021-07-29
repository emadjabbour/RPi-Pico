#written by Emad Jabbour https://www.youtube.com/c/emadjab
import pwmio
import analogio
import board
import time
import lcd

led = pwmio.PWMOut(board.GP0, frequency=1000)
pot = analogio.AnalogIn(board.GP28)
lcd.i2cinit()
while True:
    pv = pot.value - 5700
    if pv < 0:
        pv = 0
    led.duty_cycle = pv
    print(pv)

    lcd.LCDPrint("Voltage "+ str(0.00005*pv),2,"Duty_cycle "+ str(pv))
    time.sleep(0.1)


