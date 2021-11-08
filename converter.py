def gcodeToHPGL(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = lines[23:-4]
        for index, line in enumerate(lines):
            line = line.replace('G1 X', '')
            line = line.replace('Y', '')
            line = line.replace('\n', '')
            coords = line.split(' ')
            x = round(float(coords[0]))
            y = round(float(coords[1]))
            line = f'{x},{y}'
            lines[index] = line
        return lines
