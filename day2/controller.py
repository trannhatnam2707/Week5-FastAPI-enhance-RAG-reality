from service import register_service, login_service, get_me_service, get_all_user_service


def register_user(username: str,password: str):
    return register_service(username, password)

def login_user(form_data):
    return login_service(form_data)

def get_me(token):
    return get_me_service(token)

def get_all_user():
    return get_all_user_service()