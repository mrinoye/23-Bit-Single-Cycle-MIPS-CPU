def convertBinToHex(bin):
    hex =" "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    elif bin == "00000":
        hex = "0"
    elif bin == "00001":
        hex = "1"
    elif bin == "00010":
        hex = "2"
    elif bin == "00011":
        hex = "3"
    elif bin == "00100":
        hex = "4"
    elif bin == "00101":
        hex = "5"
    elif bin == "00110":
        hex = "6"
    elif bin == "00111":
        hex = "7"
    elif bin == "01000":
        hex = "8"
    elif bin == "01001":
        hex = "9"
    elif bin == "01010":
        hex = "A"
    elif bin == "01011":
        hex = "B"
    elif bin == "01100":
        hex = "C"
    elif bin == "01101":
        hex = "D"
    elif bin == "01110":
        hex = "E"
    elif bin == "01111":
        hex = "F"
    return hex

# AND   r3    r4     r5
# 0001  0011  0100   0101
# 1     3      4      5
# 1345

# //todo check opcode
def checkInstruction(inst):
    convertInstruction = " "
    if inst == "jmp":
        convertInstruction = "001"
    elif  inst == "lw":
        convertInstruction = "010"
    elif inst == "addi":
        convertInstruction = "011"
    elif inst == "nop":
        convertInstruction = "100"
    elif inst == "beq":
        convertInstruction = "101"
    elif inst == "bne":
        convertInstruction = "110"
    elif inst == "sw":
        convertInstruction = "111"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction

# //todo create function to check rtype function bit "SLT": "000",
def checkFunction(func):
    convertInstruction = " "
    if func == "sll":
        convertInstruction = "001"
    elif  func == "sub":
        convertInstruction = "010"
    elif func == "and":
        convertInstruction = "011"
    elif func == "nor":
        convertInstruction = "100"
    elif func == "or":
        convertInstruction = "101"
    elif func == "add":
        convertInstruction = "110"
    elif func == "srl":
        convertInstruction = "111"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction

# //todo change register number to r0 to r22
def checkRegister(reg):
    convertReg = ""
    if  reg == "$r0": 
        convertReg ="00000" 
    elif reg == "$r1":
        convertReg ="00001"
    elif reg == "$r2":
        convertReg ="00010"
    elif reg == "$r3":
        convertReg ="00011"
    elif reg == "$r4":
        convertReg ="00100"
    elif reg == "$r5":
        convertReg ="00101"
    elif reg == "$r6":
        convertReg ="00110"
    elif reg == "$r7":
        convertReg ="00111"
    elif reg == "$r8":
        convertReg ="01000"
    elif reg == "$r9":
        convertReg ="01001"
    elif reg == "$r10":
        convertReg ="01010"
    elif reg == "$r11":
        convertReg ="01011"
    elif reg == "$r12":
        convertReg ="01100"
    elif reg == "$r13":
        convertReg ="01101"
    elif reg == "$r14":
        convertReg ="01110"
    elif reg == "$r15":
        convertReg ="01111"
    elif reg == "$r16":
        convertReg ="10000"
    elif reg == "$r17":
        convertReg ="10001"
    elif reg == "$r18":
        convertReg ="10010"
    elif reg == "$r19":
        convertReg ="10011"
    elif reg == "$r20":
        convertReg ="10100"
    elif reg == "$r21":
        convertReg ="10101"
    elif reg == "$r22":
        convertReg ="10110"
    else:
        convertReg =="Invalid Register"
    return convertReg


def decimalToBinary(num, bit_length=10):
    if num < 0:
        num = (1 << bit_length) + num  # Handle negative numbers using two's complement

    result = ""

    while num > 0:
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        num = num // 2

    result = "0" * (bit_length - len(result)) + result  # Pad with leading zeros
    return result

def decimalToBinary20Bits(num):
    if num < 0:
        num = (1 << 20) + num  # Handle negative numbers using 20-bit two's complement

    result = ""

    while num > 0:
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        num = num // 2

    result = "0" * (20 - len(result)) + result  # Pad with leading zeros to make it 20 bits
    return result

def convertBinToHex(bin):
    hex_output = ""
    # Ensure the binary string length is a multiple of 4
    while len(bin) % 4 != 0:
        bin = "0" + bin  # Pad with leading zeros if necessary

    # Process the binary string in chunks of 4 bits
    for i in range(0, len(bin), 4):
        nibble = bin[i:i+4]  # Take each 4-bit group
        if nibble == "0000":
            hex_output += "0"
        elif nibble == "0001":
            hex_output += "1"
        elif nibble == "0010":
            hex_output += "2"
        elif nibble == "0011":
            hex_output += "3"
        elif nibble == "0100":
            hex_output += "4"
        elif nibble == "0101":
            hex_output += "5"
        elif nibble == "0110":
            hex_output += "6"
        elif nibble == "0111":
            hex_output += "7"
        elif nibble == "1000":
            hex_output += "8"
        elif nibble == "1001":
            hex_output += "9"
        elif nibble == "1010":
            hex_output += "A"
        elif nibble == "1011":
            hex_output += "B"
        elif nibble == "1100":
            hex_output += "C"
        elif nibble == "1101":
            hex_output += "D"
        elif nibble == "1110":
            hex_output += "E"
        elif nibble == "1111":
            hex_output += "F"
    return hex_output

#a[1,6,7,8]
#for(i=0, i<4, i++ )
#    {
#        a[i];
#    }

#a = ['apple', 'ball', 'cat', 'dog']
#for i in a:
#    i

# Update file operations for processing
readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

# Process each line in the input file
for i in readf:
    splitted = i.split()

    # Handle R-type instructions
    if splitted[0] in ["sub", "and", "nor", "or", "add", "srl", "slt", "sll"]:
        opcode = "000"  # Default 3-bit opcode for R-type
        rs = checkRegister(splitted[2])  # 5-bit binary for rs
        rt = checkRegister(splitted[3])  # 5-bit binary for rt
        rd = checkRegister(splitted[1])  # 5-bit binary for rd
        shamt = "00"  # Default 2-bit shamt (e.g., "00" for shift amount)
        func = checkFunction(splitted[0])  # 3-bit binary for function

        # Combine to form the complete 23-bit binary string
        r_binary = opcode + rs + rt + rd + shamt + func

        # Convert to hex and write to file
        hex_output = convertBinToHex(r_binary)
        print(hex_output)
        writef.write(hex_output + "\n")

    # Handle I-type instructions
    elif splitted[0] in ["lw", "addi", "nop", "beq", "bne", "sw"]:
        opcode = checkInstruction(splitted[0])  # 3-bit opcode for I-type
        rs = checkRegister(splitted[2])  # 5-bit binary for rs
        rt = checkRegister(splitted[1])  # 5-bit binary for rt
        immediate = decimalToBinary(int(splitted[3]), 10)  # 10-bit immediate field

        # Combine to form the complete 23-bit binary string
        i_binary = opcode + rs + rt + immediate

        # Convert to hex and write to file
        hex_output = convertBinToHex(i_binary)
        print(hex_output)
        writef.write(hex_output + "\n")

    # Handle J-type instructions
    elif splitted[0] == "jmp":
        opcode = checkInstruction(splitted[0])  # 3-bit opcode for J-type
        address = decimalToBinary(int(splitted[1]), 20)  # 20-bit address field

        # Combine to form the complete 23-bit binary string
        j_binary = opcode + address

        # Convert to hex and write to file
        hex_output = convertBinToHex(j_binary)
        print(hex_output)
        writef.write(hex_output + "\n")
