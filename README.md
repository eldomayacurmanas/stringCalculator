# stringCalculator
calculates the value of a formula passed in a string way

## way of use
the resultadode function takes a string as a parameter, and if its a formula then returns the result of it.
### the syntaxis used is:
- for adding: just pass an "a+b" string. e.g: passing "5+7" returns 12.
- for substracting: pass "a-b" string. e.g: passing "5-2" returns 3.
- for multiplying: pass "axb" string. e.g: passing "2x3" returns 6.
- for dividing: pass "a/b" string. e.g: passing "10/2" returns 5.
- for powering: pass "a^b" string. e.g: passing "3^3" returns 27.
- for rooting: pass "raiz,[indice], [root]" or "raiz,root"(will take 2 automaticly as indice). e.g: passing "raiz,3,125" returns 5, "raiz,9" returns 3.
- for summations: pass "sumtry, [superior indice], [inferior indice name], [formula]" string. e.g: passing "sumtry,4,X,X" returns 10.
- for a parenthesis: pass "(a)" string. e.g: passing "(5)" returns 5.

#### mixing: you can pass a mixed formula, mixing the operators from below. e.g:
- passing "5+2x10" returns 25.
- passing "(5+2)x10/2" returns 35.
- passing "sumtry, 5,X,(X^2)" returns 55.
- passing "raiz,((sumtry,4,X,(sumtry,X,J,(sumtry,J,K,K)))-10)" returns 5.

### all examples done by the program
![imagen](https://user-images.githubusercontent.com/97920368/189493645-44fd64e2-ef6e-4ea1-abaf-759c50cc9f9b.png)

## functionality
### resultadode
in this function first checks some important commands to support roots or sumatories commands, also checks if has parenthesis, 
then it's the main proccess turn;

#### calcules
first is declared a list with all the calculus operations in the correct order of priority, then iterating over that list splitting
each case by the calculus character identificator, if the string is actually splitted, it means that THAT calculus operation is in fact modifying
the formula, so calcules recursevely the left part of the split and does the indicated operation between them. the operation is indicated by the char
that makes the formula split, in each 'for' iteration that char is called "calculo", if the string is splitted it means that "calculo" is in fact the 
indicated operation.
e.g; if the calcule is "+" then adds up the resulting parts.

#### other handies
as I said before, the main process runs after checking if there are parenthesis, summations or roots, how does the program do that?:

##### summations
it checks if the first 6 characters of the formula are "sumtry"(the command for doing a sumatorie), if so it means that all the string are parts of the
summation, so the program splits the elements by the commas and calls the function sumatoria passing the summation elements.

##### parenthesis
In this part checks if there are parenthesis in the formula for giving it its adecuate priority. does this by checking if there is the char "(" in the string
if so then executes the following: checks if is there the ")" closing parenthesis. If there isn't then raises an error. If there is the ")" char then 
does the following: checks if the amount of elements of the formula splitted by "(" is different that one. If so means that there is something before the 
parenthesis so saves the very first element in a variable called "preparenthesis".
Then by the same way checks if there is something after ")". if so saves it in another variable called postparenthesis.
for saving the inner part of the parenthesis it saves the longitudes of the before and the after. the inner parenthesis is 
going to start by the longitude of the preparenthesis plus one (because the "(" is not included), and ends in the 
index negative: longitud of post parenthesis, plus one. Then so the parenthesis variable value is stringFormula[len(preparenthesis)+1:-(len(postparenthesis)+1)].
Recursevely checks the value of the inside of the parenthesis and concatenates it with the pre and post parenthesis calling, recursively again, the function
for checking the whole value, but now the inside of the parenthesis is just its resulting value.
(I had been a long period of time cracking that out)

##### roots
also checks if the first four characters are equal to "raiz"(its command). If so also means that the whole Formula is just the root, so it takes its elements
splitting in the commas. If there are three elements it means that the indice has been passed, so assigns the second element to the indice variable and the third one
to the root(the first element is now not useful because its just the command). If there are only 2 elements it emans that the indice has not been passed
so assigns the second element to the root variable and the tradicional 2 value is assigned to the idnice variable.
Now notice that rooting a root by an indice, is equal to powering that root to the opposite of that indice. Thats what the program does by powering the value
to the resultadode(f"1/{indice}")'th potency. Then returns the result.

### sumatoria
in this other function its calculed a summand defined by the parameters passed. 
#### proccess
iterating on a list of numbers that goes through 1 to indicesup's value. It replaces each number of the list with the indice name defined
in the indice's value and adds up to a total sum variable the result of the formula obtained by calling the 'resultadode' function.
Then returns the total sum.

## other files
There are also other files that shows examples of ways to use that function.

### examples.py 
this file contains the examples given in this readme file, its up to you to execute it by youtself.

### problema1sumando.py 
In this file is a real use i gave to the functions. I used it to check if my solution to a problem from a National Maths 
olimpiads https://omaforos.com.ar/viewtopic.php?f=9&t=8115 was right. I needed to do the summand of a summand of a summand.. And it was a tough work to do
by hand, and the traditional calculator does not allow you to calcule that much.





