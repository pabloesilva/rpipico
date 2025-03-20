from machine import Pin
from time import sleep

led_board = Pin("LED", Pin.OUT)
sleep(1)    #le damos tiempo a vREPL
print("\nLED esta destellando...")
while True:
    try:
        led_board.toggle() #metodo propio de las pico
        # led_board.value(not led_board.value()) #metodo para ambos, si no le paso argumento lee el estado, sino lo escribe
        sleep(.1) # sleep 1sec
    except KeyboardInterrupt:
        break
led_board.off()
print("Listo")
