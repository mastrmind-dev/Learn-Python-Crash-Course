import re

def rearrangeName(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)

    if result == None:
        return "Doesn't match to the search pattern."
    return "{} {}".format(result[2], result[1])

print(rearrangeName("Morahela, Sapthaka A."))
