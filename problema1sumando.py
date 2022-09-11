# problema OMA Regional 2022 N3 P1:https://omaforos.com.ar/viewtopic.php?f=9&t=8115

#Una sucesión creciente de números naturales se dice impar-par si cada término en una posición impar es impar y cada término en una posición par es par.
#  Todas las sucesiones crecientes impar-par cuyos términos son menores o iguales que 4 son: {1},{3},{1,2},{1,4},{3,4},{1,2,3} y {1,2,3,4}.
# Determinar la cantidad de sucesiones crecientes impar-par cuyos términos son menores o iguales que 10.
# Nota. Una sucesión se dice creciente si cada término es mayor que el término que lo precede.


from stringcalculator import resultadode


sumatotal = 0

sumatotal += 5 # con 1 elemento

sumatotal += resultadode("sumtry,5,X,X") #con 2 elementos

sumatotal += resultadode("sumtry,4,X,(sumtry,X,J,J)") # con 3 elementos

sumatotal += resultadode("sumtry,4,X,(sumtry,X,J,(sumtry,J,K,K))")# con 4 elementos

sumatotal += resultadode("sumtry,3,X,(sumtry,X,J,(sumtry,J,K,(sumtry,K,M,M)))")# con 5 elementos

sumatotal += resultadode("sumtry,3,X,(sumtry,X,J,(sumtry,J,K,(sumtry,K,M,(sumtry,M,N,N))))")# con 6 elementos

sumatotal += resultadode("sumtry,2,X,(sumtry,X,J,(sumtry,J,K,(sumtry,K,M,(sumtry,M,N,(sumtry,N,O,O)))))")# con 7 elementos

sumatotal += resultadode("sumtry,2,X,(sumtry,X,J,(sumtry,J,K,(sumtry,K,M,(sumtry,M,N,(sumtry,N,O,(sumtry,O,P,P))))))")# con 7 elementos

sumatotal += 1 # con 9 elementos

sumatotal += 1 # con 10 elementos


print(f"la suma total de posibilidades es {sumatotal}")
