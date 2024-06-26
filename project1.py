from pathlib import Path
from queue import PriorityQueue
class Alert:
    def __init__(self,call, device, message, time_received):
        self.call = call
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
        alert_lst.append(Alert(alert_parts[0],alert_parts[1], alert_parts[2], alert_parts[3]))

    for propagation in propagations:
        propagation_list.append(Propagation(propagation[0], propagation[1], propagation[2], propagation[3]))
        sources[propagation[1]] = (propagation[2],propagation[3])

    for cancellation in cancellations:
        cancellation_parts= cancellation.split()
        cancellations_lst.append(Cancellation(cancellation_parts[0], cancellation_parts[1], cancellation_parts[2], cancellation_parts[3]))

    queue_messages= []
    input_messages= PriorityQueue()
    q= PriorityQueue()

    for alert in alert_lst:
        input_messages.put((int(alert_lst[0].time_received), alert_lst[0].call, alert_lst[0].message, alert_lst[0].device, None))
    for cancellation in cancellations_lst:
        input_messages.put((int(cancellations_lst[0].time_received), cancellations_lst[0].call, cancellations_lst[0].message, cancellations_lst[0].device, None))
    while not input_messages.empty():
        queue_messages.append(input_messages.get())

    for msg in queue_messages:
        q.put(msg)

    cancel_dict= {}
    for source in sources.keys():
        cancel_dict[source]= []

    while not q.empty():
        top_alert = q.get()
        if top_alert[0] > length:
            break

        if "ALERT" in top_alert[1]:
            if top_alert[4] is not None:
                print(f'@{top_alert[0]}: #{top_alert[3]} RECEIVED ALERT FROM #{top_alert[4]}: {top_alert[2]}')
            if top_alert[2] in cancel_dict[top_alert[3]]:
                continue
            print(f'@{top_alert[0]}: #{top_alert[3]} SENT ALERT TO #{sources[top_alert[3]][0]}: {top_alert[2]}')
            msg = (top_alert[0] + int(sources[top_alert[3]][1]), top_alert[1], top_alert[2],sources[top_alert[3]][0], top_alert[3])
            q.put(msg)

        if "CANCEL" in top_alert[1]:
            if top_alert[4] is not None:
                print(f'@{top_alert[0]}: #{top_alert[3]} RECEIVED CANCELLATION FROM #{top_alert[4]}: {top_alert[2]}')
            if top_alert[2] in cancel_dict[top_alert[3]]:
                continue
            cancel_dict[top_alert[3]].append(top_alert[2])
            print(f'@{top_alert[0]}: #{top_alert[3]} SENT CANCELLATION TO #{sources[top_alert[3]][0]}: {top_alert[2]}')
            msg = (top_alert[0] + int(sources[top_alert[3]][1]), top_alert[1], top_alert[2],sources[top_alert[3]][0], top_alert[3])
            q.put(msg)
    print(f'@{length}: END')




if __name__ == '__main__':
    main()
