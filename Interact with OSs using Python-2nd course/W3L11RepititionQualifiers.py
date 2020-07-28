import re

print(re.search(r"[a-zA-Z]{5}", "There is scary a ghost"))

print(re.findall(r"\b[a-zA-Z]{2}\b", "There is scary a ghost"))

print(re.findall(r"B\w{,20}.", "There is scary a ghost but I don't afraid. It is a BullShitMotherFucker"))
