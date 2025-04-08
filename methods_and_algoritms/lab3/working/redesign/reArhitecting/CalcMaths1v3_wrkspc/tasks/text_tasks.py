"""
Текстові задачі проєкту CalcMaths.

Цей модуль містить реалізації різних завдань для роботи з текстом.
"""

def text_split(text):
    """
    Допоміжна функція для розділення тексту на слова.
    
    Args:
        text (str): Вхідний текст
        
    Returns:
        list: Список слів без порожніх елементів
    """
    return [word for word in text.split() if word]

def task_6_a(variables):
    """
    Задача 6.a: Підрахунок пробілів до першого знаку оклику.
    
    Args:
        variables (list): Список змінних [text]
        
    Returns:
        tuple: (опис задачі, опис вхідних даних, результат)
    """
    text = variables[0] if variables else "Hello world! How are you!"
    
    # Знаходимо індекс першого знаку оклику
    exclamation_index = text.find('!')
    if exclamation_index == -1:
        return "No exclamation mark found in the string", f"Input: {text}", 0
    
    # Підраховуємо кількість пробілів до першого знаку оклику
    spaces_count = text[:exclamation_index].count(' ')
    
    return "Count spaces before first exclamation mark", f"Input: {text}", spaces_count

def task_18(variables):
    """
    Задача 18: Підрахунок слів, у яких перший і останній символи співпадають.
    
    Args:
        variables (list): Список змінних [text]
        
    Returns:
        tuple: (опис задачі, опис вхідних даних, результат)
    """
    text = variables[0] if variables else "Hello world level deed stats"
    
    # Отримуємо список слів через допоміжну функцію
    words = text_split(text)
    
    # Знаходимо слова, де перший і останній символи співпадають
    matching_words = [word for word in words if word and word[0].lower() == word[-1].lower()]
    
    return ("Count words where first and last characters match", 
            f"Input: {text}", 
            f"Matching words: {matching_words}\nCount: {len(matching_words)}")

# Майбутні текстові задачі буде додано тут 