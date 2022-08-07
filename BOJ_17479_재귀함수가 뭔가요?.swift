//
//  main.swift
//  Test
//
//  Created by 강민규 on 2022/08/07.
//

import Foundation

var input : Int = Int(readLine()!)!

var space : String = ""

var str0 : String = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
var str1 : String = "\"재귀함수가 뭔가요?\""
var str2 : String = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
var str3 : String = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
var str4 : String = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
var str5 : String = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
var str6 : String = "라고 답변하였지."

func outputStr(int : Int) -> Void{
    if int == 0 {
        print(space+str1)
        print(space+str5)
        print(space+str6)
        return
    }
    if input == int {
        print(str0)
    }
    print(space+str1)
    print(space+str2)
    print(space+str3)
    print(space+str4)
    
    space += "____"
    outputStr(int: int-1)
    space = String(space.dropLast(4))
    
    print(space+str6)
}


outputStr(int: input)
