import Foundation

var cnt = 0

/// a = 원판의 개수, b = 원판 출발 점, c = 원판 도착 점
func hanoi(_ a : Int ,_ b : Int ,_ n : Int) -> Void {
    if n == 1 {
        print("\(a) \(b)")
        return
    } else {
        hanoi(a, 6-a-b, n-1)
        print("\(a) \(b)")
        hanoi(6-a-b, b, n-1)
    }
    
}

let n = Int(readLine()!)!

print(1<<n - 1)
hanoi(1,3,n)
