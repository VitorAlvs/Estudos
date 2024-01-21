// Gerar números inteiros aleatórios dentro de um intervalo
// randomRange(Valor maximo, valor mínimo)
function randomRange(myMin, myMax) {
  let result =  Math.floor(Math.random() * (myMax - myMin + 1) + myMin);

  if (result <= myMax && result >= myMin){
    return result;
  }
  else{
    return randomRange(myMin, myMax)
  }
}