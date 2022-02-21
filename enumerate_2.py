def full_emails(people):
    result = []
    for email,name in enumerate(people):
        result.append('{} <{}>'.format(name , email))
    return result

email_1 = [('pranav@example.com' , 'Pranav'),
        ('aryan@example.com' , 'Aryan'),
        ('anurag@example.com' , 'Anurag') ]

print(full_emails(email_1))
