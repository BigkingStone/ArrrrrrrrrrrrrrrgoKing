# 📌 Array

> *An array is a collection of items stored at contiguous memory locations.*

## 1. Array?

: 메모리 상의 원소를 연속으로 배치한 자료구조

## 2. Array의 성질

- **k번째 원소를 O(1)에 확인 및 변경**이 가능하다.
- **추가적으로 소모되는 메모리의 양(=overhead)가 거의 없다.**
- **Cache hit rate**가 높다.
    
    ***Cache hit rate(캐시 메모리 적중률)란?***
    
    - (추가바람)
    
    ***왜 배열은 Cache hit rate(캐시 메모리 적중률)이 높은가?***
    
    - 메모리 상에 데이터들이 붙어있기 때문이다.
- 메모리 상에 연속한 구간을 잡아야 해서 **할당에 제약**이 걸린다.

## 3. Array Operations

- 임의의 위치에 있는 원소를 확인/변경 - Time Complexity: O(1)
- 배열의 끝에 원소 추가, 배열의 마지막 원소 삭제 - Time Complexity: O(1)
- 임의의 위치에 원소 추가, 임의의 위치의 원소 삭제 - Time Complexity: O(N)
    - **insert(a, index)**: Insert element ‘a’ at the index position - Time Complexity: O(N)
    - **erase(index)**: Erase element at the index position - Time Complexity: O(N)

## 4. Python에서의 배열

Python에서는 배열(array)을 `list` 문법으로 사용할 수 있다.

- **list[*index*]**: index위치의 원소에 접근 가능
- **list.append(*element*)**
- **list.insert(*index*, *element*)**
- **list.pop(*element*)**
    - list = list[:-1]

```python
# numbers = list()
numbers = [1,2,3,4,5]

numbers[1] = 100
print(numbers)  # [1, 100, 3, 4, 5]

numbers.append(200)
print(numbers)  # [1, 100, 3, 4, 5, 200]

numbers.pop()
print(numbers)  # [1, 100, 3, 4, 5]

numbers.pop(1)
print(numbers)  # [1, 3, 4, 5]

numbers.insert(0,300)
print(numbers)  # [300, 1, 3, 4, 5]
```

## 5. Swift에서의 배열

Swift에서는 배열(array)을 `Array`문법으로 사용할 수 있다.

```swift
var numbers: [Int] = [1,2,3,4,5]

numbers[1] = 100
print(numbers)  // [1, 100, 3, 4, 5]

numbers.append(200) 
print(numbers)  // [1, 100, 3, 4, 5, 200]

let popElement: Int? = numbers.popLast()
print(numbers) // [1, 100, 3, 4, 5]
print(popElement!)  // 200

numbers.remove(at: 1)
print(numbers)  // [1, 3, 4, 5]

numbers.insert(300, at: 0)
print(numbers)  // [300, 1, 3, 4, 5]
```

---

***reference***

[[실전 알고리즘] 0x03강 - 배열](https://blog.encrypted.gg/927)

[Array Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/array-data-structure/)
