#print number in binary 
print ("35 in binary = {:b}".format(35))
#35 in binary = 100011

#print number in octal 
print ("35 in octal = {:o}".format(35))
#35 in octal = 43

#print number in decimal
print ("35 in decimal = {:d}".format(35))
#35 in decimal = 35

#print number in hexadecimal
print ("35 in hexadecimal = {:x}".format(35))
#35 in hexadecimal = 23

#print number in hexadecimal with prefix
print ("35 in binary with prefix = {:#b}".format(35))
#35 in binary with prefix = 0b100011


# convert int to string
number_string = format(35, 'b')
print ("number_string with binary ", number_string)

number_string = format(35, 'o')
print ("number_string with octal ", number_string)

number_string = format(35, 'd')
print ("number_string with decimal ", number_string)

number_string = format(35, 'x')
print ("number_string with hex ", number_string)

number_string = format(35, '#x')
print ("number_string with octal 0x ", number_string)


# convert string to int
number_string_bin = format(35, 'b')
number_int_bin = int(number_string_bin, base=2)
number_int_bin = number_int_bin + number_int_bin
print ("number_int_bin with binary ", number_int_bin)