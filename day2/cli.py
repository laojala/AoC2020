from ValidatePassword import ValidatePassword

if __name__ == "__main__":
    counter = ValidatePassword.process_file("file.dat")
    print("Rule 1:", counter["policy1"])
    print("Rule 2:", counter["policy2"])
