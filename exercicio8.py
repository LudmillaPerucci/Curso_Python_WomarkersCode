
hora_exer_sem = input("Informe quantas horas de exercício físico você faz por semana: ")

try:
    hora_exer_sem_int = int(hora_exer_sem)
    # Cálculo das calorias queimadas
    total_caloria = (((hora_exer_sem_int * 60) * 5) * 4)
    print(f"O total de calorias gastas ao mês é: {total_caloria}")
except ValueError:
    print("Por favor, insira um número válido de horas.")