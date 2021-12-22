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

    def crack_letter(self, cracked_password: list) -> bool:
        cracked = False
        temp_password = cracked_password.copy()
        for letter in range(97, 123):  # a to z in ASCII
            temp_password.append(chr(letter))
            if temp_password == self.password:
                cracked_password = temp_password
                print("PASSWORD CRACK SUCCESSFUL")
                print(f"The password is: {''.join(cracker.password)}")
                cracked = True
            else:
                del temp_password[-1]
        return cracked

    def crack_password(self):
        cracked = False
        cracked_password = []
        while not cracked:
            temp_password = cracked_password.copy()


cracker = Cracker()
cracker.crack_letter(cracked_password=[])
