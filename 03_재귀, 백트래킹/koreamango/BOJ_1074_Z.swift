import Foundation

/// n = 배열의 크기, r = 행, c =열
func funcZ(_ n : Int ,_ r : Int ,_ c : Int) -> Int {
    if n == 0 {return 0}
    
    let half = 1 << (n-1) // 한 변의 절반 그러므로 2^n - 1
    
    if r < half && c < half { // 1번 자리인 경우
        return funcZ(n-1, r, c) // 크기는 1/2 되므로 n-1, r 위치와 c 위치는 그대로
    }
    if r < half && c >= half { // 2번 자리인 경우
        return half * half + funcZ(n-1, r, c-half) // 크기는 1/2 되므로 n-1, r 위치는 그대로와 c 위치 시작점은 절반 기준으로 다시 시작
    }
    if r >= half && c < half{ // 3번 자리인 경우
        return 2 * half * half + funcZ(n-1, r-half, c) // 크기는 1/2 되므로 n-1, r 위치 시작점은 절반 기준으로 다시 시작과 c 위치는 그대로
    }
    return 3 * half * half + funcZ(n-1, r-half, c-half) // 4번 자리인 경우
    // 크기는 1/2 되므로 n-1, r 위치와 c 위치의 시작점은 절반 기준으로 다시 시작
}

let input = readLine()!.split(separator: " ").map{Int($0)!}

let (n, r ,c) = (input[0], input[1], input[2])

print(funcZ(n, r, c))


