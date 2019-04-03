file = open("processed_code.txt", "w")


with open("to_process_code.txt") as gcode_file_original:
    contents = gcode_file_original.readlines()
    for line in contents:
        line = str(line)
        get = line.find("Z")

        if get != -1:
            line = "\n" + "G94" + "\n" + line + "\n" + "G93" + "\n"
            print(line)
            file.write(line)
        else:
            line = line
            print(line)
            file.write(line)
