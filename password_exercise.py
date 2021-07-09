username = 'codeup'
password = 'notastrongpassword'

five_or_more_char = (length(password) >= 5)
long_username = (length(username) > 20)
same_u_and_p = (username == password)
password_has_spaces = password != password.strip()
