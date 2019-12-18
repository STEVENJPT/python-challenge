import os
import csv
input_file = open("PyBank_budget.csv","r")
reader_file = csv.reader(input_file)
value = len(list(reader_file))-1
print(value)
with open('PyBank_budget.csv', 'r') as f:
  next(f)
  total = 0
  for row in csv.reader(f):
    total += float(row[1])
  print(total)
import csv
import uuid

is_first = True
with open('PyBank_budget.csv', newline='') as input_file:  
    with open('output1.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        reader = csv.reader(input_file)
        for row in reader:
            if is_first:
                row.insert(2, 'Change')
                is_first = False
            else:
                row.insert(2, str(uuid.uuid4()))

            writer.writerow(row)
#got stuck with how to replace the value of the newly created column (one referring to changes)
#Writing what i reckon would be the rest of the code 

# to get the average change would just have to replicate the following
#with open('output1.csv', 'r') as f:
  #next(f)
  #total1 = 0
  #for row in csv.reader(f):
    #total1 += float(row[2])
  #average = (total1/86)
#Then to get the maximum increase in profit/losses and maximum decrease in profit/losses i would do: 
#maximum = max(row[2])
#print(maximum)
#minimum = min(row[2])
#print(minimum)

