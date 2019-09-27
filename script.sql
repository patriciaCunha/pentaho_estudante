create database postgres;

CREATE TABLE public.estudante
(
    id integer NOT NULL,
    nome varchar(100),
    matricula integer,
    datamatricula date,
    CONSTRAINT estudante_pkey PRIMARY KEY (id)
);

CREATE TABLE public.alreadyrunnedid
(
    id integer NOT NULL,
    CONSTRAINT alreadyrunnedid_pkey PRIMARY KEY (id)
);

CREATE TABLE public.lastrun
(
    data timestamp without time zone NOT NULL
);

