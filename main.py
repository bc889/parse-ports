import re

with open("./datain.txt", "r") as f:
  content = f.read()

# Match for possible references to port numbers based on patterns from the logs: 
# look for a case-insensitive instance of "port" or "service", 
# followed by any non-alphanumeric chars in between, then the digits.
portReferences = re.findall('(port|service)[^\w]+(\d+)', content, re.IGNORECASE)

# Get the numbers, they should be in the second group.
portNumbers = [match[1] for match in portReferences]

print(portNumbers)
