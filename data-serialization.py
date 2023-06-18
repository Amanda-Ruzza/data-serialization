import csv
import logging
import sys, getopt
import datetime 
import hashlib

# set the logger

logging.basicConfig(filename="data-serialization.log", 
					format='%(levelname)s:%(name)s:%(message)s', 
					filemode='w')
logger = logging.getLogger(__name__)
logger.root.setLevel('DEBUG')


# ADD THE COLUMN FOR THE TIMESTAMP CONVERSION, AND ATTACH IT TO THE MAIN ARGV FUNCTION
# ADD THE COLUMN FOR THE PRODUCT NAME PROCESSING WITH THE QUANTITY SOLD + TOTAL SALES AMMOUNT FUNCTION AND ATTACH IT TO THE MAIN ARGV FUNCTION
# This the function where we want to entry the script
def main(argv):
    inputfile = ''
    outputfile = ''
    columnnames = []
    try:
       opts, args = getopt.getopt(argv[1:],"hi:o:c:",["ifile=","ofile=", "column="])
    except getopt.GetoptError:
       print (f"{argv[0]} -i <inputfile> -o <outputfile> -c <columnname>")
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
           print (f"{argv[0]} -i <inputfile> -o <outputfile> -c <columnname>")
           sys.exit()
       elif opt in ("-i", "--ifile"):
           inputfile = arg
       elif opt in ("-o", "--ofile"):
           outputfile = arg
       elif opt in ("-c", "--column"):
           columnnames = arg.split(',')

    logger.info('Input file is: ' + str(inputfile))
    parse_file(inputfile, outputfile, columnnames)
    logger.info('Output file is: ' + str(outputfile))

# testing this with the hashing function. Delete this once things are working
HASH_SALT = "keij3ka2Hie2lilie1aiwab5oaQuooth"

def hash_field(field: str) -> str:
    salted_value = "{}{}".format(field, HASH_SALT)
    return str(hashlib.sha1(salted_value.encode("utf-8")).hexdigest())[:12]    
def product_organizer():
# extracts the information from the column 'Product Name' and organizes all the quantity and prices from 
# 'ProdA, ProdB, ProdC and ProdD' 
    pass
    
### Add the date time function here
def timestamp_converter():
    pass

def first_sale_writer():
    pass

def last_sale_writer():
    pass

def total_quantity_sold():
    
    pass 
    
def total_sales_amount():
# extract the quantity and price for 
    pass
            
# Main function that parses the file:
def parse_file(input_file_name, output_file_name, columns_to_parse):
    with open(input_file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(output_file_name, 'w') as new_file:
            
            fieldnames = next(csv_reader)
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter='\t')
            # csv_writer.writeheader() # writes the header from the original CSV into the new one
            # logger.info('Header written to: ' + str(outputfile))
            fieldnames = ["Product Name", "First Sale", "Last Sale", "Total Quantity Sold", "Total Sales Amount"]        
            csv_writer.writeheader()
            # csv_writer.writerow({"Product Name": "Blue Car", "First Sale": "12-23-1987", "Last Sale": "06-17-2019", "Total Quantity Sold": "4", "Total Sales Amount": "25"} )
        for line in csv_reader:
            for column in columns_to_parse:
                    line[column] = hash_field(line[column])
                    
                    csv_writer.writerow(line)


if __name__ == "__main__":
    main(sys.argv)