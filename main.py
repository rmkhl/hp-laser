import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource('GPIB0::3::INSTR', timeout=60000)

def writeCommand(command):
  inst.write('{}'.format(command))

def readOutput(command):
  inst.write('{}'.format(command))
  while True:
    try:
      byte = inst.read_bytes(1)
      print(byte)
      if byte == b'\n':
        break
    except:
      break

# 1-36
def setSpeed(speed):
  inst.write('VS {};'.format(speed))

def movePen(x, y):
  inst.write('PA {},{};'.format(x, y))
  inst.write('OA;')
  while True:
    byte = inst.read_bytes(1)
    if byte == b'\n':
      break
  return True

def home():
  movePen(0, 0)

def init():
  writeCommand('PU')
  home()
  setSpeed(1)

if __name__ == '__main__':
  init()
  with open('pylpyra.txt', 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
      if index == 0:
        writeCommand('PD')
      coords = line.split(',')
      x = round(float(coords[0]) * 50)
      y = round(float(coords[1]) * 50)

      movePen(x, y)
  writeCommand('PU')
  home()
