while True:
    data = input("Please enter data (If there is no data push the Enter): ")
    if not data: break
    with open('data_file.txt', 'a') as fayl:
        fayl.write(data + '\n')
