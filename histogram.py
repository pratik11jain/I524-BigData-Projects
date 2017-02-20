import pandas as pd
import pygal

data = pd.read_csv('2016-first-quarter-citations.csv')
ages = data['Cited Person Age']
ages = ages[ages < 100]

new_list = [0] * 100
for x in ages:
    new_list[int(x)] += 1

ages = []
for i in range(0, len(new_list)):
    ages.append((new_list[i], i, i + 1))

hist = pygal.Histogram()
hist.add("ages", ages)
hist.render_to_file("histogram.svg")
