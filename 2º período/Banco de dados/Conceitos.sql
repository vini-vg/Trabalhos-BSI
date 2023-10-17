CREATE DATABASE CONCEITOS;

USE CONCEITOS;

/* Lógico_1XN: */

CREATE TABLE Departamento (
    ID_Depto INT PRIMARY KEY,
    Nome VARCHAR(50),
    Sigla VARCHAR(10)
);

CREATE TABLE Empregado (
    ID_Emp INT PRIMARY KEY,
    Nome VARCHAR(100),
    CPF VARCHAR(20),
    fk_Departamento_ID_Depto INT
);
 
ALTER TABLE Empregado ADD CONSTRAINT FK_Empregado_2
    FOREIGN KEY (fk_Departamento_ID_Depto)
    REFERENCES Departamento (ID_Depto)
    ON DELETE RESTRICT;
    
    INSERT INTO Departamento(ID_Depto, Nome, Sigla)
    VALUES(111, 'Vendas','DV'),
			(222, 'Recursos Humanos', 'RH'),
            (333, 'Marketing', 'DM');
            
SELECT * FROM Departamento;
    
INSERT INTO Empregado (ID_Emp, Nome, CPF, fk_Departamento_ID_Depto)
VALUES (1, 'Maria', '1234567890', 111),
		(2, 'Jose', '2345678901', 222),
        (3, 'Joao', '3456789012', 333);

SELECT * FROM Empregado;

            