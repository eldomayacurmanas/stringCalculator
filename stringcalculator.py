from logging import raiseExceptions

def resultadode(stringFormula): 
    
    if stringFormula[:6] == "sumtry":
        command, indicesup, indice, formula = stringFormula.split(sep=",", maxsplit=3)
        return sumatoria(int(indicesup), indice, formula)
    
    preparenthesis = ""
    postparenthesis = ""
    if "(" in stringFormula:
        if ")" in stringFormula:
            if stringFormula.split("(") != 1:
                preparenthesis = stringFormula.split("(")[0]
            if stringFormula.split(")") != 1:
                postparenthesis = stringFormula.split(")")[-1]
            parenthesis = stringFormula[len(preparenthesis)+1:-(len(postparenthesis)+1)]
            returnvalue= resultadode(preparenthesis + str(resultadode(parenthesis)) + postparenthesis)
            #print(f"preprnt: '{preparenthesis}' parnt: '{str(resultadode(parenthesis))}' postprnt: '{postparenthesis}' returnvalue: '{returnvalue}'")
            return returnvalue
        else:
            raiseExceptions(f"invalid amount of parenthesis in {stringFormula}")

    if stringFormula[:4] == "raiz":
        splitted = stringFormula.split(sep=",", maxsplit=2)
        if len(splitted) == 3:
            command, indice, radicando = splitted
        elif len(splitted) == 2:
            command, radicando = splitted
            indice = 2
        else:
            print(f"syntaxis error in {stringFormula} returning 0")
            return 0
        #print(f"radicando es '{radicando}' e indice es '{indice}'")
        return round(resultadode(radicando) ** resultadode(f"1/{indice}"),12)

    calculos = ["+", "-", "x", "/","^"]
    for calculo in calculos:
        ecuation = stringFormula.split(sep= calculo, maxsplit=1)
        if len(ecuation) != 1:

            if calculo == "+":
                return resultadode(ecuation[0]) + resultadode(ecuation[1])
            if calculo == "-":
                return resultadode(ecuation[0]) - resultadode(ecuation[1].replace("-","+"))
            if calculo == "x":
                return resultadode(ecuation[0]) * resultadode(ecuation[1])
            if calculo == "/":
                return resultadode(ecuation[0]) / resultadode(ecuation[1])
            if calculo =="^":
                return resultadode(ecuation[0]) ** resultadode(ecuation[1])    
    try:
        returnvalue = round(float(stringFormula),10)
        return returnvalue
    except:
        print(f"wrong sintaxis in {stringFormula} returning 0")
        return 0


def sumatoria(indicesup, indice, formula):
    resultado = 0

    for i in range(indicesup+1):
        formulai = formula.replace(indice, str(i))

        resultado += resultadode(formulai)
    return resultado

    



