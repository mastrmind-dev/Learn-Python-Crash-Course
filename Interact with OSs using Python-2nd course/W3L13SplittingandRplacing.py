import re

result = re.split(r"([.?!])", "One sentence. Another one? Last one!")
print(result)

result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recieved an Email for example_for@example.co-m")
print(result)

result = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(result)
