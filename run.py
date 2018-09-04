import json
from datetime import datetime

def time_fix(time):
    """ Removes the colon from the UTC timezone, eg +10:00 -> +1000, as colons are not supported in python versions < 3.7 """
    k = time.rfind(":")
    return time[:k] + time[k+1:]

def print_span(indent, id, trace):
    """
    Recursively builds trace message for all children and itself. 
    Checks to see if any children or itself has an error which determines if it should be printed
    """
    logs = trace[id]['logs']
    has_error = False
    print_message = ""
    for log in logs:
        if log.get('error'):
            has_error = True
        print_message += "{0}{1} {2} {3} {4} \n".format(indent, log.get('time'), log.get('app'), log.get('component'), log.get('msg'))
    for c in trace[id]['children']:
        result = print_span(indent + '   ', c, trace)
        if result[0]:
            has_error = True
        print_message += result[1]
    return has_error, print_message
    

with open('spec/log-data.json') as f:
    data = json.load(f)

# sort all logs based on time, assumes all dates are in the same format - O(n log n)
sorted_data = sorted(data, key=lambda k: datetime.strptime(time_fix(k['time']), "%Y-%m-%dT%H:%M:%S%z"))

error_traces = {}

# go through and group all spans from traces with errors by their trace id, O(n)
for log in sorted_data:
    if log['trace_id'] not in error_traces:
        error_traces[log['trace_id']] = {}
    trace = error_traces[log['trace_id']]
    if log['span_id'] not in trace: #initialize this span if it does not exist
        trace[log['span_id']] = {
            'logs': [],
            'children': set()
        }
    trace[log['span_id']]['logs'].append(log)

    if 'parent_span_id' in log:
        if log['parent_span_id'] not in trace: #initialize the parent if it does not exist
            trace[log['parent_span_id']] = {
            'logs': [],
            'children': set()
        }
        trace[log['parent_span_id']]['children'].add(log['span_id'])


# print - O(2n)
for trace in error_traces.keys():
    for span_id in error_traces[trace]:
        logs = error_traces[trace][span_id]['logs']
        if 'parent_span_id' not in logs[0]: #start recurision only from highest level parents
            result = print_span('', logs[0]['span_id'], error_traces[trace])
            if result[0]: #if the trace contains errors print it
                print("TRACE ID: {0}".format(trace))
                print(result[1])