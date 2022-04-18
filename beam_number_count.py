import apache_beam as beam


with beam.Pipeline() as pipeline:
    data = range(1,10)
    print([i for i in data])
    print([i for i in enumerate(data)])
    print('|'.join([str(i) for i in data[5:7] ]))
    result = ( pipeline
        | beam.Create(data)
        | beam.Map(lambda x: x*2)
        | beam.CombineGlobally(sum)
        | beam.Map(print)
    )
