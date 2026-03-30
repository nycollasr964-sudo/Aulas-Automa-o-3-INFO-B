while True:
  try:
    n1 = float(input("Digite um numero para ser divido"))
    n2 = float(input("Digite o numero para dividir o primeiro"))
    div = n1 / n2
    print(" O resultado é ",div)
  except ValueError:
   print("O valor é digitado é invalidp")
  except ZeroDivisionError:
   print("Você não pode dividir por 0")
  except Exception as e:
   print("Ocorreu um erro ", e)