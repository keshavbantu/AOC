with open("day2.txt", "r") as f:
    lines = f.readlines()


# Interpret movement as a complex number
# - Has direction and magnitude
# - Can be summed easily
def parse(command):
    if command.startswith("forward"):
        return int(command.split()[1])
    if command.startswith("down"):
        return int(command.split()[1]) * 1j
    if command.startswith("up"):
        return - int(command.split()[1]) * 1j
    raise Exception

data = [parse(line) for line in lines]


# Part 1
print((lambda z: z.real * z.imag)(sum(data)))


# Part 2
# The "aim" at each step can be computed first,
# and then zipped with data to take a sum:
aims = [sum(data[: i + 1]).imag for i in range(len(data))]
position = sum(z.real * (1 + 1j * aim) for z, aim in zip(data, aims))
print(position.real * position.imag)
