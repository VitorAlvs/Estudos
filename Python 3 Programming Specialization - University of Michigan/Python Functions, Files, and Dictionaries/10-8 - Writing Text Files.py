import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#First, we will need to open the file. Afterwards, we will iterate through the numbers 1 through 12, and square each one of them. This new number will need to be converted to a string, and then it can be written into the file.
#The program below solves part of the problem. We first want to make sure that we’ve written the correct code to calculate the square of each number.
for number in range(1, 13):
    square = number * number
    print(square)

#When we run this program, we see the lines of output on the screen. Once we are satisfied that it is creating the appropriate output, the next step is to add the necessary pieces to produce an output file and write the data lines to it. To start, we need to open a new output file by calling the `open` function, `outfile = open("squared_numbers.txt",'w')`, using the `'w'` flag.  We can choose any file name we like. If the file does not exist, it will be created. However, if the file does exist, it will be reinitialized as empty and you will lose any previous contents.
#Once the file has been created, we just need to call the `write` method passing the string that we wish to add to the file. In this case, the string is already being printed so we will just change the `print` into a call to the `write` method. However, there is an additional step to take, since the write method can only accept a string as input. We’ll need to convert the number to a string. Then, we just need to add one extra character to the string. The newline character needs to be concatenated to the end of the line. The entire line now becomes `outfile.write(str(square)+'\n')`. The print statement automatically outputs a newline character after whatever text it outputs, but the write method does not do that automatically. We also need to close the file when we are done.The complete program is shown below.
    
filename = "10-8Doc1.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()
