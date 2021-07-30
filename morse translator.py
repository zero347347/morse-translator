# We need to use input
# create a list of translate by using .replace
# print output
# we need to define our function
input_content = []
input_content = input("Enter your text:")
input_content = input_content.lower()
code = input_content


def convert_to_morse(code):
    code = code.replace(" ", "/ ")
    code = code.replace(",", "--..--")
    code = code.replace(".", ".-.-.-")
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")
# now we can put in the consideration of alphabets data
# remember that we have both lowercase and uppercase
    code = code.replace("a", ".- ")
    code = code.replace("b", "-... ")
    code = code.replace("c", "-.-. ")
    code = code.replace("d", "-.. ")
    code = code.replace("e", ". ")
    code = code.replace("f", "..-. ")
    code = code.replace("g", "--. ")
    code = code.replace("h", ".... ")
    code = code.replace("i", ".. ")
    code = code.replace("j", ".--- ")
    code = code.replace("k", "-.- ")
    code = code.replace("l", ".-.. ")
    code = code.replace("m", "-- ")
    code = code.replace("n", "-. ")
    code = code.replace("o", "--- ")
    code = code.replace("p", ".--. ")
    code = code.replace("q", "--.- ")
    code = code.replace("r", ".-. ")
    code = code.replace("s", "... ")
    code = code.replace("t", "- ")
    code = code.replace("u", "..- ")
    code = code.replace("v", "...- ")
    code = code.replace("w", ".-- ")
    code = code.replace("x", "-..- ")
    code = code.replace("y", "-.-- ")
    code = code.replace("z", "--.. ")

    return code


morse_output = convert_to_morse(input_content)
print(morse_output)
