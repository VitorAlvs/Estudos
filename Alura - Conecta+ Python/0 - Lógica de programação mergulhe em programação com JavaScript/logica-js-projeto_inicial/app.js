alert("Boas vindas ao jogo do número secreto!");

// Variáveis em JS
//Número aleatório
let numeroMaximo = 5000;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1);
console.log(`O número secreto é ${numeroSecreto}`);
let chute;
console.log(`O chute foi ${chute}`);
let tentativas = 1;
console.log(`Tentativas: ${tentativas}`)

//Condições
while (chute != numeroSecreto) {
  chute = prompt(`Escolha um número entre 0 e ${numeroMaximo}`);

  //Se chite for igual ao número secreto
  if (numeroSecreto == chute) {
    //parar
    break;
  } else {
    if (chute > numeroSecreto) {
      alert(`O número secreto é menor que ${chute}`);
    } else {
      alert(`O número secreto é maior que ${chute}`);
    }
    //tentativas = tentativas + 1
    tentativas++;
    console.log(`Tentativas: ${tentativas}`)
  }
}

console.log(`Tentativas: ${tentativas}`)

//Operador ternário
// tentativas é maior que um? Se sim escrever 'tentativas' e se não, escrever 'tentativa'
let palavraTentativa = tentativas > 1 ? "tentativas" : "tentativa";
alert(
  `Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}`
);

// if (tentativas > 1){
//     alert(`Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas`);
// } else{
//     alert(`Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativa`);
// }
