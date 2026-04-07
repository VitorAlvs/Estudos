function checkObj(obj, checkProp) {
  // Altere apenas o código abaixo desta linha
  if( obj.hasOwnProperty(checkProp) == true){
    return obj[checkProp]
  }
  else{
    return "Not Found"
  };
  // Altere apenas o código acima desta linha
}

console.log(checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "gift"))
console.log(checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "pet"))
console.log(checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "house"))
console.log(checkObj({city: "Seattle"}, "city"))
console.log(checkObj({city: "Seattle"}, "district"))
console.log(checkObj({pet: "kitten", bed: "sleigh"}, "gift"))