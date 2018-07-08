
import re

gcode_regex_x = re.compile(r'X\D*\d*\W*')
gcode_regex_z = re.compile(r'Z\D*\d*\W*')
x_dimension_regex = re.compile(r'\d*\W\d*')
first_letters_regex = re.compile(r'[G]\d*')
gcode_regex_none_z = re.compile(r'(!Z)')

#filename = input("Please provide the name of the gcode files.")
filename = "rolka.t"

file_1 = open(filename, 'r')
contents = file_1.readlines()
file_1.close()

x_values = {}
z_values = {}
#array_values = {x_values, z_values}

for i, line in enumerate(contents):

    if len(line.strip()) == 0 :
        continue
    
    if 'X' in line:
        x_search = gcode_regex_x.search(line)
        x_val = x_search.group()
        
        if len(x_val.strip()) != 0 :
            x_values[i] = x_val.strip()
            #print x_val.strip()
        
    #print(line)
    #continue
 
print(x_values) 
#for arrv in array_values :
#for j, result_value in x_values:
    #print j+result_value
        
input("Press the enter to exit: ")
