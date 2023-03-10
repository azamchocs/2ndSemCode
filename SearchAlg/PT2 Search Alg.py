import os
os.system('cls')

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def LinearSearch(data):
    for i in range(len(var)):
        if isinstance(var[i], str) and var[i] == data:
            return i
        elif isinstance(var[i], list) and data in var[i]:
            return (i, var[i].index(data))
    return None

while True:
    SearchWho = input("Who to find? (type 'Breakout' to stop): ")
    if SearchWho == "Breakout":
        print("Search stopped.")
        break
    Result = LinearSearch(SearchWho)
    if Result is None:
        print(f"{SearchWho} Not Found.")
    elif isinstance(Result, int):
        print(f"{SearchWho} di indeks {Result}.")
    else:
        print(f"{SearchWho} di indeks {Result[0]} pada kolom {Result[1]}.")
