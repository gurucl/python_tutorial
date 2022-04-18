import re
import pyspark

sc = pyspark.SparkContext()

result = sc.parallelize(range(1,10)).map(lambda x:x*2).reduce(lambda x,y:x+y)

print(result)