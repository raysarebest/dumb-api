from flask import Flask
import functools

app = Flask(__name__)

phrase = "dumb"

@app.route("/")
def index():
    return "You gotta tell me how dumb you want it"

@app.route("/<int:count>")
def integer(count):
    return phrase * count

@app.route("/<float:count>")
def decimal(count):
    return (phrase * int(count)) + partial_from_float(count)

@app.route("/<count>")
def special(count):
    try:
        count = float(count)
        positive = abs(count)
        return phrase[::slice_direction(count)] * int(positive) + partial_from_float(count)
    except ZeroDivisionError:
        return ""
    except ValueError:
        # Convert every character to an ASCII value, add them all together, and return that many phrases
        return phrase * functools.reduce(lambda x, y: x + y, [ord(x) for x in count])
    except:
        return "That's too dumb for me"

def partial_from_float(value):
    if value == 0:
        return ""

    positive = slice_direction(value) > 0
    value = abs(value) # Make sure what's passed in is positive to abide by conditional
    value -= int(value) # Round the value down and subtract it from itself to isolate the decimal

    partial = ""
    
    while len(partial) < len(phrase):
        if (len(partial) + 1) / len(phrase) <= value:
            if positive:
                partial += phrase[len(partial)]
            else:
                partial += phrase[len(phrase) - len(partial) - 1]
        else:
            return partial

def slice_direction(value):
    positive = abs(value)
    return int(positive / value)

app.run(debug=True)