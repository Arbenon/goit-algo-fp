def greedy_algorithm(items, budget):
    # Створимо список страв з їхніми властивостями
    items_list = [(name, details['cost'], details['calories']) for name, details in items.items()]
    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    items_list.sort(key=lambda x: x[2] / x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for name, cost, calories in items_list:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
            
    return selected_items, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print(f"Selected items: {selected_items}")
print(f"Total calories: {total_calories}")


def dynamic_programming(items, budget):
    # Створимо список страв з їхніми властивостями
    items_list = [(name, details['cost'], details['calories']) for name, details in items.items()]
    n = len(items_list)
    
    # Ініціалізуємо DP таблицю
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо DP таблицю
    for i in range(1, n + 1):
        name, cost, calories = items_list[i - 1]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо вибрані страви
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, cost, calories = items_list[i - 1]
            selected_items.append(name)
            w -= cost
    
    selected_items.reverse()  # Порядок обрання страв неважливий, але для коректності можна перевернути
    
    return selected_items, dp[n][budget]

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100
selected_items, total_calories = dynamic_programming(items, budget)
print(f"Selected items: {selected_items}")
print(f"Total calories: {total_calories}")
