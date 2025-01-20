/* Criar um DataBase para guardarmos os dados. */
CREATE DATABASE universidade;

/* Iniciando o DataBase para uso. */
use universidade;

/* Criando a tabela 'aluno' para guardarmos as informações sobre os alunos ao qual estamos trabalhando. */
CREATE TABLE aluno(
	nome VARCHAR(100),
    idade INT, 
    sexo CHAR(1),
    telefone VARCHAR(15),
    endereco VARCHAR(255),
    data_inscricao DATE,
    valor DECIMAL(10,2),
    ativo CHAR(1)
);

/* Inserindo dados na tabela 'aluno' para que armazene os dados necessários. */
INSERT INTO aluno(
	nome,
	idade,
    sexo,
    endereco,
    telefone,
    data_inscricao,
    valor,
    ativo
) VALUES
	('João Silva', 20, 'M', 'Rua A, 123', '11982101111', '2024-01-10', 150.00, 'S'),
	('Maria Oliveira', 22, 'F', 'Avenida B, 456', '21987654321', '2024-02-15', 200.00, 'S'),
	('Carlos Santos', 19, 'M', 'Rua C, 789', '31987654321', '2024-03-20', 180.00, 'S'),
	('Ana Souza', 21, 'F', 'Praça D, 101', '42987654321', '2024-04-25', 220.00, 'S'),
	('Paulo Almeida', 23, 'M', 'Rua E, 202', '53987654321', '2024-05-30', 160.00, 'S'),
	('Cláudia Lima', 18, 'F', 'Avenida F, 303', '64987654321', '2024-06-05', 210.00, 'S'),
	('Lucas Pereira', 24, 'M', 'Rua G, 404', '75987654321', '2024-07-10', 190.00, 'S'),
	('Fernanda Costa', 25, 'F', 'Rua H, 505', '86987654321', '2024-08-15', 170.00, 'S'),
	('Ricardo Silva', 26, 'M', 'Avenida I, 606', '97987654321', '2024-09-20', 230.00, 'S'),
	('Juliana Rocha', 27, 'F', 'Rua J, 707', '1087654321', '2024-10-25', 240.00, 'S'),
	('Eduardo Martins', 29, 'M', 'Praça K, 808', '2187654321', '2024-11-10', 250.00, 'S'),
	('Patrícia Oliveira', 30, 'F', 'Rua L, 909', '3287654321', '2024-12-01', 260.00, 'S'),
	('Marcos Costa', 31, 'M', 'Avenida M, 1010', '4387654321', '2024-01-15', 270.00, 'S'),
	('Rita Santos', 32, 'F', 'Rua N, 1111', '5487654321', '2024-02-20', 280.00, 'S'),
	('Gustavo Almeida', 33, 'M', 'Rua O, 1212', '6587654321', '2024-03-25', 290.00, 'S'),
	('Isabela Lima', 34, 'F', 'Avenida P, 1313', '7687654321', '2024-04-30', 300.00, 'S'),
	('Felipe Rocha', 35, 'M', 'Rua Q, 1414', '8787654321', '2024-05-05', 310.00, 'S'),
	('Luciana Pereira', 36, 'F', 'Rua R, 1515', '9887654321', '2024-06-10', 320.00, 'S'),
	('Thiago Martins', 37, 'M', 'Avenida S, 1616', '10987654321', '2024-07-15', 330.00, 'S'),
	('Jéssica Souza', 38, 'F', 'Rua T, 1717', '11987654321', '2024-08-20', 340.00, 'S');

/* Adicionando o campo 'cpf' a tabela 'aluno'. */
ALTER TABLE aluno ADD cpf VARCHAR(11);

/* Adicionando o campo 'email' a tabela 'aluno'. */
ALTER TABLE aluno ADD email VARCHAR(150) AFTER idade;

/* Adicionando o campo 'idaluno' na tabela 'aluno' como chave primaria. */
ALTER TABLE aluno ADD idaluno INT PRIMARY KEY AUTO_INCREMENT;

/* Criando a tabela 'telefone' para complementar a tabela 'aluno'. */
CREATE TABLE telefone(
	idtelefone INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(15),
    tipo char(1)
);

/* Droppando a coluna 'telefone' da tabela 'aluno', visto que criamos uma tabela separada. */
ALTER TABLE aluno DROP COLUMN telefone;

