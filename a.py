def name_input():
    input_user = input("plase inter name:(spac for next)")
    names = input_user.split()
    if not names:
        print("no name in list!")
        return
    print("name list")
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")
    print(f"name number: {len(names)}")
name_input()
