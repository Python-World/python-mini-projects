import json
import csv

# Open the JSON file and save the data as a variable.
with open('input.json') as f:
    data = json.load(f) # Originally I used loads, but that caused a type error. Loads converts the data in memory
    
familyData = data["data_file"]

# Create a file for writing
writeFile = open('output.csv', 'w')

# CSV writer object
csvWriter = csv.writer(writeFile)

# Counter used for headers
count = 0

for name in familyData:
    if count == 0:
        
        # Creates the initial headers using the first object
        header = name.keys()
        csvWriter.writerow(header)
        count += 1
        
    csvWriter.writerow(name.values())
    
writeFile.close()
