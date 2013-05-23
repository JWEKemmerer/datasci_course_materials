import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key = Document Identifiers
    key = record[0]
    # value = Document Contents(Text)
    value = record[1]
    words = set(value.split())
    for i in words:
        mr.emit_intermediate(str(i), str(key))

def reducer(key, list_of_values):
    mr.emit((key, list_of_values))    

if __name__ == '__main__':
    docid = open(sys.argv[1])
    mr.execute(docid, mapper,reducer)

