inputs = [[0,0], [0,1], [1,0], [1,1]]
target = [0, 0, 0, 1]

w1, w2, b = 0.1, 0.1, 0.1
lr = 0.1

for epoch in range(1):
    for i in range(4):
        x1, x2 = inputs[i]
        y = w1*x1 + w2*x2 + b
        error = target[i] - y

        w1 += lr * error * x1
        w2 += lr * error * x2
        b += lr * error

print("Final weights:", round(w1, 3), round(w2, 3))
print("Final bias:", round(b, 3))

for x in inputs:
    y = w1*x[0] + w2*x[1] + b
    output = 1 if y >= 0.5 else 0
    print(x, "->", output)