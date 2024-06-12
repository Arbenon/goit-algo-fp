import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sums_count[roll_sum] += 1
    
    probabilities = {sum_val: count / num_rolls for sum_val, count in sums_count.items()}
    return probabilities

def main():
    num_rolls = 1000000
    probabilities = simulate_dice_rolls(num_rolls)
    
    theoretical_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    
    # Вивід та показ результатів
    print(f"{'Сума':<4} {'Симульована ймовірність':<30} {'Теоретична ймовірність'}")
    for sum_val in range(2, 13):
        sim_prob = probabilities[sum_val]
        theo_prob = theoretical_probabilities[sum_val]
        print(f"{sum_val:<4} {sim_prob:<30} {theo_prob}")
    
    # Результати
    sums = list(range(2, 13))
    sim_probs = [probabilities[sum_val] for sum_val in sums]
    theo_probs = [theoretical_probabilities[sum_val] for sum_val in sums]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sums, sim_probs, label='Симульована ймовірність', marker='o')
    plt.plot(sums, theo_probs, label='Теоретична ймовірність', marker='x')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність розподілення сум кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
