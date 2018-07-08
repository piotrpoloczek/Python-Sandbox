import re

gcode_regex_x = re.compile(r'X\D*\d*\W*')
gcode_regex_z = re.compile(r'Z\D*\d*\W*')

#filename = input("Please provide the name of the gcode files.")
filename = "rolka.t"

file_1 = open(filename, 'r')
contents = file_1.readlines()
file_1.close()
	
i = 1
	
for line in contents:
	
	
	
	try:
		mo_z = gcode_regex_z.search(line)
			
		if "." not in mo_z.group():
			print("You missed the point in " + str(i) + " line.")
			print("The line is: " + line)
				
	except AttributeError:
		pass
		
	try:
		mo_x = gcode_regex_x.search(line)
			
		if "." not in mo_x.group():
			print("You missed the point in " + str(i) + " line.")
			print("The line is: " + line)
				
	except AttributeError:
		pass
		
	i = i + 1
	
input("Press the enter to exit: ")
