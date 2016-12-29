# import the SenseHat class from the sense_hat module so we can use it
from sense_hat import SenseHat


# initialize a SenseHat object and save it in the sense variable
sense = SenseHat()

# do forever
while True:
    # get the temperature from the Sense Hat
    temperature = sense.get_temperature()

    # round the temperature to 2 decimal digits
    temperature = round(temperature, 2)

    # the temperature is normal, under 30 degrees Celsius
    if temperature < 30:
        # print the temperature on the LED matrix
        sense.show_message(str(temperature))
    # the temperature is elevated, between 30 and 40 degrees Celsius
    elif temperature < 40:
        # print the temperature on the LED matrix in red
        sense.show_message(str(temperature), text_colour=[255, 0, 0])
    # the temperature is extremelly high, over 40 degrees Celsius
    else:
        sense.show_message(str(temperature), text_colour=[255, 0, 0])
        sense.show_message(' ')
        sense.show_message("ATTENTION! EXTREME TEMPERATURE!", text_colour=[255, 0, 0])

    # print a space to separate the sequential messages on the LED matrix
    sense.show_message(' ')
