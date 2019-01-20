def increment_operation(file_path):
    with open(file_path, "r") as f:
        data = int(f.read())
        #data = int(data)
        #value = int(data)
        value = data
        data += 1
    f.close()
    with open(file_path, "w") as f:
        f.write(str(data))
    f.close()
    return value

print increment_operation("C:\\New folder\\increment.txt")
