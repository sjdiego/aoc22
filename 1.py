def get_kcal_per_elf():
    elfs = {}
    i = 1

    with open("input-1.txt", "r") as file:
        for line in file:
            if not i in elfs:
                elfs[i] = 0

            if line.strip().isnumeric():
                elfs[i] += int(line)
            else:
                i += 1

    return elfs

def get_top_elfs(elfs, top):
    total_kcal = 0

    for rank in range(1, 4):
        top_elf = 0
        top_val = 0
        items = elfs.items()

        for elf, kcal in items:
            if kcal > top_val:
                top_elf = elf
                top_val = kcal

        print(f"Top {rank} elf is: {top_elf} with {top_val} kcal")

        del elfs[top_elf]
        total_kcal += top_val

    print(f"Total carried kcal are: {total_kcal}")

def main():
    elfs = get_kcal_per_elf()
    get_top_elfs(elfs, 3)


main()
