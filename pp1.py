import re

def is_valid_author(author):
    return re.fullmatch(r"[a-zA-Z]((?!_)\w)*", author) and\
           2*len(re.findall(r"\d", author)) <= len(author)

def is_valid_password(password):
    return re.fullmatch(r"(?:(?:(?:(?:(?:(\d)(?:(?!\1)[\dA-F]))|(?:[A-F]\d))))\.){3}(?:(?:(?:(\d)((?!\2)[\dA-F]))|([A-F]\d)))", password)

def is_valid_ip(ip):
    return re.fullmatch(r"((\d|(\d\d)|([01]\d\d)|([2](([0-4]\d)|([5][0-5]))))\.){3}(\d|(\d\d)|([01]\d\d)|([2](([0-4]\d)|([5][0-5]))))", ip)

def is_valid_email(email):
    return re.fullmatch(r"[A-Za-z][^@]*@[^@]*\.[^@]*", email)

def is_valid_transaction(transaction):
    return re.fullmatch(r"((pull)|(push)|(stash)|(fork)|(pop))", transaction)

def is_valid_repository(repository):
    return re.fullmatch(r"[a-z]+([_]([a-z]+))*", repository)

def is_valid_hash_md5(hash_md5):
    return re.fullmatch(r"[a-f\d]{32}", hash_md5)

def verify(author, password, ip, email, transaction, repository, hash_md5):
    return is_valid_author(author) and is_valid_password(password) and is_valid_ip(ip) and is_valid_email(email) and is_valid_transaction(transaction) and is_valid_repository(repository) and is_valid_hash_md5(hash_md5)

def main():
    try:
        my_input = input().split()
        if len(my_input) != 7:
            print(False)
        else:
            author, password, ip, email, transaction, repository, hash_md5 = my_input
            print(True if verify(author, password, ip, email, transaction, repository, hash_md5) else False)
    except EOFError:
        print(False)

if __name__ == "__main__":
    main()
