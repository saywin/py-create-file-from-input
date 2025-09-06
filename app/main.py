def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"

    with open(name_file, "a") as file:
        while True:
            line_content = input("Enter new line of content: ")
            if line_content == "stop":
                break
            file.write(line_content + "\n")


if __name__ == "__main__":
    main()
