using System.Reflection.Metadata;

int quantidadeEstoque = 2;
int quantidadeCompra = 0;
bool possivelVenda = quantidadeCompra > 0 && quantidadeEstoque >= quantidadeCompra;

Console.WriteLine($"Quantidade em estoque: {quantidadeEstoque}");
Console.WriteLine($"Quantidade compra: {quantidadeCompra}");
Console.WriteLine($"É possível realizar a venda? {possivelVenda}");

if(quantidadeCompra == 0){
    Console.WriteLine("Venda inválida");
}
else if (possivelVenda)
{
    Console.WriteLine("Venda realizada");
}
else
{
    Console.WriteLine("Desculpe, não temos a quantidade desejada em estoque.");
}

Console.WriteLine("-------------------------");

Console.WriteLine("Digite uma letra: ");
string letra = Console.ReadLine();

if (letra == "a" ||
    letra == "e" ||
    letra == "i" ||
    letra == "o" ||
    letra == "u")
{
    Console.WriteLine("Vogal");
}
else
{
    Console.WriteLine("Não é vogal.");
}

Console.WriteLine("-------------------------");

switch(letra)
{
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        Console.WriteLine("vogal");
        break;
    default: 
        Console.WriteLine("Não é uma vogal");
        break;
}