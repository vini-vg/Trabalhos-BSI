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
    ON DELETE SET NULL;