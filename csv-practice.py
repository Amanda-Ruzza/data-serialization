import csv

infile_columns = []
def parse_csv_to_psv():
    with open ('sales.csv', 'r') as infile:
        csv_reader = csv.reader(infile, delimiter= '\t')
         
        rows = []
        for row in csv_reader:
            rows.append(row) 
            print(rows)   
            print(f"This CSV has {len(rows)} rows")
        product_a = list(map(lambda t: 'Product A'  not in t, rows))
        # product_a = [a for a in rows if "Product A" in a]
        print(product_a.count(True))
        filtered_rows = []
        for product_a in rows:
            split_product_a = product_a.split('Product A')
            if "Product A" in split_product_a:
                filtered_rows.append(",".join(split_product_a))
            else:
                split_product_a.clear()
        print(filtered_rows)


        product_b = []
        product_c = []
        product_d = []  



        with open ('practice-writing.psv', 'w', newline= '', encoding='utf-8') as outfile:
            header_names = ["Product Name", "First Sale", "Last Sale", "Total Quantity Sold", "Total Sales Amount"]

            # csv_writer = csv.writer(outfile, fieldnames=header_names, extrasaction='ignore', delimiter="|")
            
            # csv_writer.writerow(timestamp)
            # csv_writer.writerow({"Product Name": "Blue Car", "First Sale": "12-23-1987", "Last Sale": "06-17-2019", "Total Quantity Sold": "4", "Total Sales Amount": "25"} )
            # for line in csv_reader:
            #     for column in csv_reader:
            #         line[column] = outfile(line, column)
                    
parse_csv_to_psv()