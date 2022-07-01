# Section 7.11 snippets
import numpy as np

numbers = np.arange(1, 6)

numbers

numbers2 = numbers.view()

numbers2

id(numbers)

id(numbers2)

numbers[1] *= 10

numbers2

numbers

numbers2[1] /= 10

numbers

numbers2

# Slice Views
numbers2 = numbers[0:3]

numbers2

id(numbers)

id(numbers2)

numbers2[3]

numbers[1] /= 10

numbers

numbers2


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
