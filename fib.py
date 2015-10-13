# Print Fibonacci Numbers

def fib(x):
  result = []
  a, b = 0, 1
  while a < x:
    result.append(a)		
    a, b = b, a + b		
  return result

if __name__ == '__main__':
  data = fib(int(input('Enter the range : ')))
  print(data)