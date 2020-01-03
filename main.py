# CapChecker v1
# Dean Ralph
# Jan 2020

# Description:
# Designed to run on a Raspberry Pi with 4 INA219 i2c current sensors attached.
# The app gathers and records the current use and voltage of attached batteries
# to work out the current capacity of the cell

#Imoprts
from flask import Flask, render_template
import qrcode
import json

#Main App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dbsettings')
def dbsettings():
    return render_template("dbsettings.html")

@app.route('/batteries')
def batteries():
    return render_template("batteries.html")

@app.route('/reports')
def reports():
    return render_template("reports.html")

@app.route('/readings')
def readings():
    return render_template("readings.html")

@app.route('/newBattery')
def newBattery():
    return render_template("newBattery.html")

if __name__ == "__main__":
    app.run()