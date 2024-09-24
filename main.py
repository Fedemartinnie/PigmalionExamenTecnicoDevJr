#  1)Un algoritmo que resuelva el problema asumiendo que la máquina en donde va a correrse el programa tiene recursos infinitos, que el tiempo de ejecución no importa y que lo más importante es realizar el desarrollo en el menor tiempo posible.
# Función para verificar si existe el par en el array que la suma sea 'x' 
def hasPairWithSum(arr, requiredSum, i=0, j=1, sumEight=False):
    # recorro el array desde el primer elemento hasta el anteúltimo y sumo el elemento actual con cada uno de los posibles elementos
    while (i<len(arr)-1 and not sumEight):
        # recorro el array desde el segundo elemento hasta el último verificando si encontré la suma requerida
        while(j<len(arr) and not sumEight):
            # sumo el elemento actual (i) con cada uno de los siguientes elementos (j) y verifico si la suma del par es igual a la suma requerida
            sum2Elements = arr[i] + arr[j]
            if(sum2Elements == requiredSum):
                sumEight = True
            else:
                j+=1
        # incremento 'i' para pasar al siguiente elemento y ubico 'j' en la siguiente posición de 'i'
        i+=1
        j=i+1
    return sumEight



# 2) Un algoritmo que resuelva el problema asumiendo que los recursos son un bien preciado, que el tiempo de ejecución si importa y que el tiempo de desarrollo no es importante.
# Función recursiva para verificar si existe una suma de un par de numeros que sea igual a 'x' (8)
def hasPairWithSumRecursion(arr, requiredSum, sum_eight=False, i=0, j=1):
    # Caso Base: llego al último elemento del array y ya no tengo un par de elementos para sumar O encontré la suma requerida
    if i == len(arr)-1 or sum_eight == True:
        return sum_eight
    else:
        # Verifico si la suma del par de elementos es igual a 'X' retorno True
        if arr[i] + arr[j] == requiredSum:  
            return hasPairWithSumRecursion (arr, requiredSum,sum_eight = True)     
        # Verifico si ya sumé todos los pares posibles para el elemento seleccionado y paso al siguiente elemento
        else: 
            if j == len(arr)-1:
                i += 1  # Ubico 'i' en el siguiente elemento
                j = i + 1  # Y ubico 'j' en la siguiente posición del índice de 'i'
                return hasPairWithSumRecursion (arr, requiredSum, sum_eight, i, j)
            else:
                # Mantengo la posición de 'i' y ubico 'j' en el siguiente índice
                return hasPairWithSumRecursion (arr, requiredSum, sum_eight, i, j+1)

# main
if __name__ == "__main__":
    array1 = [1,4,3,9]
    print('Array1: ',array1,' \n')
    print('Desarrollo en el menor tiempo posible\nArray 1: ',hasPairWithSum(array1, 8))
    print('\nDesarrollo con el menor costo posible\nArray 1: ',hasPairWithSumRecursion(array1, 8))

    print('--------------------------------------')

    array2 = [1,2,4,4]
    print('Array2: ',array2,' \n')
    print('Desarrollo en el menor tiempo posible\n Array 2: ',hasPairWithSum(array2, 8))
    print('\nDesarrollo con el menor costo posible\n Array 2: ',hasPairWithSumRecursion(array2,8))


