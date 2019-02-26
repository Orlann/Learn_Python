import random, re, itertools, string


def write_to_file(file, input_list):
    for item in input_list:
        file.write(str(item))


def random_list():
    numbers_list = list()
    random_length_of_list = random.randint(20, 100)
    for i in range(random_length_of_list):
        numbers_list.append(random.randint(0,9))
    return numbers_list


def random_char_list():
    char_list = list()
    random_length_of_list = random.randint(20, 100)
    for i in range(random_length_of_list):
        char_list.append(random.choice(string.ascii_letters))
    return char_list


def main():
    # write data in file A
    with open("fileA.txt", "w") as file_a_write:
        random_lines_number = random.randint(10, 20)
        for i in range(random_lines_number):
            list_for_file_1 = random_list()
            list_for_file_1[0] = "A "
            write_to_file(file_a_write, list_for_file_1)
            file_a_write.write("\n")
    file_a_write.close()              # I`m not sure whether it is necessary while using "with" statement

    # write data in file B
    with open("fileB.txt", "w") as file_b_write:
        random_list_length = random.randint(10, 20)
        for i in range(random_list_length):
            list_for_file2 = random_char_list()
            list_for_file2[0] = "B "
            write_to_file(file_b_write, list_for_file2)
            file_b_write.write("\n")
        file_b_write.close()

    # merge files
    try:
        with open("fileA.txt", "r") as file_a:
            with open("fileB.txt", "r") as file_b:
                with open("fileC.txt", "w") as result_file:
                    line_from_file_a = file_a.readlines()   # read lines from "fileA" to list
                    line_from_file_b = file_b.readlines()   # read lines from "fileB" to list
                    # combine two lists as corteges with size of the longest list and write them to resulted file
                    for line1, line2 in itertools.zip_longest(line_from_file_a, line_from_file_b):
                        result_file.write("{}\n{}\n".format(str(line1).rstrip(), str(line2).rstrip()))
                result_file.close()     # I`m not sure whether it is necessary while using "with" statement
            file_b.close()              # I`m not sure whether it is necessary while using "with" statement
        file_a.close()                  # I`m not sure whether it is necessary while using "with" statement
        # next part removes "None" and double paragraph marks that appear in places where the shortest list has no item
        # while the longest still has
        with open("fileC.txt", "r") as result_file:
            text_from_file = result_file.read()
            new_text = text_from_file.replace("None", "")
            pattern = r"\n{2,}"
            new_text = re.sub(pattern, "\n", new_text)
        result_file.close()                  # I`m not sure whether it is necessary while using "with" statement
        with open("fileC.txt", "w") as result_file:
            result_file.write(new_text)
        result_file.close()                  # I`m not sure whether it is necessary while using "with" statement
    except FileNotFoundError:
        print("Some problem with files. Check them.")


if __name__ == "__main__":
    main()
