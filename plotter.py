import pyvisa

class Plotter:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.inst = rm.open_resource('GPIB0::3::INSTR', timeout=60000)
    
    def writeCommand(self, command):
        self.inst.write(f'{command}')

    # 1-36
    def setSpeed(self, speed):
        self.inst.write(f'VS {speed};')

    def penUp(self):
        self.writeCommand('PU')

    def penDown(self):
        self.writeCommand('PD')

    def movePen(self, x, y):
        inst = self.inst

        inst.write(f'PA {x},{y};')
        inst.write('OA;')
        while True:
            try:
                byte = inst.read_bytes(1)
                if byte == b'\n':
                    break
            except:
                break
        return True

    def home(self):
        self.movePen(0, 0)

    def init(self):
        self.penUp()
        self.home()
        self.setSpeed(1)
    
    def endSequence(self):
        self.penUp()
        self.home()

    def printFile(self, file):
        from converter import gcodeToHPGL
        moves = gcodeToHPGL(file)
        for index, move in enumerate(moves):
            if index == 0:
                self.penDown()
            coords = move.split(',')
            self.movePen(coords[0], coords[1])
