from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

# Define your LEDs based on your soldered pins
red = LED(17)
yellow = LED(27)
green = LED(22)

# This route sends the HTML page to your browser
@app.route('/')
def index():
    return render_template('index.html')

# This route handles the "logic" when a button is pressed
@app.route('/change_light/<color>')
def change_light(color):
    # Turn everything off first to be safe
    red.off()
    yellow.off()
    green.off()

    if color == 'green':
        green.on()
    elif color == 'yellow':
        yellow.on()
    elif color == 'red':
        red.on()
    
    return f"Light changed to {color}", 200

if __name__ == '__main__':
    # '0.0.0.0' makes the server accessible to other devices on your Wi-Fi
    app.run(host='0.0.0.0', port=5000)
