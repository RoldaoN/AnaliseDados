/* Funções de Agregação */
SELECT * FROM aluno;
SELECT max(valor) FROM aluno;
SELECT min(valor) FROM aluno;
SELECT avg(valor) FROM aluno;
SELECT SUM(valor) FROM aluno;
SELECT MAX(valor), MIN(valor), AVG(valor), SUM(valor) FROM aluno;
SELECT count(*) FROM aluno WHERE sexo='F';
SELECT MAX(valor) FROM aluno WHERE idade > 30;
SELECT MIN(valor) FROM aluno WHERE ativo!='N';

/* Retorne a idade minima, maxima, soma das idades e média das idades das pessoas com mais de 25 anos*/
SELECT MIN(idade), MAX(idade), SUM(idade), AVG(idade)
FROM aluno
WHERE idade > 25;

/* Apelidando! */
SELECT 	MIN(idade) as idade_minima, 
		MAX(idade) as idade_maxima, 
		SUM(idade) as soma_idades, 
        AVG(idade) as media_idades
FROM aluno
WHERE idade > 25;

/* Ceil - Arredonda para cima*/
SELECT CEIL(17.4) as valor;
SELECT CEIL(17.1) as valor;
SELECT CEIL(17.0) as valor;

/* Floor - Arredonda para baixo*/
SELECT FLOOR(17.4) as valor;
SELECT FLOOR(17.99) as valor;

/* Truncate */
SELECT TRUNCATE(17.9856, 1) as valor;
SELECT TRUNCATE(17.9856, 2) as valor;

/* Round */
SELECT ROUND(17.9856,1) as valor; -- >= 5 Arrendonda
SELECT ROUND(17.9856,2) as valor; -- 5< Não arredonda
SELECT ROUND(17.9856,3) as valor;
SELECT ROUND(17.98563,4) as valor;

/* Agrupamento - Group By*/

SELECT * FROM aluno;
SELECT nome, count(*) as repeticao
FROM aluno
GROUP BY nome;

/* Estados com mais alunos */
SELECT * FROM endereco;
SELECT estado, count(*) as total -- Projetando o estado e a contagem 
FROM endereco -- Acessando a tabela de endereço
GROUP BY estado -- Agrupando por estado
ORDER BY total DESC -- Ordenando do maior para o menor
LIMIT 5; -- Limitando a 5 resultados

/* Cursos mais vendidos/cursos com mais alunos */
SELECT * FROM aluno_curso;
SELECT fk_idcurso, count(*) as total
FROM aluno_curso
GROUP BY fk_idcurso
ORDER BY total DESC;
SELECT * FROM curso;

/* CURDATE retorna a data atual*/
SELECT CURDATE();

/* NOW data atual + hora*/
SELECT NOW();

SELECT date_format(curdate(), '%d/%m/%Y') AS `data`;
SELECT date_format(curdate(), '%D %M %Y') AS `data`; 
/*
%d - Dia do mês (1 a 31)
%D - Dia do mês com o sufixo em inglês. Exemplo: 17th
%m - Número do mês (1 a 12)
%M - Nome do mês em inglês
%y - Ano com dois digitos
%Y - Ano com quatro digitos
*/

/* DATE_ADD: Adiciona um intervalo de tempo

DAY
MONTH
YEAR
SECOND
MINUTE
HOUR*/
SELECT date_add('2003-01-15', interval 10 day) as `data`;
SELECT date_add('2003-01-15', interval 4 month) as `data`;
SELECT date_add('2003-01-15', interval 4 year) as `data`;
SELECT date_add('2003-01-15 15:28:12', interval 4 second) as `data_hora`;
SELECT date_add('2003-01-15 15:28:12', interval 10 minute) as `data_hora`;
SELECT date_add('2003-01-15 15:28:12', interval 3 hour) as `data_hora`;

/*DATEDIFF - Retorna a diferença em dias de duas datas.*/
SELECT
	'1998-08-24' as data_nascimento,
    curdate() as data_atual,
    datediff(curdate(), '1998-08-24') as diferenca_dias,
    floor(datediff(curdate(), '1998-08-24')/365) as idade;

/* dayofyear: Retorna o dia do ano */
SELECT dayofyear('2015-06-18');

/* Calculando a idade*/
-- timestamp (marca temportal) inicio em 01/01/1970
SELECT timestampdiff(YEAR,'1986-01-15', curdate()) as idade;
SELECT 
	data_nascimento,
    curdate() as data_atual,
    idade,
    timestampdiff(YEAR, data_nascimento, curdate()) as idade_atual
FROM 
	aluno;
ALTER TABLE aluno DROP idade;

/* Calculando o dia de Aniversário*/
SELECT * FROM aluno;
SELECT
	idaluno,
    nome,
    data_nascimento,
    -- extract(month from data_nascimento) as data_nasc_mes,
    -- extract(day from data_nascimento) as data_nasc_dia,
    curdate() as data_atual,
    -- extract(month from curdate()) as data_atual_mes,
	-- extract(day from curdate()) as data_atual_dia,
    timestampdiff(YEAR, data_nascimento, curdate()) as idade
FROM
	aluno
WHERE
	extract(day from curdate()) = extract(day from data_nascimento)
    AND
    extract(month from curdate()) = extract(month from data_nascimento);
    
UPDATE aluno SET data_nascimento = '1982-12-18' where idaluno = 2;

alter table aluno_curso modify column data_inscricao datetime default current_timestamp;

select * from aluno_curso;

alter table aluno_curso drop column idalunocurso;

alter table aluno_curso add constraint pk_aluno_curso primary key(fk_idaluno, fk_idcurso, data_inscricao);