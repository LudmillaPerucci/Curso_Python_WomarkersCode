'''Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.'''
 
login_user = input("Insira o seu usuário: ")
senha_user = input("Insira a sua senha: ")

while (login_user != "admin" or senha_user != "admin123"):
    print("Usuário ou senha inválidos, tente novamente ")
    login_user = input("Insira o seu usuário: ")
    senha_user = input("Insira a sua senha: ")

print("Login realizado com sucesso! ")
