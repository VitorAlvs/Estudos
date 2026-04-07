//1
let diaSemana = prompt('Que dia da semana é hoje?')

// '|| quer dizer "ou"'
if (diaSemana == 'Sábado' || diaSemana == 'Domingo'){
    alert("Bom fim de semana!")
}
else {
    alert("Boa semana!")
}

//2
let numero = prompt('Digite um número')

if(numero < 0){
    alert(`O número ${numero} é negativo`)
}
else{
    alert(`O número ${numero} é positivo`)
}

//3
let pontos = 105

if (pontos >= 100){
    alert('Parabéns, você venceu!')
} 
else{
    alert('Tente novamente para ganhar')
}