Claro. Como você vai entregar um **Gerenciador de Tabela de Símbolos**, o README pode ser focado no objetivo da atividade e no funcionamento da sua implementação.

# Avaliação Prática PBL: Componentes de Compiladores

## Gerenciador de Tabela de Símbolos

### Descrição

Este projeto foi desenvolvido como parte da Avaliação Prática PBL da disciplina de Compiladores. O objetivo da atividade é aplicar, de forma prática, conceitos relacionados à construção de compiladores por meio da implementação de um componente específico.

O componente escolhido foi um **Gerenciador de Tabela de Símbolos**, responsável por armazenar e consultar informações sobre variáveis declaradas em diferentes escopos de um programa.

---

## Objetivo

Simular o funcionamento de uma tabela de símbolos utilizada em compiladores, permitindo:

- Criação de escopos aninhados;
- Remoção de escopos;
- Declaração de variáveis com seus respectivos tipos;
- Busca de variáveis em diferentes níveis de escopo;
- Demonstração do conceito de ocultação de variáveis (_shadowing_).

---

## Estruturas de Dados Utilizadas

### Pilha (Stack)

Os escopos são armazenados em uma lista Python (`list`) utilizada como uma pilha.

Operações utilizadas:

- `append()` → Inserção de um novo escopo (Push)
- `pop()` → Remoção do escopo atual (Pop)

O sistema inicia automaticamente com um escopo global ativo, que permanece disponível durante toda a execução da aplicação.

Exemplo:

```python
self.escopos = [{}]
```

### Tabela Hash (Hash Table)

Cada escopo é representado por um dicionário Python (`dict`), que funciona como uma tabela hash.

Exemplo:

```python
{
    "idade": "int",
    "nome": "string"
}
```

Cada chave representa o nome da variável e o valor representa seu tipo.

---

## Funcionalidades

## Observação

Ao iniciar a execução, o sistema cria automaticamente um escopo global. Esse escopo funciona como a base da pilha de escopos e não pode ser removido, garantindo que sempre exista um ambiente válido para armazenamento e consulta de símbolos.

Novos escopos podem ser criados e removidos normalmente, desde que o escopo global seja preservado.

### Criar Escopo

Cria um novo escopo vazio e o adiciona ao topo da pilha.

### Remover Escopo

Remove o escopo atual da pilha, desde que ele não seja o escopo global. O escopo global permanece ativo durante toda a execução do sistema.

### Declarar Variável

Permite cadastrar uma variável associada a um tipo.

Exemplo:

```text
idade -> int
nome -> string
```

### Buscar Variável

Realiza a busca da variável do escopo mais interno para o mais externo.

---

## Tipos Suportados

O sistema aceita os seguintes tipos:

```text
int
float
string
char
bool
```

---

## Exemplo de Funcionamento

### Escopo Global

```text
x -> int
```

### Escopo Interno

```text
x -> float
```

Ao buscar a variável `x` dentro do escopo interno:

```text
Resultado: float
```

Após remover o escopo interno:

```text
Resultado: int
```

Esse comportamento demonstra o conceito de escopos aninhados e ocultação de variáveis.

---

## Menu da Aplicação

```text
1 - Criar escopo
2 - Remover escopo
3 - Declarar variável
4 - Buscar variável
5 - Mostrar tabela de símbolos
0 - Sair
```

---

## Tecnologias Utilizadas

- Python 3
- Estruturas de dados nativas (`list` e `dict`)

---

## Conceitos de Compiladores Aplicados

- Tabela de Símbolos
- Escopos Aninhados
- Pilha de Escopos
- Tabelas Hash
- Busca de Identificadores
- Shadowing (Ocultação de Variáveis)

---

## Conclusão

A implementação demonstra o funcionamento básico de uma tabela de símbolos utilizada por compiladores para armazenar e recuperar informações sobre identificadores. O uso de uma pilha de tabelas hash permite representar adequadamente escopos aninhados e simular o comportamento observado durante a análise semântica de programas.

Esse README já fica com cara de documentação acadêmica e cobre exatamente os conceitos que o professor provavelmente vai procurar ao corrigir o projeto.
