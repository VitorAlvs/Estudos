string  nome    = "Vítor";
int     idade   = 19;
double  altura  = 1.70;
decimal peso    = 50.0M;
bool    condicao= true;

Console.WriteLine(nome);
Console.WriteLine(nome + " tem "  + idade + " anos.");
Console.WriteLine(nome + " tem "  + altura.ToString("0.00") + "m.");
Console.WriteLine(nome + " tem "  + peso + "kg.");
Console.WriteLine("Valor: " + condicao);

Console.WriteLine("-----------------------------");

idade = idade + 1;
Console.WriteLine("Em um ano, " + nome + " terá "  + idade + " anos.");

Console.WriteLine("-----------------------------");

DateTime dataAtual = DateTime.Now;
Console.WriteLine("A data e hora atual são: " + dataAtual);
Console.WriteLine(dataAtual.ToString("dd/MM/yyyy"));
Console.WriteLine(dataAtual.ToString("dd/MM/yyyy HH:mm"));
DateTime dataAmanha = DateTime.Now.AddDays(1);
Console.WriteLine("Em 24 horas serão: " + dataAmanha);