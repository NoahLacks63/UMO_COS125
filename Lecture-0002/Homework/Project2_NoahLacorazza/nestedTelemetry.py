# File: nestedTelemetry.py
# Author: Noah Lacorazza
# Date: 12/12/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# Recursively process a nested telemetry data file to extract and log information about subsystems
# Collaboration:
# N/A

TELEMETRY_FILE = "simplifiedTelemetry500.txt"

SEGMENT_ID = "[SEGMENT_ID:"
SUBSYSTEM = "[SUBSYSTEM:"
POWER = "P"
THERMAL = "T"
GUIDANCE = "G"

def main():
    subsystem = input("Enter subsystem to analyze (P/T/G): ").upper()

    with open(TELEMETRY_FILE) as f:
        lines = f.readlines()
    
    telemetry_data = sort_telemetry(lines, {}, None, None)

    min_val, max_val = find_extremes(telemetry_data, "M1", POWER)

    log(telemetry_data, subsystem, min_val, max_val)


def sort_telemetry(lines, result, segment_id, subsystem):
    if len(lines) <= 0:
        return result
    
    line = lines[0].strip()
    seg_len = len(SEGMENT_ID)
    sub_len = len(SUBSYSTEM)

    if line[:seg_len] == SEGMENT_ID:
        result[line[seg_len:-1]] = {}
        return sort_telemetry(lines[1:], result , line[seg_len:line.index("]")], subsystem)
    
    if line[:sub_len] == SUBSYSTEM:
        result[segment_id][line[sub_len:line.index("]")]] = {}
        return sort_telemetry(lines[1:], result, segment_id, line[sub_len:line.index("]")])
    
    parts = line.split(",")
    if len(parts) == 2:
        print(parts)
        result[segment_id][subsystem][int(parts[0])] = float(parts[1])
        return sort_telemetry(lines[1:], result, segment_id, subsystem)
    
    return sort_telemetry(lines[1:], result, segment_id, subsystem)

def find_extremes(telemetry, segment_id, subsystem):
    data = telemetry[segment_id][subsystem]
    values = list(data.values())
    return recursive_minmax(values, 0, values[0], values[0])

def recursive_minmax(values, index, current_min, current_max):
    if index >= len(values):
        return current_min, current_max

    val = values[index]

    if val < current_min:
        current_min = val
    if val > current_max:
        current_max = val

    return recursive_minmax(values, index + 1, current_min, current_max)

def count_pulses(data):
    print("hullo")
    if len(data) == 0:
        return 0
    
    key = list(data.keys())[0]
    
    return len(data[key][POWER]) + len(data[key][THERMAL]) + len(data[key][GUIDANCE]) + count_pulses(dict(list(data.items())[1:]))

def log(data, subsystem, min_val, max_val):
    name = input("Enter log file name: ")

    try:
        with open(name, "x") as f:
            f.write(f"Telemetry File: {TELEMETRY_FILE}\n")
            f.write(f"Subystem: {subsystem}\n")
            f.write(f"Total Pulses: {count_pulses(data)}\n")
            f.write(f"Min Value: {min_val}\n")
            f.write(f"Max Value: {max_val}\n")
    except FileExistsError:
        print("Log file already exists.")
        log(data, subsystem, min_val, max_val)

main()