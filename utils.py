import csv

def getClass(csvPath: str, Class: str):
    with open(csvPath, 'r') as file:
        reader = csv.DictReader(file)
        results = []
        for row in reader:
            if (Class.lower().strip() in row["Class"].lower().strip()):
                values = {}
                for field in reader.fieldnames:
                    values[field] = row[field]
                results.append(values)

        return results if results != [] else None

def getPossibleHeaderValues(csvPath: str, header: str):
    uniqueValues = set()
    with open(csvPath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            uniqueValues.add(row[header])
    return list(uniqueValues)

def getCSVHeaders(csvPath: str):
    with open(csvPath, 'r') as file:
        reader = csv.reader(file)

        headers = next(reader)
        
        return headers

def searchByHeader(csvPath: str, header: str, keyword: str):
    with open(csvPath, 'r') as file:
        reader = csv.DictReader(file)
        results = []
        for row in reader:
            if (keyword.lower().strip() in row[header].lower().strip()):
                values = {}
                for field in reader.fieldnames:
                    values[field] = row[field]
                results.append(values)

        return results if results != [] else None

def searchByAll(csvPath: str, keyword: str):
    with open(csvPath, 'r') as file:
        reader = csv.DictReader(file)
        results = []
        for row in reader:
            for value in row.values():
                print(value)
                if (keyword.strip().lower() in value.strip().lower()):
                    values = {}
                    for field in reader.fieldnames:
                        values[field] = row[field]
                    results.append(values)

        return results if results != [] else None
    
def searchByAllAndClass(csvPath: str, keyword: str, Class: str):
    with open(csvPath, 'r') as file:
        reader = csv.DictReader(file)
        results = []
        for row in reader:
            if (Class.lower().strip() in row["Class"].lower().strip()):
                for value in row.values():
                    if (keyword.strip().lower() in value.strip().lower()):
                        values = {}
                        for field in reader.fieldnames:
                            values[field] = row[field]
                        results.append(values)

        return results if results != [] else None

def searchByMultipleHeaders(csvPath: str, headerKeywordPairs):
    "headerKeywordPairs : {'headerName': 'Value', '2ndHeaderName': 'Value'}"    
    with open(csvPath, 'r') as file:
        reader = csv.DictReader(file)
        results = []
        print(headerKeywordPairs)
        for row in reader:
            allMatch = True
            for headerKeywordPair in headerKeywordPairs.keys():
                key = str(headerKeywordPair)
                value = str(headerKeywordPairs[headerKeywordPair])
                if (value.lower() in row[key].lower()):
                    pass
                else: 
                    allMatch = False 
            if (allMatch == True):
                values = {}
                for field in reader.fieldnames:
                    values[field] = row[field]
                results.append(values)

    return results