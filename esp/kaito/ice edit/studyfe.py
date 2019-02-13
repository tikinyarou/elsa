id = open('test.gcode', 'r+')

text = ['G94','G93',';']

# with id as f:
#     lines = f.readlines()
# #     f.write('G93\n')
#     print(lines)
#     if 'Z' in lines:
#         print(lines)

# id = [i for i, line in enumerate(lines) if 'Z' in line]
#
tester = [i for i, line in enumerate(id) if 'Z' in line]
print(tester)

# print(sum(1 for i in id))
