def fun1(input,add):
    answer = 0
    machines = []
    with open(input) as f:
        lines = ""
        for line in f:
            if line != "\n":
                line = line.replace("\n", " ")
            lines += line
        machines = lines.split("\n")
        for machine in machines:
            _, A, B, PRIZE = machine.split(":")
            AX, AY = A.replace("Button B", "").strip().replace(", Y+", " ").replace("X+", "").split(" ")
            AX, AY = int(AX), int(AY)

            BX, BY = B.replace("Prize", "").strip().replace(", Y+", " ").replace("X+", "").split(" ")
            BX, BY = int(BX), int(BY)

            X, Y = PRIZE.replace("X=", "").strip().split(", Y=")
            X, Y = int(X)+add, int(Y)+add

            answer += calculate_buttons((AX, AY), (BX,BY), 0, 0, (X, Y))


    print(answer)

def calculate_buttons(A_button, B_button, a_pressed, b_pressed, prize):
    AX, AY = A_button
    BX, BY = B_button
    PX, PY = prize

    B = ((-1 * AY) * PX + AX * PY) / ((-1 * AY) * BX + AX * BY)
    if ((PX - BX*B)/AX) == ((PY - BY*B)/AY):
        A = (PX - BX*B)/AX
        if A % 1 == 0 and B % 1 == 0:
            return  A * 3 + B
    A = ((-1 * BY) * PX + BX * PY) / ((-1 * BY) * AX + BX * AY)
    if ((PX - AX * A) / BX) == ((PY - AY * A) / BY):
        B = (PX - AX * A) / BX
        if A % 1 == 0 and B % 1 == 0:
            return A * 3 + B
    return 0


input = "input.txt"
#input = "smallinput.txt"
fun1(input, 0)
input = "input.txt"
#input = "smallinput.txt"
fun1(input, 10000000000000)