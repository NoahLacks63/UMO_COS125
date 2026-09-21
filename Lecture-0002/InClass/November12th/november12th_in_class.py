# opens the file so actions can be taken
text_file = open("writeIt.txt", "w")
# modes: (r)ead, (w)rite, (a)ppend, (x) throws error if file already exists

text_file.write("Hullo\n")
text_file.write("Greetings!!!\n")

# closes the file so no more actions can be taken
text_file.close()

t_file = open("writeIt.txt", "r")

text = t_file.read()
