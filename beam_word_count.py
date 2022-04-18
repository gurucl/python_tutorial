
from venv import create
import apache_beam as beam
import re


with beam.Pipeline() as pipeline:
    input_file_path = "/Users/gurumurthy.cl/Documents/python_tutorial/resources/text.txt"
    output_file_path = "/Users/gurumurthy.cl/Documents/python_tutorial/resources/output"
    with beam.Pipeline() as pipeline:
        result = (pipeline
        | beam.io.ReadFromText(input_file_path)
        #| beam.FlatMap(lambda x: x.split(' '))
        | beam.FlatMap(lambda x: re.findall('[A-Za-z]+', x))
        | beam.Map(lambda x: (x,1))
        #| beam.combiners.Count.PerElement()
        | beam.CombinePerKey(sum)
        | beam.MapTuple(lambda x,y: f"{x},{y}")
        #| beam.MapTuple(lambda x,y: f"word: {x},   count: {y}")
        #| beam.sort()
        #| beam.combiners.Sample.FixedSizeGlobally(3)
        #| beam.Map(print)
        | beam.io.WriteToText(output_file_path)
        #| _WriteTextMode()
        )
    

    
