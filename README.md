# criptografiaSimples

Regras da Criptografia:
O código deve receber uma string e converter todas as letras para maiúsculas.

A substituição deve obedecer às seguintes regras:

Vogais (A, E, I, O, U): devem ser trocadas por outra vogal, contando duas casas à direita na sequência das vogais.
Exemplo:

A → I

E → O

I → U

O → A

U → E

Consoantes (todas as demais letras): devem ser trocadas por outra consoante, contando cinco casas à direita na sequência das consoantes.
Sequência de consoantes para referência:
B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z

Exemplo:

B → H

C → J

D → K

Espaços em branco devem ser substituídos por um hífen ("-").

Qualquer outro caractere (como números, acentos, pontuação etc.) deve ser mantido inalterado.

🔓 Regras da Decriptografia:
A função de decriptografia deve reverter o processo anterior, ou seja:

Vogais voltam duas posições à esquerda na sequência de vogais.

Consoantes voltam cinco posições à esquerda na sequência de consoantes.

O hífen ("-") volta a ser espaço em branco.

Demais caracteres permanecem inalterados.