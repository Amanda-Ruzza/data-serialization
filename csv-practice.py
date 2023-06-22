import csv
import logging
import sys, getopt
from decimal import Decimal
from datetime import datetime 

# Setting up a  logger

logging.basicConfig(filename="data-serialization.log", 
					format='%(levelname)s:%(name)s:%(message)s', 
					filemode='w')
logger = logging.getLogger(__name__)
logger.root.setLevel('DEBUG')

def parse_csv_to_psv():
    with open ('sales.csv', 'r') as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)
        sales_report = {}
        for row in csv_reader:
            product_name = row[1]
            if product_name in sales_report: 
                sales_report[product_name]["First Sale"] = datetime.fromtimestamp(int(row[0]))
                sales_report[product_name]["Last Sale"] = datetime.fromtimestamp(int(row[0]))  
                sales_report[product_name]["Total Quantity Sold"] += int(row[2]) 
                sales_report[product_name]["Total Sales Amount"] += Decimal(row[3])
                
            else:
                  
                sales_report[product_name] = {
                    "First Sale": datetime.fromtimestamp(int(row[0])),
                    "Last Sale": datetime.fromtimestamp(int(row[0])),
                    "Total Quantity Sold": int(row[2]), 
                    "Total Sales Amount": Decimal(row[3])
                }
        
        logger.info(f"Processed the raw data and added to the 'Sales Report Dictionary': \n{sales_report}" )        


        with open ('sales_report.psv', 'w') as outfile:
            header_names = ["Product Name", "First Sale", "Last Sale", "Total Quantity Sold", "Total Sales Amount"]

            csv_writer = csv.writer(outfile, delimiter="|")
            
            csv_writer.writerow(header_names)
            
            for product in sales_report.keys():
                csv_writer.writerow([product, sales_report[product].get("First Sale"),
                                     sales_report[product].get("Last Sale"),
                                     sales_report[product].get("Total Quantity Sold"), 
                                     sales_report[product].get("Total Sales Amount")])
        logger.info(f"\nWrote the processed data to the new file: \n{'sales_report.psv'}" )        
                                    
                                   
parse_csv_to_psv()

