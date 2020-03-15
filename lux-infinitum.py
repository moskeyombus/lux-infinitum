import serial
import serial.tools.list_ports
import time
import PySimpleGUI as sg

serial_port = None
window = None

def send_event_on_serial(event):
  print('You entered ', event)
  formatted_message = (event.lower() + '\n').encode()
  serial_port.write(formatted_message)

def connect_to_arduino():
  for port in serial.tools.list_ports.comports():
    if port.manufacturer and ("Arduino" in port.manufacturer):
      arduino_port = port
  if arduino_port:
    ser = serial.Serial(port.device, 115200)
    print(ser.name)
  return ser

def build_ui():
  sg.theme('DarkAmber')
  layout = [
              [sg.Button('BLUE', key='BLUE')],
              [sg.Button('RED', key='RED')],
              [sg.Button('GREEN', key='GREEN')],
              [sg.Button('RAINBOW!!!!', key='RAINBOW')],
              [sg.Button('Cancel')]
          ]

  return sg.Window('Window Title', layout)

def init_led_strip():
  led_strip_ready = False

  while(led_strip_ready == False):
    inbound_message = serial_port.readline()

    if(inbound_message):
      print(inbound_message)
      inbound_message = None
      led_strip_ready = True
      send_event_on_serial('rainbow')

def app_loop():
  while(serial_port.is_open):
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        send_event_on_serial('kill')
        serial_port.close()
        break
    else:
      send_event_on_serial(event)
      continue

serial_port = connect_to_arduino()
if serial_port:
  window = build_ui()
  init_led_strip()
  app_loop()
else:
  print("No Arduino found!")
