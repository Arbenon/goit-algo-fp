import turtle
import math

def draw_tree(branch_length, level, angle):
    if level == 0:
        return
    
    # Малюємо гілку
    turtle.forward(branch_length)
    turtle.left(angle)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1, angle)
    turtle.right(2 * angle)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1, angle)
    turtle.left(angle)
    turtle.backward(branch_length)

def main():

    level = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 10): "))
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

    initial_branch_length = 100
    angle = 45

    try:
        draw_tree(initial_branch_length, level, angle)
    except turtle.Terminator:
        print("Виникла помилка turtle.Terminator: графічне вікно було закрите або не вдалося викликати методи turtle.")
    turtle.done()

if __name__ == "__main__":
    main()

