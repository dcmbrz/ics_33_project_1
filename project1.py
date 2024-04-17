from pathlib import Path





def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())



def main() -> None:
    """Runs the simulation program in its entirety"""
    lines = []
    devices = []
    propagations = []
    alerts = []
    time = []
    cancellations = []
    input_file_path = _read_input_file_path()
    with open(input_file_path, 'r+') as file:
        for line in file:
            lines.append(line.strip('\n'))
        for line in lines:
            if line.startswith('DEVICE'):
                devices.append(line)
            if line.startswith('PROPAGATE'):
                propagations.append(line)
            if line.startswith('ALERT'):
                alerts.append(line)
            if line.startswith('CANCEL'):
                cancellations.append(line)


    #print(lines)
    print(devices, propagations, alerts, cancellations)




if __name__ == '__main__':
    main()
