N = int(input())
arr = [input() for _ in range(N)] 

def sum_numbers(x:str) -> int:
  result = 0
  for num in x:
    if num.isdigit():
      result += int(num)
  return result

# 람다식 쓰는 것 잘 활용하기
arr.sort(key=lambda x: (len(x),sum_numbers(x),x))
print("\n".join(arr))
