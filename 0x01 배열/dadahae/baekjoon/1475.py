# 입력받고
# numbers에 저장
# 단, 6과 9는 같은 것으로 본다.
# numbers에서 max값 리턴

N = input()
numbers = [0 for _ in range(10)]

for num in N:
  if num == "9":
    numbers[6] += 1
  else:
    numbers[int(num)] += 1

numbers[6] = numbers[6] // 2 + numbers[6] % 2
print(max(numbers))
