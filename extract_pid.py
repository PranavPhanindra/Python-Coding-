import re

def extract_pid(log) :
    regex = r"\d{5}"
    result = re.search(regex,log)

    if result is None :
        return ""
    return result[0]

log = input("Enter log line : " )

print(extract_pid(log))

