
__author__ = 'kikita'


filename = 'james2.txt'

with open(filename) as f:
    data = f.readline()

templ = data.strip().split(',')

print templ


print type(templ)

