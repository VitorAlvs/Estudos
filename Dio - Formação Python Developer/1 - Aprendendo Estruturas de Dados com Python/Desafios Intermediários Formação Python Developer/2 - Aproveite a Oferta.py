def calc_garrafas_segundo_dia(N, K):
  garrafas_cheias = N//K
  garrafas_vazias = N%K
  total = garrafas_cheias + garrafas_vazias
  return(total)
T = int(input())

for i in range(T):
  i = input()
  i = i.split()
  N = int(i[0])
  K = int(i[1])

  print(calc_garrafas_segundo_dia(N, K))