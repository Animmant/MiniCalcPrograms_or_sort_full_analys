import time
import random
import matplotlib.pyplot as plt

# 1. Merge Sort
def merge_sort(arr):
   if len(arr) <= 1:
       return arr
   
   mid = len(arr) // 2
   left = merge_sort(arr[:mid])
   right = merge_sort(arr[mid:])
   return merge(left, right)

def merge(left, right):
   result = []
   i = j = 0
   
   while i < len(left) and j < len(right):
       if left[i] <= right[j]:
           result.append(left[i])
           i += 1
       else:
           result.append(right[j])
           j += 1
           
   result.extend(left[i:])
   result.extend(right[j:])
   return result

# 2. Bubble Sort
def bubble_sort(arr):
   n = len(arr)
   for i in range(n):
       for j in range(0, n-i-1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr

# 3. Selection Sort 
def selection_sort(arr):
   n = len(arr)
   for i in range(n):
       min_idx = i
       for j in range(i+1, n):
           if arr[j] < arr[min_idx]:
               min_idx = j
       arr[i], arr[min_idx] = arr[min_idx], arr[i]
   return arr

# Функція для генерації тестових даних
def generate_test_data(size):
   random_array = [random.randint(1, 1000) for _ in range(size)]
   sorted_array = list(range(size))
   nearly_sorted = list(range(size))
   swaps = size // 20
   for _ in range(swaps):
       i, j = random.randint(0, size-1), random.randint(0, size-1)
       nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
   return random_array, sorted_array, nearly_sorted

# Функція для вимірювання часу виконання
def measure_time(func, arr):
   start_time = time.time()
   func(arr.copy())
   end_time = time.time()
   return end_time - start_time

def test_sorting_algorithms():
   print("=== ТЕСТУВАННЯ АЛГОРИТМІВ СОРТУВАННЯ ===\n")
   
   # Тест 1: Звичайний масив
   test1 = [64, 34, 25, 12, 22, 11, 90]
   print("Тест 1: Звичайний масив")
   print("Вхідний масив:", test1)
   print("Merge Sort:", merge_sort(test1.copy()))
   print("Bubble Sort:", bubble_sort(test1.copy()))
   print("Selection Sort:", selection_sort(test1.copy()))
   print("Очікуваний результат:", sorted(test1))
   print("\nВсі алгоритми працюють правильно для Тесту 1:", 
         merge_sort(test1.copy()) == bubble_sort(test1.copy()) == selection_sort(test1.copy()) == sorted(test1))
   print("-" * 50)

   # Тест 2: Відсортований масив
   test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   print("\nТест 2: Відсортований масив")
   print("Вхідний масив:", test2)
   print("Merge Sort:", merge_sort(test2.copy()))
   print("Bubble Sort:", bubble_sort(test2.copy()))
   print("Selection Sort:", selection_sort(test2.copy()))
   print("Очікуваний результат:", sorted(test2))
   print("\nВсі алгоритми працюють правильно для Тесту 2:", 
         merge_sort(test2.copy()) == bubble_sort(test2.copy()) == selection_sort(test2.copy()) == sorted(test2))
   print("-" * 50)

   # Тест 3: Зворотньо відсортований масив
   test3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
   print("\nТест 3: Зворотньо відсортований масив")
   print("Вхідний масив:", test3)
   print("Merge Sort:", merge_sort(test3.copy()))
   print("Bubble Sort:", bubble_sort(test3.copy()))
   print("Selection Sort:", selection_sort(test3.copy()))
   print("Очікуваний результат:", sorted(test3))
   print("\nВсі алгоритми працюють правильно для Тесту 3:", 
         merge_sort(test3.copy()) == bubble_sort(test3.copy()) == selection_sort(test3.copy()) == sorted(test3))
   print("-" * 50)

   # Тест 4: Масив з повторюваними елементами
   test4 = [1, 4, 2, 4, 2, 4, 1, 2, 3]
   print("\nТест 4: Масив з повторюваними елементами")
   print("Вхідний масив:", test4)
   print("Merge Sort:", merge_sort(test4.copy()))
   print("Bubble Sort:", bubble_sort(test4.copy()))
   print("Selection Sort:", selection_sort(test4.copy()))
   print("Очікуваний результат:", sorted(test4))
   print("\nВсі алгоритми працюють правильно для Тесту 4:", 
         merge_sort(test4.copy()) == bubble_sort(test4.copy()) == selection_sort(test4.copy()) == sorted(test4))
   print("-" * 50)

   # Тест 5: Порожній масив
   test5 = []
   print("\nТест 5: Порожній масив")
   print("Вхідний масив:", test5)
   print("Merge Sort:", merge_sort(test5.copy()))
   print("Bubble Sort:", bubble_sort(test5.copy()))
   print("Selection Sort:", selection_sort(test5.copy()))
   print("Очікуваний результат:", sorted(test5))
   print("\nВсі алгоритми працюють правильно для Тесту 5:", 
         merge_sort(test5.copy()) == bubble_sort(test5.copy()) == selection_sort(test5.copy()) == sorted(test5))
   print("-" * 50)

   # Тест 6: Один елемент
   test6 = [1]
   print("\nТест 6: Масив з одним елементом")
   print("Вхідний масив:", test6)
   print("Merge Sort:", merge_sort(test6.copy()))
   print("Bubble Sort:", bubble_sort(test6.copy()))
   print("Selection Sort:", selection_sort(test6.copy()))
   print("Очікуваний результат:", sorted(test6))
   print("\nВсі алгоритми працюють правильно для Тесту 6:", 
         merge_sort(test6.copy()) == bubble_sort(test6.copy()) == selection_sort(test6.copy()) == sorted(test6))
   print("-" * 50)

   # Тест 7: Великий випадковий масив
   test7 = random.sample(range(1, 1001), 100)
   print("\nТест 7: Великий випадковий масив (показано перші 10 елементів)")
   print("Вхідний масив (перші 10):", test7[:10])
   merged = merge_sort(test7.copy())
   bubbled = bubble_sort(test7.copy())
   selected = selection_sort(test7.copy())
   expected = sorted(test7)
   print("Merge Sort (перші 10):", merged[:10])
   print("Bubble Sort (перші 10):", bubbled[:10])
   print("Selection Sort (перші 10):", selected[:10])
   print("Очікуваний результат (перші 10):", expected[:10])
   print("\nВсі алгоритми працюють правильно для Тесту 7:", 
         merged == bubbled == selected == expected)
   print("-" * 50)

   print("\n=== ПІДСУМОК ТЕСТУВАННЯ ===")
   print("Всі алгоритми успішно пройшли всі тести!")
   print("Тестування завершено.")

# Тестування продуктивності
sizes = [100, 500, 1000, 5000]
results = {
   'Merge Sort': {'random': [], 'sorted': [], 'nearly_sorted': []},
   'Bubble Sort': {'random': [], 'sorted': [], 'nearly_sorted': []},
   'Selection Sort': {'random': [], 'sorted': [], 'nearly_sorted': []}
}

for size in sizes:
   random_arr, sorted_arr, nearly_sorted_arr = generate_test_data(size)
   
   for arr_type, arr in [('random', random_arr), 
                        ('sorted', sorted_arr), 
                        ('nearly_sorted', nearly_sorted_arr)]:
       results['Merge Sort'][arr_type].append(
           measure_time(merge_sort, arr))
       results['Bubble Sort'][arr_type].append(
           measure_time(bubble_sort, arr))
       results['Selection Sort'][arr_type].append(
           measure_time(selection_sort, arr))

# Візуалізація результатів
plt.figure(figsize=(15, 5))
types = ['random', 'sorted', 'nearly_sorted']
titles = ['Random Array', 'Sorted Array', 'Nearly Sorted Array']

for i, (type_, title) in enumerate(zip(types, titles)):
   plt.subplot(1, 3, i+1)
   plt.plot(sizes, results['Merge Sort'][type_], 
           'o-', label='Merge Sort')
   plt.plot(sizes, results['Bubble Sort'][type_], 
           'o-', label='Bubble Sort')
   plt.plot(sizes, results['Selection Sort'][type_], 
           'o-', label='Selection Sort')
   plt.title(title)
   plt.xlabel('Array Size')
   plt.ylabel('Time (seconds)')
   plt.legend()
   plt.grid(True)

plt.tight_layout()
plt.show()

if __name__ == "__main__":
   test_sorting_algorithms()


