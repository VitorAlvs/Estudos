let listaDeNumerosSorteados = [];
let numeroLimite = 10;
let numerSecreto = gerarNumeroAleatorio();
let tentativas = 1;

function exibirTextoNaTela(tag, texto) {
  let campo = document.querySelector(tag);
  campo.innerHTML = texto;
   if ('speechSynthesis' in window) {
        let utterance = new SpeechSynthesisUtterance(texto);
        utterance.lang = 'pt-BR'; 
        utterance.rate = 1.2; 
        window.speechSynthesis.speak(utterance); 
    } else {
        console.log("Web Speech API não suportada neste navegador.");
    }
}
function exibirMensagemInicial(){
  exibirTextoNaTela("h1", "Jogo do número secreto");
  exibirTextoNaTela("p", "Escolha um número entre 1 e 10");
}


function verificarChute() {
  let chute = document.querySelector("input").value;
  if (chute == numerSecreto) {
    exibirTextoNaTela("h1", "Parabéns, você acertou!");
    let palavraTentativa = tentativas > 1 ? "tentativas" : "tentativa";
    let mensagemTentativas = `Você acertou o número secreto com ${tentativas} ${palavraTentativa}`;
    exibirTextoNaTela("p", mensagemTentativas);
    document.getElementById("reiniciar").removeAttribute("disabled");
  } else {
    if (chute > numerSecreto) {
      exibirTextoNaTela("p", "O número secreto é menor que " + chute);
    } else {
      exibirTextoNaTela("p", "O número secreto é maior que " + chute);
    }
    tentativas++;
    limparCampo();
  }
}

function gerarNumeroAleatorio() {
  let numeroEscolhido = parseInt(Math.random() * numeroLimite + 1);
  let quantidadeDeElementosNaLista = listaDeNumerosSorteados.length;

  if (quantidadeDeElementosNaLista >= 10) {
    listaDeNumerosSorteados = [];
  } 

  if (listaDeNumerosSorteados.includes(numeroEscolhido)) {
    return gerarNumeroAleatorio();
  } else {
    listaDeNumerosSorteados.push(numeroEscolhido);
    return numeroEscolhido;
  }
}

function limparCampo() {
  chute = document.querySelector("input")
  chute.value = "";
}

function reiniciarJogo() {
  numerSecreto = gerarNumeroAleatorio();
  limparCampo();
  tentativas = 1;
  exibirMensagemInicial();
  document.getElementById("reiniciar").setAttribute("disabled", true);
  limparCampo();
}

exibirMensagemInicial();