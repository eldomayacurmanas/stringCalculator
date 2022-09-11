from stringcalculator import resultadode

examples = ["5+7", "5-2", "2x3", "10/2", "3^3",
            "raiz,3,125", "raiz,9", "(5)", "5+2x10", "(5+2)x10/2",
            "sumtry, 5,X,(X^2)", 
            "raiz,((sumtry,4,X,(sumtry,X,J,(sumtry,J,K,K)))-10)"]
for example in examples:
    print(f'passing "{example}" returns {resultadode(example)}')
