medicine = {1: "Нурофен для детей, суспензия для приема внутрь 100мг/5мл", 2: "Ибупрофен, суспензия для приема внутрь, 100мг/5мл",
            3: "Ибупрофен Форте, суспензия для приема внутрь, 40мг/мл", 4: "Парацетамол, суспензия для приема внутрь, 120мг/5мл",
            5: "Эффералган, раствор для приема внутрь для детей, 30мг/мл", 6: "Панадол детский, cуспензия 120 мг/5 мл"}

medicine_doze = 0

def show_result(choice, weight, medicine_doze):
    print(f"Разовая доза препарата {medicine[choice]}, для ребенка весом {weight} кг составляет: {round(medicine_doze,1)} мл")

def show_warning(problem):
    if problem == "weight":
        print()
        print("Внимание! Этот препарат нельзя применять у детей весом менее 10 кг. Выберете другой детский жаропонижающий препарат.")
        print()

    elif problem == "age":
        print()
        print("Этот препарат нельзя применять у детей в возрасте до 1 года. Выберете другой детский жаропонижающий препарат.")
        print()

def ask_weight():
    weight = eval(input("Введите вес ребенка в килограммах: "))
    return weight

def make_choice():
    print("Выберете детское жаропонижающее в форме сиропа(суспензии) для расчета дозировки: ")
    for i in medicine:
        print(f"{i} - {medicine[i]}")
    print()
    choice = int(input())
    return choice

def give_result(choice, weight):
    if choice == 1 or choice == 2:
        single_doze = 10*weight
        medicine_doze = (single_doze*5)/100
        show_result(choice, weight, medicine_doze)

    elif choice == 3:
        if weight < 10:
            problem = "weight"
            show_warning(problem)
            run_program()

        elif weight >= 10:
            age= int(input("Уточните, сколько ребенку полных лет:  "))
            if age < 1:
                problem = "age"
                show_warning(problem)
                run_program()

            elif age >= 1:
                single_doze = 10 * weight
                medicine_doze = (single_doze * 1) / 40
                show_result(choice, weight, medicine_doze)

    elif choice == 4 or choice == 6:
        single_doze = 15*weight
        medicine_doze = (single_doze*5)/120
        show_result(choice, weight, medicine_doze)

    elif choice == 5:
        single_doze = 15* weight
        medicine_doze = (single_doze*1)/30
        show_result(choice, weight, medicine_doze)

def run_program():
    weight = ask_weight()
    choice = make_choice()
    give_result(choice, weight)

run_program()