/* Criando uma coluna na tabela 'telefone' para que entre com a chave estrangeira (id da tabela 'aluno') 
para relacionar cada aluno ao seu respectivo telefone. */
ALTER TABLE telefone ADD COLUMN fk_idaluno INT;

/* Colocando a chave estrangeira na tabela 'telefone'. */
ALTER TABLE telefone ADD CONSTRAINT fk_aluno_telefone
	FOREIGN KEY (fk_idaluno) REFERENCES aluno(idaluno);

/* Criando a tabela 'endereco' para complementar a tabela 'aluno'. */
CREATE TABLE endereco(
	idendereco INT AUTO_INCREMENT PRIMARY KEY,
    logradouro VARCHAR(100),
    numero VARCHAR(10),
    complemento VARCHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(100),
    estado CHAR(2),
    fk_idaluno INT
);

/* Colocando a chave estrangeira na tabela 'endereco'. */
ALTER TABLE endereco ADD CONSTRAINT fk_aluno_endereco
	FOREIGN KEY(fk_idaluno) REFERENCES aluno(idaluno);

/* Adicionando na tabela 'aluno' campos de endereço. */
ALTER TABLE aluno
ADD logradouro VARCHAR(100),
ADD numero VARCHAR(10),
ADD complemento VARCHAR(20),
ADD bairro VARCHAR(50),
ADD estado CHAR(2),
ADD cidade VARCHAR(100);

/* Puxando da tabela 'aluno' os campos relacionados ao endereço para inserir na tabela 'endereco'. */
INSERT INTO endereco(logradouro, numero, complemento, bairro, estado, cidade, fk_idaluno)
SELECT logradouro, numero, complemento, bairro, estado, cidade, idaluno
FROM aluno;

/* Droppando os campos de endereco da tabela 'aluno'. */
ALTER TABLE aluno
DROP COLUMN logradouro,
DROP COLUMN numero,
DROP COLUMN complemento,
DROP COLUMN bairro,
DROP COLUMN cidade,
DROP COLUMN estado;

/* Droppando a coluna endereço da tabela 'aluno'. */
alter table aluno drop column endereco;

/* Criando a tabela 'curso' para complementar a tabela 'aluno'. */
CREATE TABLE curso(
	idcurso INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50)
);

/* Criando a tabela 'aluno_curso' para relacionar a tabela 'aluno' com a tabela 'curso'. */
CREATE TABLE aluno_curso(
	idalunocurso INT AUTO_INCREMENT PRIMARY KEY,
    fk_idaluno INT,
    fk_idcurso INT
);

/* Colocando a chave estrangeira de 'aluno' na tabela 'aluno_curso'. */
ALTER TABLE aluno_curso ADD CONSTRAINT fk_aluno_curso
	FOREIGN KEY(fk_idaluno) REFERENCES aluno(idaluno);

/* Colocando a chave estrangeira de 'curso' na tabela 'aluno_curso'. */
ALTER TABLE aluno_curso ADD CONSTRAINT fk_curso_aluno
	FOREIGN KEY(fk_idcurso) REFERENCES curso(idcurso);

/* Droppando a coluna 'telefone' da tabela 'aluno'. */
ALTER TABLE telefone DROP COLUMN tipo;

ALTER TABLE telefone ADD tipo ENUM('C','F');

ALTER TABLE telefone MODIFY COLUMN numero VARCHAR(15) NOT NULL;
    
	ALTER TABLE telefone MODIFY COLUMN tipo ENUM('C','F') NOT NULL;

ALTER TABLE endereco ADD CONSTRAINT uc_endereco_fkidaluno unique(fk_idaluno);

/* Adicionar a data de nascimento */
ALTER TABLE aluno ADD data_nascimento DATE;

alter table aluno_curso add data_inscricao date;
alter table aluno_curso add valor decimal(20,2);

update
	aluno_curso
set
 data_inscricao = (select data_inscricao from aluno where idaluno = 20),
 valor = (select valor from aluno where idaluno = 20)
where
	fk_idaluno = 20;
    
alter table aluno drop valor;
alter table aluno drop data_inscricao;

desc aluno;

alter table aluno modify column ativo char(1) default 'S';

insert into aluno (sexo, email, nome, cpf, data_nascimento)
values ('M','nathan@gmail.com','Nathan','14524528966','1998-08-24');

insert into aluno (sexo, email, ativo, nome, cpf, data_nascimento)
values ('M','matheus@gmail.com', 'N','Matheus','14524528965','2003-01-15');

select * from aluno;