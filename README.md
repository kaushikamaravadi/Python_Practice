# Python_Practice

# Python-Enthusiasts

##Summary

* This is a repository for python enthusiasts, which covers algorithms, specific problems for algorithms enthusiasts to solve and project Euler.
* All problems and algorithms are in pure python and are well documented.
* All Data Structures and problems should have documentation and tests.


##Table of Contents

* Data Structures
  * Linked List
  * Queue
  * Queue using Linked List
  * Stack
  * Stack using Linked List

* Project Euler
>  Project Euler exists to encourage, challenge, and develop the skills and enjoyment of anyone with an interest in the fascinating world of mathematics.
  * Project Euler was started by Colin Hughes (a.k.a. euler) in October 2001 as a subsection on mathschallenge.net. the membership has continued to grow and Project Euler moved to its own domain in 2006.
  * I solve Project Euler problems to practice and extend my math and programming skills, all while having fun at the same time.
  * Warmup and Transcend lists all of my Project Euler solution code.All solutions to project euler problems are in pure python. 
  * There were some problems which are really interesting. 

###Project Euler Problem 38: 
Take the number 192 and multiply it by each of 1, 2, and 3:

				     192 * 1 = 192
			         192 * 2 = 284
				     192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3). 
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

#####Python Code:
        for i in range(1, n):
        mul = ""
        # noinspection PyRedeclaration
        first = 1
        while len(mul) < 9:
            mul = mul + str(i * first)
            first = first + 1

        if len(mul) == 9 and len(set(mul)) == 9 and ('0' not in mul):
            if int(mul) > largest:
                largest = int(mul)

For complete code, please see Transcend Pandigital.py




 

