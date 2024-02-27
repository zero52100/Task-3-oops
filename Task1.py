class Add:
    def __call__(self, numbers):
        return sum(numbers)

add = Add()

limit = int(input("Enter the number of integers you want to add: "))
input_list = []

for i in range(limit):
    user_input = int(input(f"Enter integer {i + 1}: "))
    input_list.append(user_input)

total = add(input_list)
print(f"Total: {total}")
