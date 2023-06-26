# Build our RNG storage from the bytes recovered from the flash.
def build_triplets():
    triplets = []
    triplets_bytes = bytes.fromhex("02 05 0D FF FF 00 00 AD 8B 00 00 05 0B 0B FF FF 00 00 0D F0 00 00 0E 0D 0F FF FF FF FF BE BA FE CA")

    for i in range(3):
        triplet_bytes = triplets_bytes[i*11:i*11+11]
        
        shifts = [triplet_bytes[0], triplet_bytes[1], triplet_bytes[2]]
        mask = triplet_bytes[3] + (triplet_bytes[4] << 8) + (triplet_bytes[5] << 16) + (triplet_bytes[6] << 24)
        gen = triplet_bytes[7] + (triplet_bytes[8] << 8) + (triplet_bytes[9] << 16) + (triplet_bytes[10] << 24)
        
        triplets.append([shifts, mask, gen])
    
    return triplets

# Get the next bit for a given triplet
def triplet_bit(triplet):
    shifts, mask, gen = triplet
    # shifts = Z0-2
    # mask = Z3-6
    # gen = Z7-10
    
    next_gen = gen
    
    shift = shifts[2]
    next_gen = ((next_gen >> shift) ^ next_gen) & mask
    
    shift = shifts[0]
    next_gen = ((next_gen >> shift) ^ next_gen) & mask
    
    shift = shifts[1]
    next_gen = ((next_gen << shift) ^ next_gen) & mask
    
    triplet[2] = next_gen
    
    return next_gen & 1

# Get the next bit for the three triplets
def next_bit(triplets):    
    a = triplet_bit(triplets[2])
    b = triplet_bit(triplets[1])
    c = triplet_bit(triplets[0])
    
    # something_something
    s = (a & b) | (b & c) | (a & c)
    
    return s

# Get the next byte for the three triplets
def next_byte(triplets):
    s = 0
    for i in range(8):
        s = s << 1
        s = s | next_bit(triplets)
    return s

# Set enc to integer values of the bytes in the cipher
enc = "JIGGYCIPHER{a1557d3801d7723f3d385111d85cd125625cc260ba76d3051a5de6ff24786b8fc70c1659aa4c41b9151c8eef70d438515a6642562ab9f0403f276ba556a7429829433d2572484f2585719d468964832ab1a258521f568165c3ab1bead146ecd2de65a5d812b53ca5c168473bac895d4a8bc37390f860b11e6a6eb442c249180a9c337285455ab098d47b7264ec42bed7688d59dcdfddcf3d0de674356cbee22547e087c63be52013dc319600c4a4859788ab87349c6c81ea9598127f87093c148c1d3e94edea50132f324eaf5cc88b63b8fac20cf6}"
enc = bytes.fromhex(enc[12:-1])
enc = list(enc)
## print(enc)
## [161, 85, 125, 56, ... ]

# Build the triplets (the seed) of the RNG
triplets = build_triplets()

# Generate the RNG nums, one for each encrypted byte
rng_nums = [next_byte(triplets) for i in range(len(enc))]
## print(rng_nums)
## [128, 81, 12, 36, ... ]
## These numbers were compared to the output in the emulator to ensure accuracy.

enc_1 = [byte for index, byte in enumerate(enc) if index % 3 == 0] # [161, 56, ...]
enc_2 = [byte for index, byte in enumerate(enc) if index % 3 == 1] # [85, ... ]
enc_3 = [byte for index, byte in enumerate(enc) if index % 3 == 2] # [125, ... ]

rng_nums_1 = [byte for index, byte in enumerate(rng_nums) if index % 3 == 0] # [128, 36, ... ]
rng_nums_2 = [byte for index, byte in enumerate(rng_nums) if index % 3 == 1] # [ 81, ... ]
rng_nums_3 = [byte for index, byte in enumerate(rng_nums) if index % 3 == 2] # [ 12, ... ]

# Recover characters from enc_3
# *(Y+10) = enc_3_byte ^ random_next()

dec_3 = []

for i in range(len(enc_3)):
    d = enc_3[i] ^ rng_nums_3[i]
    dec_3.append(d)

## print("".join([chr(x) for x in dec_3]))
## qo:Gvrmnso h nutilWrd o er inso ls n te,Icm rmCbrpc,tenwhm fM~jb;hl{~ne

# Recover characters from enc_2
# *(Y+5) = *(Y+5) ^ *(Y+10)
# *(Y+11) = enc_2_byte ^ *(Y+5) ^ random_next()

dec_2 = []
key = 0

for i in range(len(enc_2)):
    key ^= dec_3[i]
    d = enc_2[i] ^ key ^ rng_nums_2[i]
    dec_2.append(d)

## print("".join([chr(x) for x in dec_2]))
## ut{oenet fteIdsra ol,yuwaygat ffehadsel  oefo yesae h e oeo i~p}ca:~edr

# Recover characters from enc_1
# **(Y+48,47) = enc_1_byte ^ *(Y+11) ^ random_next()
dec_1 = []

for i in range(len(enc_1)):
    d = enc_1[i] ^ dec_2[i] ^ rng_nums_1[i]
    dec_1.append(d)

## print("".join([chr(x) for x in dec_1]))
## This is an Amazon(.ca?) gift card. Your claim code is ZBUH-3PYCC6-DKAG.

# Put together strings
input_string_1 = "".join([chr(x) + chr(y) for x,y in zip(dec_3, dec_2)])
input_string_2 = "".join([chr(x) for x in dec_1])

print(input_string_1)
print(input_string_2)