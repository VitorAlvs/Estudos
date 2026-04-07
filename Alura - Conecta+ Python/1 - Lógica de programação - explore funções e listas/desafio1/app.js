//2
let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';


//3
function cliqueButtonConsole(){
    console.log('O botão foi clicado');
}

//4
function cliqueButtonAlerta(){
    alert("Eu amo JS");
}

//5
function cliqueButtonPrompt(){
    let cidade = prompt("Escreva o nome de uma cidade");
    alert(`Estive em ${cidade} e lembrei de você`)
}

//6
function cliqueButtonSoma(){
    let numeroPrimeiro = parseInt(prompt('Escreva um número'));
    let numeroSegundo = parseInt(prompt('Escreva outro número'));
    alert(`A soma de ${numeroPrimeiro} e ${numeroSegundo} resulta em ${numeroPrimeiro + numeroSegundo}`);
}