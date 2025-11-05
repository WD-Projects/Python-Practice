def generate(n):
    table = ""
    for j in range(1, 11):
        table  += f"{n} * {j} = {n * j}\n"

    with open(f"file/Table/tables/table_{n}.txt", "w") as f:
        f.write(table)

    return

for i in range(2,21):
    generate(i)    
