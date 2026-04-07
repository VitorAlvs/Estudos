let count = 0;

function cc(card) {
  // Altere apenas o código abaixo desta linha
  switch (card){
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count += 1
      break;
    case 7:
    case 8:
    case 9:
      count += 0
      break;
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count += -1
      break;
  }

  if (count >= 1){
    return count + " Bet"
  }
  else{
    return count + " Hold"
  }

  return "Change Me";
  // Altere apenas o código acima desta linha
}

cc(9); cc(6); cc(2); cc('Q'); cc('K');

console.log(cc(2));
console.log(cc(3));
console.log(cc(7));
console.log(cc('Q'));
console.log(cc('A'));