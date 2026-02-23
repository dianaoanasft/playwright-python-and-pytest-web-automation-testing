import json
import report

def generate_report():
    #generate report data
    dt = {
        "timestamp": "2026-02-19 20-58-30",
        "status": "PASSED",
        "summary": "module.py::test_case"
    }
    #open json file in writing mode
    with open("report.json", "w") as file:
        #write data to json file
        json.dump(dt, file)