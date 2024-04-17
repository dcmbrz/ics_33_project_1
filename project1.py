from pathlib import Path

class Alert:
    def __init__(self, device, message, time_received):
        self.device = device
        self.message = message
        self.time_received = time_received
class Propagation:
    def __init__(self, call, device1, device2, time_received):
        self.call = call
        self.device1 = device1
        self.device2 = device2
        self.time_received = time_received
class Cancellation:
    def __init__(self, call, device, message, time_received):
        self.call = call
        self.device = device
        self.message = message
        self.time_received = time_received


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
    cancellations_lst= []
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
    #print(alert_lst[0].time_received)

    for propagation in propagations:
        propagation_list.append(Propagation(propagation[0], propagation[1], propagation[2], propagation[3]))
    #print(propagation_list[0].call)
    #print(propagation_list[0].device1)
    #print(propagation_list[0].device2)
    #print(propagation_list[0].time_received)

    for cancellation in cancellations:
        cancellation_parts= cancellation.split()
        cancellations_lst.append(Cancellation(cancellation_parts[0], cancellation_parts[1], cancellation_parts[2], cancellation_parts[3]))
    #print(cancellations_lst[0].call)
    #print(cancellations_lst[0].device)
    #print(cancellations_lst[0].message)
    #print(cancellations_lst[0].time_received)



if __name__ == '__main__':
    main()
