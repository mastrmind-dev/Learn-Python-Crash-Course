import re

s = '456-456-456'

result = re.sub('([0-9]{3}-[0-9])', '+1-\\1', s)
print(result)
result = re.sub('([0-9]{3}-[0-9])', r'+1-\1', s)
print(result)
