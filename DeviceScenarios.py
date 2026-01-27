import time
import random
import re

results = [
    {"device": "Camera1", "status": "Fail"},
    {"device": "Radio1", "status": "Pass"},
    {"device": "Camera1", "status": "Pass"}
]

#Create a summary dictionary: {"Camera1": {"Pass": 1, "Fail": 1}, "Radio1": {"Pass": 1, "Fail": 0}}
def returnDeviceSummary(result):
    summarydict={}
    for result in results:
        device=result["device"]
        status=result["status"]
        #check if device exists
        if (device not in summarydict):
            # Initialize the nested dictionary with default values 0
            summarydict[device]={"Pass":0 , "Fail":0}

        #Update the status count
        summarydict[device][status] +=1
    print(summarydict)

#Function iterates to check device status for every 1 second and if not up within timeout return Timeout exception
def check_status(device_id:str):
    return random.choice([True,False])

def devicewait(device_id:str, timeout:int):
    start_time=time.time()
    while time.time()-start_time <timeout:
        if check_status(device_id)== True:
            return "DEVICE iS READY"
        time.sleep(1)
    raise TimeoutError(f"Device{device_id}failed to initialize")

#Function to read logfiles line by line
def extract_warnings(file_path):
    warnings = []

    # Using 'with' is best practice for automatic file closing
    with open(file_path, 'r') as file:
        # This loop is memory-efficient (O(1) memory)
        for line in file:
            if "[WARN]" in line:
                warnings.append(line.strip())

    return warnings


def extractbatterypercentage():

    line = "2023-10-01 12:00:05 [WARN] Device Radio1: Battery level 15%"

    # \d+ looks for one or more digits
    # The () around \d+ tells Python "this is the specific part I want to grab"
    match = re.search(r"(\d+)%", line)

    if match:
        battery_value = match.group(1)
        print(f"Extracted Value: {battery_value}")  # Output: 15


print(extractbatterypercentage)

#print(devicewait("Device1",1))

#returnDeviceSummary(results)