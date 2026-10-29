inputs = [[0,0], [0,1], [1,0], [1,1]]
target = [0, 0, 0, 1]

for lr in [0.1, 0.3, 0.5]:
    w1, w2, b = 0.1, 0.1, 0.1

    for epoch in range(1, 1001):
        for i in range(4):
            x1, x2 = inputs[i]
            y = w1*x1 + w2*x2 + b
            error = target[i] - y

            w1 += lr * error * x1
            w2 += lr * error * x2
            b += lr * error

        if all((1 if w1*x[0] + w2*x[1] + b >= 0.5 else 0) == target[i]
               for i, x in enumerate(inputs)):
            break

    print("LR:", lr, "Epochs:", epoch)