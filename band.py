import json
import random
import sys




filename = sys.argv[1]
data = json.loads(open(filename).read())

bandName = data['bands']
print(bandName)


band = random.sample(bandName, 10)

output = "The Random: \n"

for bands in band:
    output += bands + "\n"

print(output)

with open ('allbands.txt', 'w') as file:
    file.write(output)