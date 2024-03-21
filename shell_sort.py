def shell_sort(array: list) -> list:
    """
        Функция сортировки методом Шелла
    """
    
    # Получение длины массива
    length_of_array = len(array)
    # Вычисление начального значения разрыва
    gap = length_of_array // 2
    
    # Пока значение разрыва больше 0
    while gap > 0:
        # Проход по подмассивам
        for i in range(gap, length_of_array):
            temp = array[i]
            j = i
            
            # Сортировка элементов в подмассиве
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

    return list(array)


array = [8, 6, 7, 2, 1, 4, 5, 3]
print(shell_sort(array))