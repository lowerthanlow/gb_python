
with open('bakery.csv', 'r', encoding='utf-8') as file:

  output = file.readlines()

  input = input()

  if len(input) == 1:
    number = output[int(input)-1:]
    print(''.join(number))

  elif len(input) >= 2 and input[0].isdigit() and input[2].isdigit():
    number = output[int(input[0])-1:int(input[2])]
    print(''.join(number))

  else:
    print(''.join(output))

    

    
