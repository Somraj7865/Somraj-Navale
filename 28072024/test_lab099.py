import csv
import pandas as pd
class Test_CRUD():
    def test_update1(self):
        with open('testdata.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    def test_update2(self):
        df=pd.read_csv('28072024/testdata.csv')
        print(df)
