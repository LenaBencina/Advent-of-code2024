import re

with open("input_day3.txt", 'r') as f:
    memory = f.read()

# part 1
nums = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)

result = 0
for pair in nums:
    result += int(pair[0]) * int(pair[1])

print(result)

# part 2
nums2 = re.findall("do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory)

result2 = 0
enabled = True
for operation in nums2:
    if operation == "do()":
        enabled = True
    elif operation == "don't()":
        enabled = False
    elif enabled and "mul" in operation:
        n1, n2 = re.findall('\d{1,3}', operation)
        result2 += int(n1) * int(n2)
print(result2)


# failed attempt
# nums2 = re.findall("(do\(\)|don't\(\))?.?mul\((\d{1,3}),(\d{1,3})\)", memory)
# print(nums2)
# i = 0
# result2 = 0
# enabled = True
# for i in range(len(nums2)):
#     operation = nums2[i]
#     if i < len(nums2) - 1:
#         operation_next = nums2[i+1]
#     if enabled:
#         result2 += int(operation[1]) * int(operation[2])
#     enabled = True if operation_next[0] == "do()" else False
#     i += 1
# print(result2)
