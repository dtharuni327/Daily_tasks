def validate_email(email):
    return '@' in email

def validate_age(age_str):

    try:

        age = int(age_str)

        return 18 <= age <= 60

    except ValueError:

        return False

def task1_data_processing():

    users = []

    while True:

        name = input("Enter name (or 'done' to finish): ")

        if name.lower() == 'done':

            break

        email = input("Enter email: ")

        age = input("Enter age: ")

        users.append({'name': name, 'email': email, 'age': age})

    valid_users = [u for u in users if validate_email(u['email']) and validate_age(u['age'])]

    invalid_users = [u for u in users if u not in valid_users]

    print(f"\nTotal users: {len(users)}")

    print(f"Valid users count: {len(valid_users)}")

    print(f"Invalid users count: {len(invalid_users)}")

    print("Valid:", valid_users)

    print("Invalid:", invalid_users)

def find_duplicates(lst):

    duplicates = []

    for i in range(len(lst)):

        for j in range(i + 1, len(lst)):

            if lst[i] == lst[j] and lst[i] not in duplicates:

                duplicates.append(lst[i])

    return duplicates

def is_palindrome(s):

    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    return cleaned == cleaned[::-1]

def second_highest(lst):

    if len(lst) < 2:

        return None

    sorted_unique = sorted(set(lst), reverse=True)

    return sorted_unique[1] if len(sorted_unique) > 1 else None

if __name__ == "__main__":

    task1_data_processing()

    print("Duplicates in [1,2,3,2,4,1]:", find_duplicates([1,2,3,2,4,1]))

    print("Palindrome 'A man a plan a canal Panama':", is_palindrome("A man a plan a canal Panama"))

    print("Second highest [1,3,2]:", second_highest([1,3,2]))

    print("Second highest [5,5,5]:", second_highest([5,5,5]))
 
