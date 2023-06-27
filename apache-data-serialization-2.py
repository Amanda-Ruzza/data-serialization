import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
from datetime import datetime
from decimal import Decimal
import logging
import argparse

class ParseCSVToPSV(beam.DoFn):
    def process(self, element):
        # element corresponds to a single row in the CSV file
        row = element.split(',')  
        product_name = row[1]
        yield (product_name, {
            "First Sale": datetime.fromtimestamp(int(row[0])),
            "Last Sale": datetime.fromtimestamp(int(row[0])),
            "Total Quantity Sold": int(row[2]),
            "Total Sales Amount": Decimal(row[3])
        })

class WriteToPSV(beam.DoFn):
    def process(self, element):
        sales_report = element
        
        header_names = ["Product Name", "First Sale", "Last Sale", "Total Quantity Sold", "Total Sales Amount"]
        yield '|'.join(header_names)

        for product in sales_report.keys():
            yield '|'.join([
                product,
                str(sales_report[product].get("First Sale")),
                str(sales_report[product].get("Last Sale")),
                str(sales_report[product].get("Total Quantity Sold")),
                str(sales_report[product].get("Total Sales Amount"))
            ])

def run_pipeline(argv=None):

  """Main entry point; defines and runs the CSV parser pipeline."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--input',
    dest='input',
    help='Input file to process.')
  parser.add_argument(
    '--output',
    dest='output',
    required=True,
    help='Output file to write results to.')
  known_args, pipeline_args = parser.parse_known_args(argv)

  pipeline_options = PipelineOptions(pipeline_args)
  with beam.Pipeline(options=pipeline_options) as pipeline:
        sales_data = (
            pipeline
            | 'ReadCSVFile' >> beam.io.ReadFromText(known_args.input)
        ) 
        processed_data = (
            sales_data    
            | 'SkipHeaderRow' >> beam.Filter(lambda row: not row.startswith('Timestamp'))
            | 'ParseCSVtoPSV' >> beam.ParDo(ParseCSVToPSV())
        )
        data_transformation = (
            processed_data
            | 'WriteProcessedData' >> beam.ParDo(WriteToPSV())
            | 'WriteToNewFile' >> beam.io.WriteToText(known_args.output, file_name_suffix='.psv')
            | 'PrintToConsole' >> beam.Map(print)
        )

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run_pipeline()

