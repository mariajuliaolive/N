import threading
import time
import queue
import random
import pandas as pd
import matplotlib.pyplot as plt


# Função para calcular a soma parcial
def soma_parcial(lista, inicio, fim, resultado_queue, barreira, log, thread_id):
    # Simulação de latência
    latencia = random.uniform(0.1, 0.5)
    time.sleep(latencia)
    resultado = sum(lista[inicio:fim])
    resultado_queue.put((thread_id, resultado, latencia))
    log[thread_id] = {'Resultado': resultado, 'Latência (s)': latencia}
    print(f"Thread {thread_id}: Resultado parcial = {resultado}, Latência = {latencia:.2f}s")
    barreira.wait()


# Função do servidor central
def servidor_central(resultado_queue, n, barreira, log):
    barreira.wait()
    soma_total = 0
    for _ in range(n):
        thread_id, resultado, latencia = resultado_queue.get()
        soma_total += resultado
        log[thread_id]['Consolidado'] = True
    print(f"Servidor central: Soma total consolidada = {soma_total}")
    log['Servidor'] = {'Soma Total': soma_total}


# Função principal
def main():
    n = 10  # Número de threads
    lista = list(range(1, 1001))  # Lista de números
    tamanho_sublista = len(lista) // n


    # Log para registrar informações
    log = {}


    # Queue e Barrier
    resultado_queue = queue.Queue()
    barreira = threading.Barrier(n + 1)


    # Iniciar threads
    threads = []
    for i in range(n):
        inicio = i * tamanho_sublista
        fim = (i + 1) * tamanho_sublista if i < n - 1 else len(lista)
        t = threading.Thread(target=soma_parcial, args=(lista, inicio, fim, resultado_queue, barreira, log, i))
        threads.append(t)
        t.start()


    # Servidor central
    servidor_thread = threading.Thread(target=servidor_central, args=(resultado_queue, n, barreira, log))
    servidor_thread.start()


    for t in threads:
        t.join()
    servidor_thread.join()


    return log


# Função para soma sequencial
def soma_sequencial(lista):
    return sum(lista)


# Gerar gráficos
def gerar_graficos(tempo_seq, tempo_paralelo, log):
    # Gráfico comparativo de tempo
    plt.bar(['Sequencial', 'Paralelo'], [tempo_seq, tempo_paralelo], color=['blue', 'orange'])
    plt.ylabel('Tempo (s)')
    plt.title('Tempo de Execução: Sequencial vs Paralelo')
    plt.show()


    # Tabela com resultados detalhados
    df = pd.DataFrame.from_dict(log, orient='index')
    print("\nTabela de resultados:\n", df)
    df.plot(kind='bar', title='Resultados por Thread')
    plt.show()


if __name__ == "__main__":
    # Soma sequencial
    start_seq_time = time.time()
    soma_total_seq = soma_sequencial(list(range(1, 1001)))
    end_seq_time = time.time()
    tempo_seq = end_seq_time - start_seq_time
    print(f"Soma sequencial: {soma_total_seq}, Tempo: {tempo_seq:.4f}s")


    # Soma paralela
    start_par_time = time.time()
    log = main()
    end_par_time = time.time()
    tempo_paralelo = end_par_time - start_par_time
    print(f"Tempo total de execução paralela: {tempo_paralelo:.4f}s")


    # Gerar gráficos e tabelas
    gerar_graficos(tempo_seq, tempo_paralelo, log)



