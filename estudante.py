import psycopg2
import datetime
import csv
import os

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Postgres2018!")
import time

def job():

    if not os.path.exists('estudante.csv'):

        with open('estudante.csv', 'w', newline='\n') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows([['id', 'Nome', 'Matricula', 'DataDeMatricula']])


    while True:
        cur = conn.cursor()
        cur.execute('select id, nome, matricula, datamatricula from estudante')
        tupla_estudante = cur.fetchall()
        lista_estudante = [list(x) for x in tupla_estudante]

        cur.execute('select * from alreadyrunnedid')
        tupla_id = cur.fetchall()
        list_already_runner_id = [x[0] for x in tupla_id]



        for estudante in lista_estudante:
            if estudante[0] not in list_already_runner_id:
                print('Gravou o aluno do id %s' % estudante[0])
                cur.execute("""INSERT INTO lastrun (data) VALUES(%(date)s)""", {"date": datetime.datetime.now()})
                cur.execute("""INSERT INTO alreadyrunnedid (id) VALUES(%(int)s)""", {"int": estudante[0]})
                conn.commit()

                list_csv = []

                with open('estudante.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        list_csv.append(row)

                list_csv.append(estudante)

                with open('estudante.csv', 'w', newline='\n') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=',')
                    for estudante_csv in list_csv:
                        csv_writer.writerows([estudante_csv])

        cur.close()
        time.sleep(2)


        # cur.execute("INSERT INTO alreadyrunnedid (id) VALUES(%s)", (str(estudante[0])))
    print(result)

    cur.close()


    for estudante in result:
        print(estudante)


if __name__ == '__main__':
    print('iniciando o JOB ')
    job()
