import Foundation
//MARK: - 입력
private var inputNM = readLine()!.components(separatedBy: " ")
private var (N, M) = (Int(inputNM[0])!, Int(inputNM[1])!)
private var arr : [[String]] = []
for _ in (1...N){
    arr.append(readLine()!.components(separatedBy: " "))
}

func functionX(_ to: Int, _ from: Int, _ x:Int, _ y:Int) -> Int{
    var cnt = 0
    for k in (to..<from){
        if arr[y][k] == "0"{
            cnt += 1
        }
    }
    return cnt
}

func functionY(_ to: Int, _ from: Int, _ x:Int, _ y:Int) -> Int {
    var cnt = 0
    for k in (to..<from){
        if arr[k][x] == "0"{
            cnt += 1
        }
    }
    return cnt
}

func drawingY(_ to: Int, _ from: Int, _ x:Int, _ y:Int){
    for k in (to..<from){
        if arr[k][x] == "0"{
            arr[k][x] = "#"
        }
    }
}
func drawingX(_ to: Int, _ from: Int, _ x:Int, _ y:Int){
    for k in (to..<from){
        if arr[y][k] == "0"{
            arr[y][k] = "#"
        }
    }
}


//MARK: - 함수
func CCTV1(_ y : Int, _ x : Int) {
    var selectMax : [Int] = []
    // 0 ~ x ... 1
    selectMax.append(functionX(0 ,x ,x, y))
    // 0 ~ y ... 2
    selectMax.append(functionY(0 ,y ,x, y))
    // x ~ M ... 3
    selectMax.append(functionX(x ,M ,x ,y))
    // y ~ N ... 4
    selectMax.append(functionY(y ,N ,x ,y))
    
    let maxIdx = (selectMax.firstIndex(of: selectMax.max()!) ?? -1) + 1
    
    if maxIdx == 1{
        drawingX(0, x, x, y)
    } else if maxIdx == 2 {
        drawingY(0 ,y ,x, y)
    } else if maxIdx == 3{
        drawingX(x ,M ,x ,y)
    } else {
        drawingY(y ,N ,x ,y)
    }
}

func CCTV2(_ y : Int, _ x : Int) {
    var selectMax : [Int] = []
    // 0 ~ M ... 1
    selectMax.append(functionX(0 ,M ,x ,y))
    // 0 ~ N ... 2
    selectMax.append(functionY(0 ,N ,x ,y))
    
    let maxIdx = (selectMax.firstIndex(of: selectMax.max()!) ?? -1) + 1
    print(selectMax, maxIdx)
    if maxIdx == 1{
        drawingX(0, M, x, y)
    } else if maxIdx == 2 {
        drawingY(0 ,N ,x, y)
    }
}

func CCTV3(_ y : Int, _ x : Int) {
    var selectMax : [Int] = []
    // 0 ~ x    || 0 ~ y    ... 1
    selectMax.append(functionX(0 ,x ,x ,y) + functionY(0 ,y ,x ,y))
    
    // x ~ M || 0 ~ y    ... 2
    selectMax.append(functionX(x ,M ,x ,y) + functionY(0 ,y ,x ,y))
    
    // x ~ M || y ~ N ... 3
    selectMax.append(functionX(x ,M ,x ,y) + functionY(y ,N ,x ,y))
    
    // 0 ~ x    || y ~ N ... 4
    selectMax.append(functionX(0 ,x ,x ,y) + functionY(y ,N ,x ,y))
    
    let maxIdx = (selectMax.firstIndex(of: selectMax.max()!) ?? -1) + 1
    
    if maxIdx == 1{
        drawingX(0, x, x, y)
        drawingY(0 ,y ,x ,y)
    } else if maxIdx == 2 {
        drawingX(x ,M ,x ,y)
        drawingY(0 ,y ,x ,y)
    } else if maxIdx == 3{
        drawingX(x ,M ,x ,y)
        drawingY(y ,N ,x ,y)
    } else {
        drawingX(0 ,x ,x ,y)
        drawingY(y ,N ,x ,y)
    }
}

func CCTV4(_ y : Int, _ x : Int) {
    var selectMax : [Int] = []
    // 0 ~ M || 0 ~ y    ... 1
    selectMax.append(functionX(0 ,M ,x ,y) + functionY(0 ,y ,x ,y))
   
    // 0 ~ M || y ~ N ... 2
    selectMax.append(functionX(0 ,M ,x ,y) + functionY(y ,N ,x ,y))
    
    // 0 ~ x || 0 ~ N ... 3
    selectMax.append(functionX(0 ,x ,x ,y) + functionY(0 ,N ,x ,y))
    
    // x ~ M || 0 ~ N ... 4
    selectMax.append(functionX(x ,M ,x ,y) + functionY(0 ,N ,x ,y))
   
    let maxIdx = (selectMax.firstIndex(of: selectMax.max()!) ?? -1) + 1
    
    if maxIdx == 1{
        drawingX(0 ,M ,x ,y)
        drawingY(0 ,y ,x ,y)
    } else if maxIdx == 2 {
        drawingX(0 ,M ,x ,y)
        drawingY(y ,N ,x ,y)
    } else if maxIdx == 3{
        drawingX(0 ,x ,x ,y)
        drawingY(0 ,N ,x ,y)
    } else {
        drawingX(x ,M ,x ,y)
        drawingY(0 ,N ,x ,y)
    }
}

func CCTV5(_ y : Int, _ x : Int) {
    var selectMax : [Int] = []
    // 0 ~ M && 0 ~ N ... 1
    selectMax.append(functionX(0 ,M ,x ,y) + functionY(0 ,N ,x ,y))
    
    let maxIdx = (selectMax.firstIndex(of: selectMax.max()!) ?? -1) + 1
    
    if maxIdx == 1{
        drawingX(0 ,M ,x ,y)
        drawingY(0 ,N ,x ,y)
    }
}

//MARK: - 메인
for (indexA, array) in arr.enumerated() {
    for (indexV,value) in array.enumerated() {
        if value == "1"{
            CCTV1(indexA,indexV)
        } else if value == "2"{
            CCTV2(indexA,indexV)
        } else if value == "3"{
            CCTV3(indexA,indexV)
        } else if value == "4"{
            CCTV4(indexA,indexV)
        } else if value == "5"{
            CCTV5(indexA,indexV)
        }
        
    }
}

//MARK: - 출력

for i in arr{
    print(i)
}
print(arr.map{$0.filter {Int($0) == 0}.count}.reduce(0,+))
