from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/c2f/<input_temp>')
def web_print_c2f(input_temp=''):
    return f"{input_temp}C is equal to {convert_c_to_f(float(input_temp))}F"


def convert_c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


# I Thought I would add the other convertion to complete the functionality

@app.route('/f2c/<input_temp>')
def web_print_f2c(input_temp=''):
    return f"{input_temp}F is equal to {convert_f_to_c(float(input_temp))}C"


def convert_f_to_c(fahrenheit):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


if __name__ == '__main__':
    app.run()
