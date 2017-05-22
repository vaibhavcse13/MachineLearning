import pyexcel as pe
import pyexcel.ext.xls
import pyexcel.ext.xlsx
records = pe.get_records(f = "C:\Users\vaibhav\Downloads\Data\Delhi\MonthlyDelhiRainFall.xls")

for record in records:
    s = records['Jan'] + records['Feb']

print(s)
