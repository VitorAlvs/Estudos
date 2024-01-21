// Alterar operador e valores no arr para calcular
let operador = "+"
const arr = [9, 8, 7, 6, 2];
let total = arr[0];

switch(operador){
    // Soma
    case "+":
        for (let i = 1; i < arr.length; i++) { 
            total = total + arr[i]
         }
        break;
    // Subtração
    case "-":
        for (let i = 1; i < arr.length; i++){ 
            total = total - arr[i]
        }
        break;
    // Multiplicação
    case "*":
        for (let i = 1; i < arr.length; i++){
            total =  total * arr[i]
        }
        break;
    // Divisão
    case "/":
        for (let i = 1; i < arr.length; i++){
            total =  total / arr[i]
        }
        break
}

console.log(total)

