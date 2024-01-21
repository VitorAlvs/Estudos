// Calcular idade (Alterar anoNasc para contar)
anoNasc = 1978
function CalcIdade(anoNasc){
    Idade = new Date().getFullYear()  - anoNasc
    const Situação = Idade >= 18 ? "é maior de idade." : "é menor de idade, faltam " + (18 - Idade) + " anos para atingir a maioridade."
    return "Você tem " + Idade + " anos e " + Situação
}

console.log(CalcIdade(anoNasc))



