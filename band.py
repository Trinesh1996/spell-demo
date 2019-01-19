import json
import random

data = json.loads(open("bandName.json").read())

bandName = data['bands']
print(bandName)


band = random.sample(bandName, 10)

output = "The Random: \n"

for bands in band:
    output += bands + "\n"

print(output)

with open ('allbands.txt', 'w') as file:
    file.write(output)