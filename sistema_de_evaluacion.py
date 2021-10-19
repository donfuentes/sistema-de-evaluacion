import random
import operator


def run():

    # Funcion que evalua números random unicos

    def random_unique(num, List):
        if len(List) == 0:
            return True
        else:
            number_found = 0

            for j in List:
                if num == j:
                    number_found = 1
                    return False
            if number_found == 0:
                return True

    # Funcion que busca el key de la respuesta correcta de la pregunta

    def answer_found(id_answer, list_answers):
        ok_answer = 0
        for i in list_answers:
            if i == id_answer:
                ok_answer = i
        return ok_answer

    # función para validar que la respuesta sea válida

    def check_answer(answer_letter):
        while answer_letter.upper() == "" or ord(answer_letter.upper()) < 65 or ord(answer_letter.upper()) > 69:
            if answer_letter.upper() == "":
                print(
                    "Por favor ingresa una respuesta valida. Solo puedes ingresar A , B, C, D o E")
                answer_letter = str(input("Respuesta: "))
            else:
                if ord(answer_letter.upper()) < 65 or ord(answer_letter.upper()) > 69:
                    print(
                        "Por favor ingresa una respuesta valida. Solo puedes ingresar A , B, C, D o E")
                    ord(answer_letter.upper())
                    answer_letter = str(input("Respuesta: "))
        return answer_letter

    welcome = """
------------------------------
Evalúa tus conocimientos
------------------------------
¿Cuántas preguntas eliges?:
"""

    total_questions_dict = {
        "1": "¿Cuál es la capital de Colombia?",
        "2": "¿Cuáles son las ramas del poder público?",
        "3": "¿Qué son los números primos?",
        "4": "¿Qué son los adjetivos?",
        "5": "¿Popayan es la capital de:?",
        "6": "¿Cuál es el nombre del Presidente de Colombia?",
        "7": "¿En qué año fue la independencia de Colombia?",
        "8": "¿En qué año fue el descubrimiento de América?",
        "9": "¿Cuál es el resultado de 1553,16/1000?",
        "10": "¿Qué es un sustantivo?"
    }

    total_correct_answers = {
        "1": "Bogotá",
        "2": "Ejecutiva, Legislativa y judicial",
        "3": "Aquellos números que unicamente se pueden dividir por ellos mismos y por la unidad",
        "4": "Son las cualidades o características de un objeto o persona",
        "5": "Departamento del Cauca",
        "6": "Iván Duque Márquez",
        "7": "En 1810",
        "8": "En 1492",
        "9": "1,55316",
        "10": "Son los nombres que designan objetos o personas"
    }

    total_wrong_answers = {
        "20": "Sincelejo",
        "21": "Congreso, Asambleas y Concejos municipales",
        "22": "Aquellos números que son hijos de números hermanos",
        "23": "Son los apellidos de las personas",
        "24": "Departamento de Santander",
        "25": "Juan Manuel Santos",
        "26": "En 1792",
        "27": "En 1495",
        "28": "155,316",
        "29": "Son Jueces de la República",
        "30": "3,1415"
    }

    # variables utilizadas para el proceso

    answer_letters = ["a", "b", "c", "d", "e"]

    amount_questions = len(total_questions_dict)
    choices = 3

    total_questions_list = []
    partial_questions_list = []
    partial_questions_dict = {}

    answers_dict = {}
    answers_dict_sorted = {}
    answer_dict_final = {}

    total_wrong_answers_list = []
    partial_wrong_answers_list = []

    number_questions = input(welcome)

    score = 0
    good_answers = 0
    bad_answers = 0

    cont_input = 1
    cont_questions = 0

    while number_questions == "" or int(number_questions) < 5 or int(number_questions) > amount_questions:
        print("Por favor ingresar un número de preguntas válido ( El número de preguntas debe estar entre 5 y ", amount_questions, "). Te quedan: ",
              choices-cont_input, "Oportunidades")

        number_questions = input("Escoge el número de preguntas: ")
        cont_input += 1

        if cont_input == 3:
            break

    if number_questions == "":
        print("Lo lamentamos!!! Haz perdido la oportunidad de presentar tu prueba.")

    elif int(number_questions) < 5:
        print("Lo lamentamos!!! Haz perdido la oportunidad de presentar tu prueba.")

    elif int(number_questions) > amount_questions:
        print("Lo lamentamos!!! Haz perdido la oportunidad de presentar tu prueba.")

    else:
        print("""
------------------------------
Iniciemos!!
------------------------------
""")
        # inicializa las variables para el score final

        val_answer = 100/int(number_questions)
        max_score = int(number_questions) * val_answer
        min_score = max_score*.6

        level1 = max_score * .8
        level2 = min_score

        # carga la lista del total de consecutivos de las preguntas

        for i in total_questions_dict:
            total_questions_list.append(int(i))

        # carga la lista del total de consecutivos de las respuestas erroneas

        for i in total_wrong_answers:
            total_wrong_answers_list.append(int(i))

        # carga los consecutivos del número de preguntas seleccionadas

        for j in range(1, int(number_questions)+1):
            flag_control = 0

            while flag_control == 0:
                key_question = random.choice(total_questions_list)

                if random_unique(key_question, partial_questions_list) == True:
                    partial_questions_list.append(key_question)
                    flag_control = 1
                    break

        # carga la lista de las preguntas seleccionadas

        for k in partial_questions_list:
            partial_questions_dict[k] = total_questions_dict.get(str(k))

        # imprime las preguntas del examen

        for l in partial_questions_dict:
            cont_questions += 1
            print(str(cont_questions) + ")", partial_questions_dict[l])

            # genera la respuesta correcta

            answer_question_key = str(answer_found(l, partial_questions_list))

            answer_question_text = total_correct_answers.get(
                str(answer_question_key))

            # inserta la respuesta correcta al diccionario de respuestas de la pregunta

            answers_dict[answer_question_key] = answer_question_text

            # inserta las demás respuestas (incorrectas) al diccionario de respuesas de la pregunta

            for i in range(1, 5):
                flag_control_answers = 0

                while flag_control_answers == 0:
                    key_question_wrong = random.choice(
                        total_wrong_answers_list)

                    if random_unique(str(key_question_wrong), partial_wrong_answers_list) == True:

                        wrong_answer_question_key = str(
                            answer_found(key_question_wrong, total_wrong_answers_list))

                        wrong_answer_question_text = total_wrong_answers.get(
                            str(wrong_answer_question_key))

                        # inserta la respuesta correcta al diccionario de respuestas de la pregunta

                        answers_dict[str(wrong_answer_question_key)
                                     ] = wrong_answer_question_text

                        partial_wrong_answers_list.append(
                            str(key_question_wrong))
                        flag_control_answers = 1
                        break

            # imprime el diccionario de respuestas de la pregunta

            # ordena por texto el diccionario de respuestas para asignar la letra de cada uno

            answers_dict_sorted = sorted(
                answers_dict.items(), key=operator.itemgetter(1), reverse=True)

            ascii_letter = 65

            # imprime y carga el diccionario final de respuestas

            for name in enumerate(answers_dict_sorted):
                print(chr(ascii_letter) + ".", answers_dict[name[1][0]])
                answer_dict_final[chr(ascii_letter)] = answers_dict[name[1][0]]
                ascii_letter += 1

            # valida que la respuesta sea una respuesta válida

            answer = str(input("Respuesta: "))
            check_answer(answer)

            # evalua la respuesta

            answer_value = ""

            for i, j in answer_dict_final.items():
                if i == answer.upper():
                    answer_value = j

            for i, j in total_correct_answers.items():
                if j == answer_value:
                    score = score + val_answer
                    good_answers += 1

            bad_answers = int(number_questions) - good_answers

            # limpia el diccionario de respuesas de la pregunta y la lista de preguntas incorrectas

            answers_dict.clear()
            answer_dict_final.clear()
            partial_wrong_answers_list.clear()

        print("")

        # imprime score final

        print("Tu puntaje fue --> "+str(round(score, 2)))
        print("Tuviste " + str(good_answers) + " respuesta(s) correcta(s) y " +
              str(bad_answers) + " respuesta(s) incorrecta(s)")

        # imprime nivel según el resultado

        if score >= level1:
            print("Felicitaciones!! Aprobaste!! Eres nivel ALTO...sigue así!!")
        elif score >= level2 and score < level1:
            print("Aprobaste!! Eres nivel MEDIO...puedes mejorar!!")
        else:
            print(
                "Reprobaste!! Eres nivel BAJO...estudia un poco más!!")


if __name__ == '__main__':
    run()
