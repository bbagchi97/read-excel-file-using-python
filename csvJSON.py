import csv, json

def csv_JSON():
	# Selecting file path and setting output file name
	csvFilePath = "airlines.csv"
	jsonFilePath = "output1.json"

	# Read the CSV and add the data to dictionary
	data = {}
	with open(csvFilePath) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:
			a_code = csvRow["Airport.Code"]
			data[a_code] = csvRow	
	
	# Write data to a JSON file
	with open(jsonFilePath, "w") as jsonFile:
		jsonFile.write(json.dumps(data, indent=4))

# Call the function
csv_JSON()