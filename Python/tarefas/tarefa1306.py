# IMPLEMENTAR AS SEGUINTES FUNÇÕES:
    # Listar os cursos cadastrados - retornar o número de cadastros
    # Dado um código de curso, retornar o nome do curso e duração em anos
    # Dado o nome de um curso, retornar o código do curso e duração em anos
    # Dado um código de curso, retornar um vetor com o nome de todas das disciplinas cadastradas para este curso
    # Dado o nome de um curso, retornar um vetor com o nome de todas das disciplinas cadastradas para este curso
    # Dado um código de curso, retornar a carga horária total de todas das disciplinas cadastradas para este curso
    # Dado o nome de um curso, retornar a carga horária total de todas das disciplinas cadastradas para este curso
    # Dado o nome de uma disciplina, consultar os cursos que a oferecem - retornar em um vetor
    # Dado o código de um curso, retornar um vetor contendo o código, o nome e a carga horária das disciplinas 

import os
from dataset import *

def clearTerminal():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def listar_cursos():
    print("Cursos cadastrados:")
    for curso in DScurso:
        print("Código:", curso["CODIGO"])
        print("Nome:", curso["NOME"])
        print("Duração em anos:", curso["DURACAO"])
        print("--------------")
    return len(DScurso)

def buscar_curso_por_codigo(codigo):
    for curso in DScurso:
        if curso["CODIGO"] == codigo:
            return curso["NOME"], curso["DURACAO"]
    return None, None

def buscar_curso_por_nome(nome):
    for curso in DScurso:
        if curso["NOME"] == nome:
            return curso["CODIGO"], curso["DURACAO"]
    return None, None

def listar_disciplinas_por_codigo(codigo):
    disciplinas = []
    for disciplina in DSdisciplinas:
        if disciplina["CODIGOCURSO"] == codigo:
            disciplinas.append(disciplina["DISCIPLINA"])
    return disciplinas

def listar_disciplinas_por_nome(nome):
    disciplinas = []
    for disciplina in DSdisciplinas:
        curso = buscar_curso_por_nome(nome)
        if disciplina["CODIGOCURSO"] == curso[0]:
            disciplinas.append(disciplina["DISCIPLINA"])
    return disciplinas

def calcular_carga_horaria_total_por_codigo(codigo):
    carga_horaria_total = 0
    for disciplina in DSdisciplinas:
        if disciplina["CODIGOCURSO"] == codigo:
            carga_horaria_total += disciplina["HORASAULAS"]
    return carga_horaria_total

def calcular_carga_horaria_total_por_nome(nome):
    carga_horaria_total = 0
    for disciplina in DSdisciplinas:
        curso = buscar_curso_por_nome(nome)
        if disciplina["CODIGOCURSO"] == curso[0]:
            carga_horaria_total += disciplina["HORASAULAS"]
    return carga_horaria_total

def buscar_cursos_por_disciplina(disciplina):
    cursos = []
    for curso in DScurso:
        for disciplina_curso in DSdisciplinas:
            if disciplina_curso["CODIGOCURSO"] == curso["CODIGO"] and disciplina_curso["DISCIPLINA"] == disciplina:
                cursos.append(curso["NOME"])
    return cursos

def buscar_disciplinas_por_curso(codigo):
    disciplinas = []
    for disciplina in DSdisciplinas:
        if disciplina["CODIGOCURSO"] == codigo:
            disciplinas.append({
                "Código": disciplina["CODIGODISCIPLINA"],
                "Disciplina": disciplina["DISCIPLINA"],
                "Carga Horária": disciplina["HORASAULAS"]
            })
    return disciplinas

while True:
    print("---- MENU ----")
    print("1. Listar cursos cadastrados")
    print("2. Buscar curso por código")
    print("3. Buscar curso por nome")
    print("4. Listar disciplinas por código do curso")
    print("5. Listar disciplinas por nome do curso")
    print("6. Calcular carga horária total por código do curso")
    print("7. Calcular carga horária total por nome do curso")
    print("8. Buscar cursos que oferecem uma disciplina")
    print("9. Buscar disciplinas de um curso")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    clearTerminal()
    if opcao == "1":
        total_cursos = listar_cursos()
        print("Total de cursos cadastrados:", total_cursos)
        print()
    elif opcao == "2":
        codigo = input("Digite o código do curso: ")
        nome, duracao = buscar_curso_por_codigo(codigo)
        if nome:
            print("Nome:", nome)
            print("Duração em anos:", duracao)
        else:
            print("Curso não encontrado.")
        print()
    elif opcao == "3":
        nome = input("Digite o nome do curso: ")
        codigo, duracao = buscar_curso_por_nome(nome)
        if codigo:
            print("Código:", codigo)
            print("Duração em anos:", duracao)
        else:
            print("Curso não encontrado.")
        print()
    elif opcao == "4":
        codigo = input("Digite o código do curso: ")
        disciplinas = listar_disciplinas_por_codigo(codigo)
        if disciplinas:
            print("Disciplinas:")
            for disciplina in disciplinas:
                print(disciplina)
        else:
            print("Curso não encontrado ou sem disciplinas cadastradas.")
        print()
    elif opcao == "5":
        nome = input("Digite o nome do curso: ")
        disciplinas = listar_disciplinas_por_nome(nome)
        if disciplinas:
            print("Disciplinas:")
            for disciplina in disciplinas:
                print(disciplina)
        else:
            print("Curso não encontrado ou sem disciplinas cadastradas.")
        print()
    elif opcao == "6":
        codigo = input("Digite o código do curso: ")
        carga_horaria_total = calcular_carga_horaria_total_por_codigo(codigo)
        if carga_horaria_total > 0:
            print("Carga horária total:", carga_horaria_total)
        else:
            print("Curso não encontrado ou sem disciplinas cadastradas.")
        print()
    elif opcao == "7":
        nome = input("Digite o nome do curso: ")
        carga_horaria_total = calcular_carga_horaria_total_por_nome(nome)
        if carga_horaria_total > 0:
            print("Carga horária total:", carga_horaria_total)
        else:
            print("Curso não encontrado ou sem disciplinas cadastradas.")
        print()
    elif opcao == "8":
        disciplina = input("Digite o nome da disciplina: ")
        cursos = buscar_cursos_por_disciplina(disciplina)
        if cursos:
            print("Cursos que oferecem a disciplina:")
            for curso in cursos:
                print(curso)
        else:
            print("Disciplina não encontrada ou sem cursos cadastrados.")
        print()
    elif opcao == "9":
        codigo = input("Digite o código do curso: ")
        disciplinas = buscar_disciplinas_por_curso(codigo)
        if disciplinas:
            print("Disciplinas do curso:")
            for disciplina in disciplinas:
                print("Código:", disciplina["Código"])
                print("Disciplina:", disciplina["Disciplina"])
                print("Carga Horária:", disciplina["Carga Horária"])
                print("--------------")
        else:
            print("Curso não encontrado ou sem disciplinas cadastradas.")
        print()
    elif opcao == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        print()
    os.system('pause')
    clearTerminal()
