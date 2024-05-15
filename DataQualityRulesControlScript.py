#!/usr/bin/env python3.12
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Excel file location
file_path = '/Users/nathanaelkoch/Documents/Keskkonnaagentuur/andmed.xlsx'

# I used the read_excel() function to read the data, specifying sheet_name='sheet name' because there are three sheets in the Excel file
reportTable = pd.read_excel(file_path, sheet_name='report') # DataFrame containing the 'report' table
facilityTable = pd.read_excel(file_path, sheet_name='facility')
pollutantReleaseTable = pd.read_excel(file_path, sheet_name='pollutantRelease')

# ---------------------------------------------------------------------------------------------------------

# The function checkPositiveNumber checks business rules 1, 8, 9.
''' 
1. All data in column 'ReportingYear' of table 'report' must be positive (> 0).
    (For example: -2017 is incorrect)

8. All data in column 'TotalQuantity' of table 'pollutantRelease' must be positive.
    (For example: "-8000.0", " ", N/A is incorrect)

9. All data in column 'AccidentalQuantity' of table 'pollutantRelease' must be positive.
    (For example: -10, " ", N/A is incorrect)
'''

def checkPositiveNumber(value):
    # Check if the value is a number or a string that can be converted to a number
    if isinstance(value, (int, float)) and value >= 0:
        return True # if the number is positive
    elif isinstance(value, str):
        try:
            # Try converting the string to a number and check if it is positive
            numvalue = float(value)
            if numvalue >= 0:
                return True
            else:
                return False
        except ValueError:
            # If this conversion raises an error, it means conversion to a number is not possible,
            # indicating it's not a numeric value
            return False
    else:
        return False

# Create a new column where the function writes True for values that pass the check and False for values that fail
reportTable['ReportingYear_valid'] = reportTable['ReportingYear'].apply(checkPositiveNumber)

# Aggregate all True values
print("Business Rule 1. All data in column 'ReportingYear' of table 'report' must be positive (> 0).")
print(f'Number of rows passing business rule checks: {reportTable["ReportingYear_valid"].sum()}')
# ~ operator changes boolean meanings to their opposites
print(f'Number of rows failing business rule checks: {(~reportTable["ReportingYear_valid"]).sum()} {'\n'}')

# Function application for the TotalQuantity column
pollutantReleaseTable['TotalQuantity_valid'] = pollutantReleaseTable['TotalQuantity'].apply(checkPositiveNumber)

print("Business Rule 8. All data in column 'TotalQuantity' of table 'pollutantRelease' must be positive.")

print(f'Number of rows passing business rule checks: {pollutantReleaseTable["TotalQuantity_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~pollutantReleaseTable["TotalQuantity_valid"]).sum()} {'\n'}')

# Function application for the AccidentalQuantity column
pollutantReleaseTable['AccidentalQuantity_valid'] = pollutantReleaseTable['AccidentalQuantity'].apply(checkPositiveNumber)

print("Business Rule 9. All data in column 'AccidentalQuantity' of table 'pollutantRelease' must be positive.")
print(f'Number of rows passing business rule checks: {pollutantReleaseTable["AccidentalQuantity_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~pollutantReleaseTable["AccidentalQuantity_valid"]).sum()} {'\n'}')

# ---------------------------------------------------------------------------------------------------------

# The checkLength2 function checks business rule 2.
'''
2. All data in column 'CountryCode' of table 'report' must be two characters long.
    (For example: NOR, FIN is correct)
'''

# Check if all values in the 'CountryCode' column are two characters long
def checkLength2(code):
    return code.str.len() == 2

reportTable['CountryCode_valid'] = checkLength2(reportTable['CountryCode'])

print("Business Rule 2. All data in column 'CountryCode' of table 'report' must be two characters long.")

print(f'Number of rows passing business rule checks: {reportTable["CountryCode_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~reportTable["CountryCode_valid"]).sum()} {'\n'}')

# ---------------------------------------------------------------------------------------------------------

# The checkIdFormat function checks business rule 3.
''' 
3. All data in column 'ReportID' of table 'report' must be integers.
    (For example: 123.6 is incorrect)
'''

def checkIdFormat(id):
   
    if isinstance(id, (int, float)) and id.is_integer():
        return True
    else:
        return False


reportTable['ReportID_valid'] = reportTable['ReportID'].apply(checkIdFormat)

print("Business Rule 3. All data in column 'ReportID' of table 'report' must be integers.")
print(f'Number of rows passing business rule checks: {reportTable["ReportID_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~reportTable["ReportID_valid"]).sum()} {'\n'}')

# ---------------------------------------------------------------------------------------------------------

