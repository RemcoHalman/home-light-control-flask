import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template
from phue import Bridge

load_dotenv()

b = Bridge(os.getenv("BRIDGE_IP"))
b.connect()


def home():
    return render_template('index.html', title="Home")

def light(light, value):
    b.set_light(light, 'bri', int(value)) #'Woonkamer lamp 2'
    return redirect('/')

def uit(light):
    b.set_light(f'{light}', 'on', False)
    return redirect('/')

def aan(light):
    b.set_light(f'{light}', 'on', True)
    return redirect('/')
