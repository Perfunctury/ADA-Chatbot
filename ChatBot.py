"""## Copyright (C) 2022 Stephen Schertz
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Author: Stephen <>
## Created: 2022-03-17"""

# declaring variables
A = " A) Poster help?"
# if A is chosen by the user, then AA will output
AA = "Great. Which poster would you like help with: "
B = " B) NFT help?"
# if B is chosen by the user, then BB will output
BB = "Great. Which NFT would you like help with?"
C = " C) Commission help?"
# if C is chosen by the user, then CC will output
CC = "Great. Which commission service would like help with"
D = " D) General help?"
# if C is chosen by the user, then generalHelp will output
generalHelp = "Can you please describe the help you are seeking in further detail?"

# Currently unused variables.
# P1 = "Poster One is a great choice."
# O2 = "Poster Two is a fantastic choice."
# U3 = "Poster Three is a excellent choice."

# declaring list for user input choices and chatbot output responses.
choices = [A, B, C, D]
# answers = [AA, BB, CC, D] # has not been called yet

posters = ["Poster One is a great choice. How may I help you with Poster one.\n "
           "Perhaps do you need help with a specific size such as: \n A",
           "Poster Two is a fantastic choice. How may I help you with Poster Two.\n "
           "Perhaps do you need help with a specific size such as: \n ",
           "Poster Three is a excellent choice. How may I help you with Poster Three.\n "
           "Perhaps do you need help with a specific size such as: \n "]

arr = [" 1) poster ",
       " 2) poster ",
       " 3) poster "]

posterSize = [" 1) 8 x 10 ",
              " 2) 10 x 10 ",
              " 3) 12 x 12 ",
              " 4) 16 x 16 ",
              " 5) 24 x 24 "]

frameColor = ["Black", "White"]

nft = ["NFT 1 is a great choice. How may I help you with NFT one.",
       "NFT 2 is a fantastic choice. How may I help you with NFT Two.",
       "NFT 3 is a excellent choice. How may I help you with NFT Three."]

services = ["3D-Rendering", "Interior 3D-Rendering", "3D animation"]

nftChoices = [" 1) nft ",
              " 2) nft ",
              " 3) nft "]


print("Hello thank you for contacting us at HQA. My name is Ada, a chat bot.\n" "Created by our very own Stephen.\n" "Below are our current on-going sales.")
print("Black Members Hoodie 20% off"
      " Premium Polo 15% off")
print()  # this print statement is to add a space between output and user input

# this while True checks the initial choice from the user.
# moves onto next sequence in while loop based on choice from the user
# print("Type: 'done' when you are finished chatting")
# Adone = "done"
i = input("Do you need help with: \n" + str(choices) + "\n A, B, C, D \n")
while i != (A, B, C, D):
    # i = input()
    print()
    # Sequence that occurs when the user choice is A
    if i == "A":
        print(AA)
        with open('PosterOptions') as f:
            contents = f.read()
            print(arr)
            i = input()
            i = int(i)  # converts I into an int
            if i == 1:
                print(posters[0] + str(posterSize))
                i = input()
                while i in posterSize[0 < 5]:
                    continue
                string = "Sounds perfect. I will contact Stephen to assist you with Poster 1. \nSize: "
                print(string, i)
            elif i == 2:
                print(posters[1] + str(posterSize))
                i = input()
                while i in posterSize[0 < 5]:
                    continue
                string = "Sounds perfect. I will contact Stephen to assist you with Poster 2. \nSize: "
                print(string, i)
            elif i == 3:
                print(posters[2] + str(posterSize))
                i = input()
                while i in posterSize[0 < 5]:
                    continue
                string = "Sounds perfect. I will contact Stephen to assist you with Poster 3. \nSize: "
                print(string, i)
    # Sequence that occurs when the user choice is B
    elif i == "B":
        print(BB, nftChoices)
        i = input()
        i = int(i)
        if i > 1:
            print(nft[1])
        elif i < 2:
            print(nft[0])
        elif i == 3:
            print(nft[2])
    # Sequence that occurs when the user choice is C
    elif i == "C":
        print(CC, services)
        i = input()
        if i == services[0]:
            print("Do you have more information regarding your project? ")
        elif i == services[1]:
            print("Do you have a floor plan ready?")
        elif i == services[2]:
            print("How long does your 3D animation need to be.")
    # Sequence that occurs when the user choice is D
    elif i == "D":
        print(D)
    break
print(" ")

print("When you're finished chatting type: " + "done \n")
info = input("Is there something else I can help you with? ")
done = "done"
while info != "done":
    print("you: ", info)
    info = input("Is there something else I can help you with? ")
#
# def a(i):
#     i = input()
#     if i == "A":
#         print(AA)
#         with open('PosterOptions') as f:
#             contents = f.read()
#             print(arr)
#             i = input()
#             i = int(i)  # converts I into an int
#             if i == 1:
#                 print(posters[0])
#             elif i == 2:
#                 print(posters[1])
#             elif i == 3:
#                 print(posters[2])
#     return
#
# def b(i):
#     i = input()
#     if i == "B":
#         print(BB, nftchoices)
#         i = int(i)
#         if i > 1:
#             print(nft[1])
#         elif i < 2:
#             print(nft[0])
#         elif i == 3:
#             print(nft[2])
#     return
#
# def choicea(i):
#     i = input()
#     if i == "C":
#         print(CC, services)
#         #i = input()
#         if i == services[0]:
#             print("Do you have more information regarding your project? ")
#         elif i == services[1]:
#             print("Do you have a floor plan ready?")
#         elif i == services[2]:
#             print("How long does your 3D animation need to be.")
#     return


# def search(arr, x):
#       for i in range(len(arr)):
#             if arr[i] == x:
#                   return i
#
#       return -1

# # While True: loop for choice A
# # this while loop iterates through conditions of choice A
# while True:
#     i = input()
#     if i == "1":
#         print(posters[0])
#     elif i == "2":
#         print(posters[1])
#     elif i == "3":
#         print(posters[2])
#     break
#
# # While True: loop for choice B
# # this while loop iterates through conditions of choice A
# while True:
#       i = input()
#       print(nft)
#       if i == "1":
#             print(nft[0])
#       elif i == "2":
#             print(nft[1])
#       elif i == "3":
#             print(nft[2])
#       break
#
# # While True: loop for choice C
# # this while loop iterates through conditions of choice A
# while True:
#     i = input()
#     if i == "1":
#         print(posters[0])
#     elif i == "2":
#         print(posters[1])
#     elif i == "3":
#         print(posters[2])
#     break
#
# # While True: loop for choice D
# # this while loop iterates through conditions of choice A
# while True:
#     i = input()
#     if i == "1":
#         print(P1)
#     elif i == "2":
#         print(O2)
#     elif i == "3":
#         print(U3)
#     break
