#Define a function called multiply. It should have one required parameter, a string. It should also have one optional parameter, an integer, named mult_int, with a default value of 10. The function should return the string multiplied by the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)
def multiply(x, mult_int = 10):
        return x * mult_int

#Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. Fix the code so that it passes the test. This should only require changing one line of code.
#     #1
# def waste(var = "Water", mar, marble = "type"):
#     final_string = var + " " + marble + " " + mar
#     return final_string
    #2
def waste(mar, marble = "type", var = "Water"):
    final_string = var + " " + marble + " " + mar
    return final_string