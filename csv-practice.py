import csv

infile_columns = []
def parse_csv_to_psv():
    with open ('sales.csv', 'r') as infile:
        csv_reader = csv.DictReader(infile, delimiter= '\t')
        
    
        for line in csv_reader:
                
                for column in line:
                    timestamp = ([line[column][0:10]])
                    
                    print(f"This is the timestamp: {timestamp}")
                    product_name = [line[column][11:20]]
                    quantity = [line[column][20:22]]
                    print(f"This is the quantity: {quantity}")
                    price = [line[column][21:26]]
                    print(f"This is the price: {price}")
                    
                    
                    
                

        #     product_name.append(column['Product Name'])
        # print(f"This is the column that has the 'Product Name' information: {product_name}")


        with open ('practice-writing.psv', 'w', newline= '', encoding='utf-8') as outfile:
            header_names = ["Product Name", "First Sale", "Last Sale", "Total Quantity Sold", "Total Sales Amount"]

            csv_writer = csv.DictWriter(outfile, fieldnames=header_names, extrasaction='ignore', delimiter="|")
            
            csv_writer.writerow(timestamp)
            # csv_writer.writerow({"Product Name": "Blue Car", "First Sale": "12-23-1987", "Last Sale": "06-17-2019", "Total Quantity Sold": "4", "Total Sales Amount": "25"} )
            # for line in csv_reader:
            #     for column in csv_reader:
            #         line[column] = outfile(line, column)
                    
parse_csv_to_psv()