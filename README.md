# Data Serialization
Python Script that converts CVS Files

## How it works:
Python program that reads the "sales.csv" file, converts the epoch timestamps to a readable format, and calculates the total sales for each product. The program should then write the first sale product name, datetime, last sale datetime, total quantity sold, and total sales amount to a new PSV file named "sales_report.psv".

### Running Instructions

- The original file needs to be either in the project folder, or a full path
- The original file needs to have a ``Header`` 
- To run the file, execute the following command:
    ```
    python data-serialization.py -i <inputfilename> -o <outputfilename> -c <columnname>  
    ```
 ``-c, or --column`` is the name of the column which needs to be [PROCESSED!!]
 
 **Important:** There cannot be spaces in between column names!
 Example on how to execute this code:
    ```
    python data-serialization.py -i sales.csv -o sales_report.psv -c 'Job Title','First Name'
    ```


## Future Improvements