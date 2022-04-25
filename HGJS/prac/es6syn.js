//* Object Shorthand Assignment
let name = "moriah"
let age = 24

// 일반적
let person = {
    name: name,
    age: age
}
console.log(person)
// 숏코드
//! 같을 경우 생략할 수 있음
let name2 = 'hwankko'
let person2 = {
    name2,
    age
}
console.log(person2)

//* Destructuring
// : 객체를 분해해서 가져옴
let person3 = {
    name: 'Ralo',
    age : '27'
}

// 방법1
// let name3 = person3.name
// let age3 = person3.age

// 방법2
// 객체뿐만아니라 배열에도 적용가능
let {name3,age3} = person3

console.log(name3, age3)

let array = [1, 2, 3, 4]
let [a, b, ...rest] = array
// ...rest : 나머지 rest에 넣음
console.log(a,b)

//* spread

let robot = {
    name: 'paka',
    age: '19'
}
// 1)객체의 깊은 복사
let robot2 = {...robot}

console.log(robot2)

// 2)바로 할당
let robot3 = robot
console.log(robot3)

// 2)의 경우 객체의 주소값만 복사
// 즉, 객체는 하나이고 그 객체를 참조하는 변수가 두개
// 1)의 경우 실제로 객체를 하나 더 생성하는거 ( 객체가 다른 2개 )
// 둘은 복사 형태가 다름
console.log(robot == robot3)
console.log(robot == robot2)

let robot4 = { ...robot, name:'homin' }
console.log(robot4)

// 배열에도 똑같이 사용가능
let x = [1, 2]
let y = [...x, 3]
console.log(y)
let z = [...x, ...y]
console.log(z)

//* 삼항연산자
let machine = {
    name : 'Dopa',
    age : '28'
}
if (machine) {
    console.log(machine.name)
}else {
    console.log("there is no miya")
}


// 삼항연산자
let machine2 = null
console.log(machine2?machine.name:"there is no miya!!")