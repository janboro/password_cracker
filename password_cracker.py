import time


class Cracker:
    def __init__(self):
        self.password = self.input_password()

    def input_password(self) -> list:
        print("Enter your password")
        password = input()
        # .isalpha method checks if there are only letters in string
        if password != password.lower() or not password.isalpha():
            raise ValueError("We only accept lower case letters")
        return list(password)

    def bruteforce(self, pwd_len, pwd=[], depth=0):
        depth += 1
        for letter in range(97, 123):
            pwd.append(chr(letter))
            if depth != pwd_len:
                pwd = self.bruteforce(pwd_len=pwd_len, pwd=pwd, depth=depth)
            if pwd == self.password:
                return pwd
            del pwd[-1]
        return pwd

    def crack_password(self):
        pwd_len = 1
        cracked = False
        while not cracked:
            pwd = self.bruteforce(pwd_len=pwd_len)
            if pwd == self.password:
                print("Cracked!")
                cracked = True
            pwd_len += 1
        return "".join(pwd)


cracker = Cracker()
start_time = time.time()
cracked_password = cracker.crack_password()
end_time = time.time()

print(f"The cracked password is: {cracked_password}")
print(f"Elapsed time: {end_time - start_time}")
