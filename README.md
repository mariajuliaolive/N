# Soma Multithread com Registro e Visualização

Este projeto implementa uma aplicação multithread para calcular a soma de uma grande lista de números, comparando seu desempenho com uma implementação sequencial. 
Ele também inclui registro detalhado para cada thread e visualiza os resultados usando gráficos e tabelas.

## Funcionalidades
- **Multithreading:** Divide a lista entre múltiplas threads para calcular somas parciais em paralelo.
- **Registro de Threads:** Registra resultados, latências e status de processamento para cada thread.
- **Comparação Sequencial:** Oferece uma linha de base para comparação de desempenho calculando a soma sequencialmente.
- **Visualização:** Gera gráficos para comparação de tempo de execução e resultados das threads.
- **Sincronização:** Utiliza barreiras para garantir que as threads terminem antes que os resultados sejam consolidados.

## Pré-requisitos
- Python 3.x
- Bibliotecas necessárias: `threading`, `time`, `queue`, `random`, `pandas`, `matplotlib`

Para instalar bibliotecas ausentes, execute:
```bash
pip install pandas matplotlib
```

## Como Funciona
1. **Lista de Entrada:** Uma lista de inteiros de 1 a 1000 é dividida entre `n` threads.
2. **Execução das Threads:** Cada thread calcula a soma parcial do segmento atribuído e registra seu resultado e latência.
3. **Servidor Central:** Uma thread central consolida os resultados de todas as threads em uma soma total.
4. **Comparação:** Os tempos de execução para os cálculos sequencial e paralelo são comparados.
5. **Visualização:** Os resultados são exibidos como gráficos e impressos em formato tabular.

## Visão Geral do Código
### Funções
- `soma_parcial`: Calcula a soma parcial para uma thread, simulando latência e registrando resultados.
- `servidor_central`: Consolida os resultados de todas as threads e registra a soma total.
- `main`: Inicializa as threads, sincroniza a execução e retorna o log.
- `soma_sequencial`: Calcula a soma da lista sequencialmente.
- `gerar_graficos`: Gera gráficos comparando tempos de execução sequencial e paralelo e visualiza os resultados das threads.

### Sincronização
O código utiliza:
- **Barreira:** Garante que todas as threads completem seus cálculos antes que o servidor central consolide os resultados.
- **Fila (Queue):** Facilita a comunicação segura entre threads.

## Uso
Execute o programa da seguinte forma:
```bash
python cluster_simulacao.py
```

### Saída
1. **Saída no Console:**
    - Resultados e latência de cada thread.
    - Soma total consolidada pelo servidor.
    - Tempos de execução para os processamentos sequencial e paralelo.

2. **Gráficos e Tabelas:**
    - Gráfico de barras comparando os tempos de execução sequencial e paralelo.
    - Tabela detalhada dos resultados e latências das threads.

## Exemplo de Saída
### Saída no Console
```
Thread 0: Resultado parcial = 5050, Latência = 0.23s
Thread 1: Resultado parcial = 15050, Latência = 0.45s
...
Servidor central: Soma total consolidada = 500500
Tempo Sequencial: 0.0015s
Tempo Paralelo: 0.1350s
```

### Gráficos
1. **Comparação de Tempo de Execução:**
   ![Comparação de Tempo](#)
2. **Resultados das Threads:**
   ![Resultados das Threads](#)

## Personalização
- **Número de Threads:** Modifique `n` na função `main()` para ajustar o número de threads.
- **Tamanho da Lista:** Altere o intervalo da lista de entrada nas funções `main()` ou `soma_sequencial()`.
- **Simulação de Latência:** Ajuste o intervalo da chamada `random.uniform(0.1, 0.5)` em `soma_parcial`.

## Conclusão
Este projeto demonstra o uso de multithreading para melhorar o desempenho em tarefas computacionais, juntamente com sincronização adequada e visualização de resultados.
Serve como um exemplo prático de programação paralela em Python.



