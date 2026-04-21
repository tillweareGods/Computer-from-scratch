def And(a,b):
  return a and b

def Or(a,b):
  return a or b

def Xor(a,b):
  return a != b

def Invert(a):
  return not a

# Adds bunary numbers based on input
def Adder(a,b,carry_in=0):
  sum_component1 = Xor(a,b)
  carry_compnent_1 = And(a,b)
  sum_component_final = Xor(sum_component1,carry_in)
  carry_compnent_2 = And(sum_component1,carry_in)
  carry_out = Or(carry_compnent_1,carry_compnent_2)
  return sum_component_final,carry_out



'''
my_sum,carry = Adder(input_value[0],input_value[1])
print(f"The sum of {int(input_value[0])} and {int(input_value[1])} = \n{int(carry),int(my_sum)}")

'''



# Add and subtract based on the cary bit , makes it programable
def Full_Subtracter(a, b, mode=0):

    b_modified = Xor(b, mode)   
    sum1 = Xor(a, b_modified)

    sum_final = Xor(sum1, mode)

    carry1 = And(a, b_modified)
    carry2 = And(sum1, mode)
    carry_out = Or(carry1, carry2)

    return sum_final, carry_out

input_value = [True,True,True]

value,carry = Full_Subtracter(input_value[0],input_value[1],input_value[2])
print(f"The sum of {int(input_value[0])} and {int(input_value[1])} = \n{int(carry),int(value)}")
