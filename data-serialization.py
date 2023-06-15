import csv
import logging
import sys, getopt
import datetime 

logger = logging.Logger(__name__)

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

    logger.info('Input file is: ', inputfile)
    parse_file(inputfile, outputfile, columnnames)
    logger.info('Output file is: ', outputfile)

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
    pass
            
# Main function that parses the file:
def parse_file(input_file_name, output_file_name, columns_to_parse):
    with open(input_file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(output_file_name, 'w') as new_file:
            
            fieldnames = next(csv_reader)
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter='\t')
            csv_writer.writeheader() # writes the header from the original CSV into the new one

            # for line in csv_reader:
            #     for column in columns_to_parse:
            #         line[column] = timestamp_converter(line[column])
                    
            #     csv_writer.writerow(line)


if __name__ == "__main__":
    main(sys.argv)