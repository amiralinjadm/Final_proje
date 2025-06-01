def name_input():
    input_user = input("plase inter name:(spac for next)")
    names = input_user.split()
    if not names:
        print("no name in list!")
        return
    print("name list")
    for i, name in enumerate(names, start=1):
        print(f"{i}.{name}")
    print(f"name number: {len(names)}")
name_input()