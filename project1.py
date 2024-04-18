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


    # def propagation_set(self, device1, device2, time_received):
    #     self.sources[device1] = (device2, time_received)



class Cancellation:
    def __init__(self, call, device, message, time_received):
        self.call = call
        self.device = device
        self.message = message
        self.time_received = time_received
class Timeline:
    def __init__(self, event):
        self.event = event

    def run(self):
        while self.event:
            pass



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
    cancellations = []
    cancellations_lst= []
    input_file_path = _read_input_file_path()
    length_list= []
    length= 0
    sources = {}
    current_time= 0
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
            elif line.startswith('LENGTH'):
                length_list.append(line)
                l= line.split()
                length= int(l[1])


    for alert in alerts:
        alert_parts= alert.split()
        alert_lst.append(Alert(alert_parts[1], alert_parts[2], alert_parts[3]))
    #print(alert_lst[0].device)
    #print(alert_lst[0].time_received)

    for propagation in propagations:
        current_time += int(propagation[3])
        propagation_list.append(Propagation(propagation[0], propagation[1], propagation[2], propagation[3]))
        sources[propagation[1]] = (propagation[2],current_time)
    print(sources)



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

    for i in range(length):
        for k,v in sources.items():
            if v[1] == i:
                print(f'#{k} SENT ALERT TO #{v[0]}: Trouble')







if __name__ == '__main__':
    main()
