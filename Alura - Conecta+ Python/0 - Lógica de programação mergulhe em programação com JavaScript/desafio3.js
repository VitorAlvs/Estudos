//1
console.log("Boas vindas!");

//2
let nome = "João";
console.log(`Olá, ${nome}!`);

//3
alert(`Olá, ${nome}!`);

//4
let linguagem = prompt("Qual a linguagem de programação que você mais gosta?");
console.log(linguagem);

//5
let valor1 = 5;
let valor2 = 9;
let resultado = valor1 + valor2;
console.log(`A soma de ${valor1} e ${valor2} é igual a ${resultado}`);

//6
let valor3 = 8;
let valor4 = 4;
let resultado2 = valor3 - valor4;
console.log(`A diferença entre ${valor1} e ${valor2} é igual a ${resultado2}`);

//7
let idade = prompt("Digite sua idade");
if (idade >= 18){
    console.log("Você é maior de idade.");
} else {
    console.log("Você é menor de idade.")
}

//8
let numero = prompt("Digite um número:");
let sinal = numero > 0 ? "positivo" : "negativo";

if (numero == 0){
    console.log(`O número é zero.`);
} else {
    console.log(`O numero é ${sinal}`);
}

//9
contagem = 0
while (contagem < 11){
    console.log(contagem)
    contagem++;
}

//10
let nota = 8;
console.log(nota >= 7 ? "Aprovado" : "Reprovado") 

//11
console.log(Math.random())

//12
console.log(parseInt( Math.random() * 10 + 1))

//13
console.log(parseInt( Math.random() * 1000 + 1))