# The checkValidNames function checks business rules 4, 5, 6, 7.
''' 
4. All names in column 'CoordinateSystemName' of table 'report' must be correctly spelled.
    (For example: WGS-84 is correct, WGS 8.4 is incorrect)

5. All names in column 'ReleaseMediumName' of table 'pollutantRelease' must be correctly spelled.
    (For example: Air is correct)

6. All names in column 'PollutantGroupName' of table 'pollutantRelease' must be correctly spelled.
    (For example: Heavy metals is correct)

7. All names in column 'UnitName' of table 'pollutantRelease' must be correctly spelled.
    (For example: kilogram is correct)
'''
# Array of valid names against which the checkValidNames function checks all names
validNames = ["Air", "Water"]

def checkValidNames(vname):
    if vname in validNames:
        return True # return True if the name is found in the array of valid names
    else:
        return False

# Function application for the ReleaseMediumName column
pollutantReleaseTable['ReleaseMedium_valid'] = pollutantReleaseTable['ReleaseMediumName'].apply(checkValidNames)

print("Business Rule 5. All names in column 'ReleaseMediumName' of table 'pollutantRelease' must be correctly spelled.")

print(f'Number of rows passing business rule checks: {pollutantReleaseTable["ReleaseMedium_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~pollutantReleaseTable["ReleaseMedium_valid"]).sum()} {'\n'}')

# Array of valid names
validNames = ["WGS 84", "ETRS89 (2D)"]
# Function application for the CoordinateSystemName column
reportTable['CoordinateSystemName_valid'] = reportTable['CoordinateSystemName'].apply(checkValidNames)

print("Business Rule 4. All names in column 'CoordinateSystemName' of table 'report' must be correctly spelled.")
print(f'Number of rows passing business rule checks: {reportTable["CoordinateSystemName_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~reportTable["CoordinateSystemName_valid"]).sum()} {'\n'}')

# Function application for the PollutantGroupName column

validNames = ["Heavy metals", "Other organic substances"]
pollutantReleaseTable['PollutantGroupName_valid'] = pollutantReleaseTable['PollutantGroupName'].apply(checkValidNames)

print("Business Rule 6. All names in column 'PollutantGroupName' of table 'pollutantRelease' must be correctly spelled.")
print(f'Number of rows passing business rule checks: {pollutantReleaseTable["PollutantGroupName_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~pollutantReleaseTable["PollutantGroupName_valid"]).sum()} {'\n'}')

# Function application for the UnitName column 

validNames = ["kilogram"]
pollutantReleaseTable['UnitName_valid'] = pollutantReleaseTable['UnitName'].apply(checkValidNames)

print("Business Rule 7. All names in column 'UnitName' of table 'pollutantRelease' must be correctly spelled.")

print(f'Number of rows passing business rule checks: {pollutantReleaseTable["UnitName_valid"].sum()}')
print(f'Number of rows failing business rule checks: {(~pollutantReleaseTable["UnitName_valid"]).sum()}')

# ---------------------------------------------------------------------------------------------------------

# Print indexes of rows that fail check for table reportTable
print("\nRows failing business rule checks in reportTable:")

print("\nIndex  ReportID")
print(reportTable.loc[~reportTable["ReportID_valid"], "ReportID"])

print("\nIndex  ReportingYear")
print(reportTable.loc[~reportTable["ReportingYear_valid"], "ReportingYear"])



print("\nIndex  CountryCode")
print(reportTable.loc[~reportTable["CountryCode_valid"], "CountryCode"])

# Print indexes of rows that fail the check for the pollutantReleaseTable
print("\nRows failing business rule checks in pollutantReleaseTable:")

print("\nIndex  TotalQuantity")
print(pollutantReleaseTable.loc[~pollutantReleaseTable["TotalQuantity_valid"], "TotalQuantity"])

print("\nIndex  AccidentalQuantity")
print(pollutantReleaseTable.loc[~pollutantReleaseTable["AccidentalQuantity_valid"], "AccidentalQuantity"])

print("\nIndex  CoordinateSystemName")
print(reportTable.loc[~reportTable["CoordinateSystemName_valid"], "CoordinateSystemName"])

print("\nIndex  ReleaseMedium")
print(pollutantReleaseTable.loc[~pollutantReleaseTable["ReleaseMedium_valid"], "ReleaseMediumName"])

print("\nIndex  PollutantGroupName")
print(pollutantReleaseTable.loc[~pollutantReleaseTable["PollutantGroupName_valid"], "PollutantGroupName"])

print("\nIndex  UnitName")
print(pollutantReleaseTable.loc[~pollutantReleaseTable["UnitName_valid"], "UnitName"])
# ---------------------------------------------------------------------------------------------------------



