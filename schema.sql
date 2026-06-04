
CREATE DATABASE minhalojatads;

USE minhalojatads;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);

INSERT INTO produtos (nome, preco) VALUES
('Mouse', 50.00),
('Teclado', 120.00),
('Monitor', 900.00),
('Notebook', 3500.00),
('Impressora', 800.00);

select *from produtos;