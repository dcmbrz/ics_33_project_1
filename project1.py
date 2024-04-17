from pathlib import Path

class Alert:
    def __init__(self, device, messge, time_recieved):
        self.device = device
        self.messge = messge
        self.time_recieved = time_recieved


def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())



def main() -> None:
    """Runs the simulation program in its entirety"""
    lines = []
    devices = []
    propagations = []
    propagation_list= []
    alerts = []
    alert_lst= []
    time = []
    cancellations = []
    input_file_path = _read_input_file_path()
    with open(input_file_path, 'r+') as file:
        for line in file:
            lines.append(line.strip('\n'))
        for line in lines:
            if line.startswith('DEVICE'):
                devices.append(line)
            elif line.startswith('PROPAGATE'):
                propagations.append(line.split())
            elif line.startswith('ALERT'):
                alerts.append(line)
            elif line.startswith('CANCEL'):
                cancellations.append(line)



    for alert in alerts:
        alert_parts= alert.split()
        alert_lst.append(Alert(alert_parts[1], alert_parts[2], alert_parts[3]))
    print(alert_lst[0].time_recieved)

    #print(devices, propagations, alerts, cancellations)
    #print(propagations)




if __name__ == '__main__':
    main()
