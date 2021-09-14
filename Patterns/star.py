try:
    num_rows = int(input("Masukkan nilai rows: "))
    for i in range(0, num_rows):
        for j in range(0, num_rows - i - 1):
            print(end=" ")
        for a in range(0, i + 1):
            print("*", end=" ")
        print()
except ValueError:
    print("Alert: You must insert number...")
except Exception as e:
    print("There is something error..")