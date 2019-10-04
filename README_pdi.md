# pentaho_estudante
Esta é uma aplicação desenvolvida para o desafio de estágio em Engenharia de Dado na GreenMile. O objetivo era desenvolver uma aplicação que criasse tabelas no banco de dados, alimentada via Kettle e que existisse um Job que fosse capaz de percorrer a tabela estudante, capturar os ids dos estudantes inserir na tabela AlreadyRunnedId, preencher tabela LastRun com a informação da data e hora que ocorreu o processo, após executado deve ser criado um arquivo .csv com todas as informações dos estudantes processados.



Setup

O banco de dados PostgresSQL subirá na porta 5432, ficando então acessível através da url http://localhost:15432


Para executar o projeto no seu ambiente de desenvolvimento você precisará atender os seguintes requisitos:

Ter o bando de dados Postgres instalado
Configurar ambiente
Rodar o arquivo script.sql no banco de dados

Ter a ferramenta do Kettle(Pentaho Data Integration) instalada
Configurar o ambiente
Rodar o arquivo job_etl.kjb na aba Jobs

Atualizar o banco de dados

Se preferir pode ser feito exclusões de tuplas para testar a funcionalidade do Job, que percorre a tabela estudante, preenche as tabelas restantes e atualiza o arquivo estudante.csv


