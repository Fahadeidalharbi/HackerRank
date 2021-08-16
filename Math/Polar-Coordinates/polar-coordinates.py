# import cmath package
import cmath
#read an input value 
z = raw_input()
#get phase angle value
pa = cmath.phase(complex(z))
#get modulus r
r = abs(complex(z))

print ("{0}\n{1}".format(r,pa))