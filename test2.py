first = [1, 4, 54, 6, 786, 78]
second = [1, 0, 6, 4, 7, 3, 5, 98]

for i in range(len(first)):
    try:
        print(f"{first[i] / second [i]} = {first[i] / second[i]}")
    except Exception as exc:
        print(repr(exc))