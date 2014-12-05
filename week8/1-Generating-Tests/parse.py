def is_empty_line(line):
    return len(line.strip()) != 0


def lines(textContents):
    return textContents.split("\n")


def unlines(lineData):
    return "\n".join(lineData)


def get_file(file):
    return open(file).read()


def compose(f, g):
    return lambda x: f(g(x))


def main():
    contents = get_file("test.dsl")

    print(compose(unlines, lines)(contents))

    # contets = lines(get_file("test.dsl"))
    # noEmptyLines = list(filter(is_empty_line, contets))
    # print(unlines(noEmptyLines))


if __name__ == '__main__':
    main()
