## We Need an Emulator ##



Attached is some some never-before-seen assembly code routine that we pulled off a processor which is responsible for string decryption. An input string is put into TRX register, then the routine is run, which decrypts the string.

For example, when putting UL\x03d\x1c'G\x0b'l0kmm_ string in TRX and executing this code, the resulting string in TRX is decrypted as 'tenable.ctfd.io'.

A few things we know about this assembly:

    There are only two registers, DRX and TRX. These are used to hold variables throughout the runtime.

    Operand order is similar to the AT&T syntax ,which has destination operand first and source operand 2nd ie: MOV DRX, "dogs", puts the string "dogs" into DRX register/variable. XOR TRX, DRX, xors the string held in DRX with the string in TRX and stores the result in TRX register/variable.

    There are only three instructions that this processor supports:

        XOR - XORs the destination string against a source string and stores the result in the destination string operand. The source string operand can be either literal string or string held in a register/variable. Destination operand is always register. XORs all characters against target string characters starting with beginning chars. Below is an example.

          	DRX = "dogs"
          	TRX = "shadow"
          	
          	XOR TRX, DRX

    TRX would become \x17\x07\x06\x17ow
        MOV - Simply copies the string from a source operand to the destination operand, the source string operand can be either literal or in another register as a variable.
        REVERSE - This only takes one operand, and simply reverses the string. ie: if DRX holds "hotdog" then "REVERSE DRX" turns DRX into "godtoh". The operand for this can only be a register.

What we need We need an emulator that can execute the code in the attached file in order to decrypt this string...

GED\x03hG\x15&Ka =;\x0c\x1a31o*5M

If you successfully develop an emulator for this assembly and initialize TRX with this string, execution should yield a final result in the TRX register.

## Solution ##

*The input1 variable contains the contents of the 'Crypto.asm' input file.

```
input1 = '''MOV DRX "LemonS"
XOR TRX DRX
MOV DRX "caviar"
REVERSE DRX
XOR TRX DRX
REVERSE TRX
MOV DRX "vaniLla"
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
REVERSE TRX
MOV DRX "tortillas"
XOR TRX DRX
MOV DRX "applEs"
XOR TRX DRX
MOV DRX "miLK"
REVERSE DRX
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
REVERSE TRX
REVERSE TRX
REVERSE TRX
XOR DRX DRX
XOR TRX DRX
MOV DRX "OaTmeAL"
XOR TRX DRX
REVERSE TRX
REVERSE TRX
REVERSE TRX
XOR DRX DRX
XOR TRX DRX
MOV DRX "cereal"
XOR TRX DRX
MOV DRX "ICE"
REVERSE DRX
XOR TRX DRX
MOV DRX "cHerries"
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
REVERSE TRX
MOV DRX "salmon"
XOR TRX DRX
MOV DRX "chicken"
XOR TRX DRX
MOV DRX "Grapes"
REVERSE DRX
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
REVERSE TRX
MOV DRX "caviar"
REVERSE DRX
XOR TRX DRX
REVERSE TRX
MOV DRX "vaniLla"
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
MOV DRX TRX
MOV TRX "HonEyWheat"
XOR DRX TRX
MOV TRX DRX
MOV DRX "HamBurgerBuns"
REVERSE DRX
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
REVERSE TRX
REVERSE TRX
REVERSE TRX
XOR DRX DRX
XOR TRX DRX
MOV DRX "IceCUBES"
XOR TRX DRX
MOV DRX "BuTTeR"
XOR TRX DRX
REVERSE TRX
XOR TRX DRX
REVERSE TRX
MOV DRX "CaRoTs"
XOR TRX DRX
MOV DRX "strawBerries"
XOR TRX DRX'''

def xor_two_str(a,b):
    xored = []
    for i in range(min(len(a), len(b))):
        xored_value = ord(a[i]) ^ ord(b[i])
        xored.append(chr(xored_value))
    if len(a) < len(b):
        return ''.join(xored) + (b[len(a):])
    else:
        return ''.join(xored) + (a[len(b):])

def emulate(instructions):
    DRX = ""
    TRX = "GED\x03hG\x15&Ka =;\x0c\x1a31o*5M"
    instructions = instructions.split('\n');
    for i in instructions:
        i = i.split(' ')
        # DEBUGGING
        # print(i)
        if i[0] == "XOR":
            if i[1] == "DRX":
                if i[2] == "TRX":
                    DRX = xor_two_str(DRX,TRX)
                else:
                    DRX = xor_two_str(DRX,DRX)
            else:
                TRX = xor_two_str(TRX,DRX)
        elif i[0] == "MOV":
            if i[1] == "DRX":
                if i[2] == "TRX":
                    DRX = TRX
                else:
                    DRX = i[2][1:-1]
            else:
                if i[2] == "DRX":
                    TRX = DRX
                else:
                    TRX = i[2][1:-1]
        elif i[0] == "REVERSE":
            if i[1] == "DRX":
                DRX = DRX[::-1]
            else:
                TRX = TRX[::-1]
        # DEBUGGING
        # print("DRX = \"%s\" , length = %d"%(DRX, len(DRX)))
        # print("TRX = \"%s\" , length = %d"%(TRX, len(TRX)))
    return TRX

# DEBUGGING
# input2 = '''MOV DRX "dogs" 
# MOV TRX "shadow"
# XOR TRX DRX
# MOV DRX "caviar"
# REVERSE DRX
# XOR TRX DRX
# REVERSE TRX
# MOV DRX "vaniLla"'''

print(emulate(input1))
```

When we run `python3 we_need_an_emulator.py`, the output is:

    flag{N1ce_Emul8tor!1}
