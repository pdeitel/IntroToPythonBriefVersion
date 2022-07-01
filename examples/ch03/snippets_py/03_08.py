# Section 3.8 snippets

for character in 'Programming':
    print(character, end='  ')
    
# Function print’s sep Keyword Argument 
print(10, 20, 30, sep=', ')

# 3.8.1 Iterables, Lists and Iterators
total = 0

for number in [2, -3, 0, 17, 9]:
    total = total + number
    
total

# 3.8.2 Built-In range Function and Generators
for counter in range(10):
    print(counter, end=' ')
    

##########################################################################
# (C) Copyright 2022 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
