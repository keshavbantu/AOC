gamma_rate=''
epsilon_rate=''
bit0_dict={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
bit1_dict={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

with open('input.txt','r') as f:
    bit_line=f.read().split('\n')
    #keys of dict are 1 to 12
    #dict[key]=bit
    for i in range(0,len(bit_line)-1):
        j=1
        while(j<13):
            if (bit_line[i][j-1]) == '1':
                bit1_dict[j]=bit1_dict[j]+1
            if (bit_line[i][j-1]) == '0':
                bit0_dict[j]=bit0_dict[j]+1
            j+=1
       
#gamma = most common
def gamma():
    global gamma_rate
    for k in range(1,12):
        temp=max(bit0_dict[k],bit1_dict[k])
        if temp == bit0_dict[k]:
            s='0'
        if temp == bit1_dict[k]:
            s='1'
        gamma_rate=gamma_rate+s 

        
#epsilon = least common
def epsilon():
    global epsilon_rate
    for k in range(1,12):
        temp=min(bit0_dict[k],bit1_dict[k])
        if temp == bit0_dict[k]:
            s='0'
        if temp == bit1_dict[k]:
            s='1'
        epsilon_rate=epsilon_rate+s
gamma()
epsilon()
#converted octal bits to binary by hand 

'''
with open("input.txt", "r") as f:
    lines = f.readlines()

N = len(lines[0].strip())  # Number of digits in the base-2 numbers
data = [int(line, base=2) for line in lines]


# Part 1
bits = [2 ** n for n in range(N)]
gamma = sum(bit for bit in bits if sum(datum & bit for datum in data) // bit >= len(data) / 2)
epsilon = sum(bit for bit in bits if sum(datum & bit for datum in data) // bit <= len(data) / 2)
print(epsilon * gamma)


# Part 2
def filter_data_bitwise(data, filter_by_most_common=True):
    filtered = [x for x in data]
    for bit in reversed(bits):
        ratio = sum(1 for num in filtered if num & bit) / len(filtered)
        wanted_bit_value = bit * int((ratio >= 0.5) == filter_by_most_common)
        filtered = [x for x in filtered if x & bit == wanted_bit_value]
        if len(filtered) == 1:
            break
    return filtered

filtered_by_most_common = filter_data_bitwise(data)
filtered_by_least_common = filter_data_bitwise(data, filter_by_most_common=False)
print(filtered_by_most_common[0] * filtered_by_least_common[0])
'''
