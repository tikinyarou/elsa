hoge = open('test.gcode', 'r+')

with hoge as fd:
    contents = fd.readlines()
    if 'Z' in contents[-1]:  # Handle last line to prevent IndexError
        contents.append('G94\n')
    else:
        for index, line in enumerate(contents):
            if 'Z' in line and 'G94' not in contents[index + 1]:
                contents.insert(index + 1, 'G94\n')
                break
    fd.seek(0)
    fd.writelines(contents)
