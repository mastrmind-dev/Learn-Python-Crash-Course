import re

def extractPID(logLine):
    regex = r"\[(\d+)\]"
    result = re.search(regex, logLine)

    if result is None:
        return print("No errors")
    else:
        return print(result[1])

log = "July 31 07:51:48 mycomputer bad_process[.12345]: ERROR Performing package upgrade"

extractPID(log)
