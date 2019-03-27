def main():

    input_file = open("input_10k.txt")

    i, a, s = 0, 0, 0
    for l in input_file:
        i += 1
        dst = l.strip()
        if dst.startswith("bcb_"):
            a += 1
            print(dst)
        else:
            s += 1
            # print(dst)

    # print(i)
    # print(a)
    # print(s)



if __name__ == '__main__':
    main()