def adicionar_tarefa(tarefas, descricao):
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")


def concluir_tarefa(tarefas, descricao):  
        for tarefa in tarefas:
            if tarefa["descricao"] == descricao:
                tarefa["concluida"] = True
                print(f"Tarefa '{descricao}' concluída com sucesso!")
                return
        print(f"Tarefa '{descricao}' não encontrada.")


def remover_tarefa(tarefas, descricao):
     for tarefa in tarefas:
          if tarefa["descricao"] == descricao:
               tarefas.remove(tarefa)
               print(f"tarefa '{descricao}' removida com sucesso")
     

tarefas = []

while True:
     
 print(
"====LISTA DE TAREFAS====    " \
"\n                      "
"\n 1- Ver Tarefas      " \
"\n 2-Adicionar Tarefa          " \
"\n 3- Marcar tarefa como concluida      " \
"\n 4- Remover Tarefa  " \
"\n 5- Sair")

 opcao = int(input("Escolha uma opção: "))

 if opcao== 1:
    for tarefa in tarefas:
     status = "(x)" if tarefa["concluida"] else "( )"
     print(f"Tarefa: {tarefa['descricao']} {status}") 

 elif opcao== 2:
      descricao =  input("Digite a descrição da nova tarefa: ")
      adicionar_tarefa(tarefas, descricao)

 elif opcao== 3:
    descricao= input("Digite a tarefa a ser concluída: ")
    concluir_tarefa(tarefas, descricao) 

 elif opcao== 4:
      descricao= input("Digite a tarefa a ser excluída: ")
      remover_tarefa(tarefas, descricao)

 elif opcao== 5:
  print("saindo...")
  break

 else:
     print("opção inválida")
