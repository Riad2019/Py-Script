# import spelling as ss;

dv_element = document.querySelector("#plot")
with open("word2.txt") as f:
    for line in f:
        li_element = document.createElement("li")
        li_element.innerText = line
        dv_element.appendChild(li_element)
    # contents = z.read()
#print(z.read())
# checker = ss.SpellChecker("./words.txt")
# misspelled_word = "gim"
# print(checker.check(misspelled_word))