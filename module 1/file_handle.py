#with open("batch.txt", "w") as f:
 #   f.write("Python is a programming language.\n")
  #  f.write("File handling is very important")

    # #Read the entire batch.txt file
    # with open("batch.txt", "r") as f:
    #     content = f.read()
    #     print(content) 

# with open("batch.txt", "r") as f:
#     for line in f:
#         print(line.strip())     

# #Read all lines into a list
# with open("batch.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

# #append new sentence in batch.txt file
# with open("batch.txt", "a") as f:
#     f.write("\nHello my name is Amritanshu Shukla")

# question 1 of file handling

# with open("diary.txt", "w") as file:
#     file.write("Today I learned Python file handling.\n")
#     file.write("I practiced reading and writing files.\n")
#     file.write("Python programming is interesting.\n")

# # Read and print the file
# with open("diary.txt", "r") as file:
#     content = file.read()
#     print("Contents of diary.txt:")
#     print(content)


# WAP to count the number of lines, words, and characters in a text file

with open("diary.txt", "r") as file:
    content = file.read()

# Count characters
characters = len(content)

# Count words
words = len(content.split())

# Count lines
lines = len(content.splitlines())

# Display the results
print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)
