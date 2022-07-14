# with open("files.txt", "w") as f:
#     for i in range(1,7):
#         f.writelines(f"line{i}\n")

with open("files.txt") as f:
    lines = f.readlines()
    print(lines)

with open("files2.txt", "w") as f:
    for i in lines:
        if "5" in i:
            continue
        f.write(i)