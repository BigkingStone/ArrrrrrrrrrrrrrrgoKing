//
//  BOJ_곱셈_1629.swift
//  Test
//
//  Created by 강민규 on 2022/07/31.
//

import Foundation
func mf(_ a: Int , _ b: Int, _ c:Int) -> Int{
    if (b==1){
        return a % c
    }
    var val = mf(a, b/2, c)
    val = val * val % c
    if (b % 2 == 0){
        return val
    }
    return val * a % c
}

var n = readLine()!.components(separatedBy: " ").map { Int($0)! }

print(mf(n[0], n[1], n[2]))
