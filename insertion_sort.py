def insertion_sort(unsorted_list):
    """Функция сортировки вставкой. Возвращает отсортированный список"""
    for i in range(1, len(unsorted_list)):
        while i >= 0 and (unsorted_list[i - 1]) > int(unsorted_list[i]):
            unsorted_list[i - 1], unsorted_list[i] = unsorted_list[i], unsorted_list[i - 1]
            i -= 1
    return unsorted_list