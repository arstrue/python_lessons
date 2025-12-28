import turtle
import random

# ------------------ НАСТРОЙКА ЭКРАНА ------------------

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("skyblue")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

WIDTH, HEIGHT = 900, 600

# ------------------ ВСПОМОГАТЕЛЬНЫЕ ------------------

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def circle_filled(r, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# ------------------ СНЕГ ВНИЗУ ------------------

t.color("white")
t.fillcolor("white")
move(-WIDTH//2, -HEIGHT//2)
t.begin_fill()

# нижняя линия
t.goto(WIDTH//2, -HEIGHT//2)

# волнистая верхняя граница
for x in range(WIDTH//2, -WIDTH//2 - 1, -40):
    y = -180 + random.randint(-15, 15)
    t.goto(x, y)

t.goto(-WIDTH//2, -HEIGHT//2)
t.end_fill()

# ------------------ СНЕГОВИК ------------------
t.pencolor("black")
# нижний шар
move(-250, -170 - 20)
circle_filled(55, "white")

# средний
move(-250, -60 - 20)
circle_filled(42, "white")

# голова
move(-250, 15 - 20)
circle_filled(32, "white")

# глаза
t.color("black")
move(-262, 55 - 20)
circle_filled(4, "black")
move(-238, 55 - 20)
circle_filled(4, "black")

# нос-морковка
t.color("orange")
move(-250, 45 - 20)
t.begin_fill()
t.goto(-205, 38 - 20)
t.goto(-250, 32 - 20)
t.goto(-250, 45 - 20)
t.end_fill()

# ------------------ ВЕДРО ------------------

t.color("black")
t.fillcolor("gray")
move(-280, 85 - 28)
t.begin_fill()
t.goto(-220, 85 - 28)
t.goto(-235, 120 - 28)
t.goto(-265, 120 - 28)
t.goto(-280, 85 - 28)
t.end_fill()

# ------------------ ЁЛКА ------------------

def triangle(cx, by, w, h):
    move(cx - w//2, by)
    t.fillcolor("darkgreen")
    t.begin_fill()
    t.goto(cx + w//2, by)
    t.goto(cx, by + h)
    t.goto(cx - w//2, by)
    t.end_fill()

triangle(230, -160, 220, 140)
triangle(230, -90, 180, 120)
triangle(230, -30, 140, 100)

# ствол
move(210, -190)
t.fillcolor("saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

# ------------------ ШАРИКИ ВНУТРИ ЁЛКИ ------------------

def rand_point(tri):
    (x1, y1, x2, y2, x3, y3) = tri
    r1, r2 = random.random(), random.random()
    if r1 + r2 > 1:
        r1, r2 = 1 - r1, 1 - r2
    x = x1 + r1*(x2-x1) + r2*(x3-x1)
    y = y1 + r1*(y2-y1) + r2*(y3-y1)
    return x, y

colors = ["red", "yellow", "blue", "purple", "pink"]

tree_tris = [
    (120, -160, 340, -160, 230, -20),
    (140, -90, 320, -90, 230, 30),
    (160, -30, 300, -30, 230, 70),
]

for _ in range(28):
    x, y = rand_point(random.choice(tree_tris))
    move(x, y)
    circle_filled(6, random.choice(colors))

# ------------------ ЗВЕЗДА ------------------

star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.penup()
star.goto(213, 80)   # координаты вершины ёлки
star.pendown()

def draw_star(color):
    star.clear()
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(35)
        star.right(144)
    star.end_fill()

star_state = True

def blink_star():
    global star_state
    if star_state:
        draw_star("darkred")
    else:
        draw_star("red")
    star_state = not star_state
    screen.ontimer(blink_star, 500)  # мигание каждые 0.5 сек

blink_star()

# ------------------ АНИМАЦИЯ ПАДАЮЩЕГО СНЕГА ------------------
snowflakes = []

SNOW_COUNT = 50

for _ in range(SNOW_COUNT):
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.speed(0)
    s.color("white")

    # случайная позиция по ВСЕЙ высоте
    x = random.randint(-WIDTH // 2, WIDTH // 2)
    y = random.randint(-HEIGHT // 2, HEIGHT // 2)

    s.goto(x, y)

    # индивидуальная скорость
    s.fall_speed = random.randint(2, 6)

    snowflakes.append(s)

def animate_snow():
    for s in snowflakes:
        s.clear()
        s.sety(s.ycor() - s.fall_speed)
        s.dot(4)

        # если упала ниже экрана — появляется СЛУЧАЙНО сверху
        if s.ycor() < -HEIGHT // 2:
            s.goto(
                random.randint(-WIDTH // 2, WIDTH // 2),
                random.randint(HEIGHT // 2 - 30, HEIGHT // 2)
            )
            s.fall_speed = random.randint(2, 6)

    screen.update()
    screen.ontimer(animate_snow, 40)

animate_snow()


turtle.done()
