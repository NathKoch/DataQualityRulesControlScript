# Data Quality Rules Control Script

This script is designed to validate data in an Excel file against specific business rules. It reads data from multiple sheets in the Excel file and performs various checks to ensure data integrity and correctness. The script uses `pandas` for data manipulation and `numpy` for numerical operations. It includes several custom functions to validate different types of data based on predefined business rules. Below is a detailed description of the script's functionality.

## Features

- **Excel File Reading**: Reads data from specified sheets in an Excel file.
- **Data Validation**: Implements multiple checks to validate data according to business rules.
- **Custom Functions**: Defines functions to check positive numbers, string lengths, and valid names.
- **Summary Output**: Prints the results of the validation checks, including counts of rows that pass and fail each rule.

## Data Quality Rules 

1. **Reporting Year**: All data in the 'ReportingYear' column of the 'report' table must be positive.
2. **Country Code**: All data in the 'CountryCode' column of the 'report' table must be two characters long.
3. **Report ID**: All data in the 'ReportID' column of the 'report' table must be integers.
4. **Coordinate System Name**: All names in the 'CoordinateSystemName' column of the 'report' table must be correctly spelled.
5. **Release Medium Name**: All names in the 'ReleaseMediumName' column of the 'pollutantRelease' table must be correctly spelled.
6. **Pollutant Group Name**: All names in the 'PollutantGroupName' column of the 'pollutantRelease' table must be correctly spelled.
7. **Unit Name**: All names in the 'UnitName' column of the 'pollutantRelease' table must be correctly spelled.
8. **Total Quantity**: All data in the 'TotalQuantity' column of the 'pollutantRelease' table must be positive.
9. **Accidental Quantity**: All data in the 'AccidentalQuantity' column of the 'pollutantRelease' table must be positive.

## Functions

### `checkPositiveNumber(value)`
- Checks if a value is a positive number or a string that can be converted to a positive number.

### `checkLength2(code)`
- Checks if a string is exactly two characters long.

### `checkIdFormat(id)`
- Checks if a value is an integer.

### `checkValidNames(vname)`
- Checks if a value matches one of the valid names in a predefined list.

## Usage

1. Place the script in a directory with the required Excel file.
2. Update the `file_path` variable with the path to the Excel file.
3. Run the script to perform the data validation checks.

## Output

- The script prints the number of rows passing and failing each business rule check.
- Detailed lists of rows failing each check are also printed for further analysis.

## Script Output

```plaintext
Business Rule 1. All data in column 'ReportingYear' of table 'report' must be positive (> 0).
Number of rows passing business rule checks: 63
Number of rows failing business rule checks: 1 

Business Rule 8. All data in column 'TotalQuantity' of table 'pollutantRelease' must be positive.
Number of rows passing business rule checks: 1553
Number of rows failing business rule checks: 4 

Business Rule 9. All data in column 'AccidentalQuantity' of table 'pollutantRelease' must be positive.
Number of rows passing business rule checks: 1553
Number of rows failing business rule checks: 4 

Business Rule 2. All data in column 'CountryCode' of table 'report' must be two characters long.
Number of rows passing business rule checks: 62
Number of rows failing business rule checks: 2 

Business Rule 3. All data in column 'ReportID' of table 'report' must be integers.
Number of rows passing business rule checks: 63
Number of rows failing business rule checks: 1 

Business Rule 5. All names in column 'ReleaseMediumName' of table 'pollutantRelease' must be correctly spelled.
Number of rows passing business rule checks: 1556
Number of rows failing business rule checks: 1 

Business Rule 4. All names in column 'CoordinateSystemName' of table 'report' must be correctly spelled.
Number of rows passing business rule checks: 62
Number of rows failing business rule checks: 2 

Business Rule 6. All names in column 'PollutantGroupName' of table 'pollutantRelease' must be correctly spelled.
Number of rows passing business rule checks: 1556
Number of rows failing business rule checks: 1 

Business Rule 7. All names in column 'UnitName' of table 'pollutantRelease' must be correctly spelled.
Number of rows passing business rule checks: 1554
Number of rows failing business rule checks: 3

Rows failing business rule checks in reportTable:

Index  ReportID
52    123.6
Name: ReportID, dtype: float64

Index  ReportingYear
7   -2017
Name: ReportingYear, dtype: int64

Index  CountryCode
16    FIN
50    NOR
Name: CountryCode, dtype: object

Rows failing business rule checks in pollutantReleaseTable:

Index  TotalQuantity
194    "-8000.0"
358          NaN
632          NaN
739          NaN
Name: TotalQuantity, dtype: object

Index  AccidentalQuantity
122      NaN
214      NaN
739      NaN
1126   -10.0
Name: AccidentalQuantity, dtype: float64

Index  CoordinateSystemName
43     WGS-84
57    WGS 8.4
Name: CoordinateSystemName, dtype: object

Index  ReleaseMedium
696    Airo
Name: ReleaseMediumName, dtype: object

Index  PollutantGroupName
1089    Hevi metall
Name: PollutantGroupName, dtype: object

Index  UnitName
156          kg
431     k-gramm
1121        NaN
Name: UnitName, dtype: object
```

## Requirements

- Python 3.12 or higher
- `pandas` library
- `numpy` library
- `matplotlib` library (data visualization in the future)


To install the required libraries, use:
```bash
pip install pandas numpy matplotlib
```

This script is a useful tool for ensuring data quality and integrity, making it easier to maintain accurate and reliable data sets.