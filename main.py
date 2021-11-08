from plotter import Plotter

if __name__ == '__main__':
  plotter = Plotter()
  plotter.init()
  plotter.printFile('pylpyra.gcode')
  plotter.endSequence()
