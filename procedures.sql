DELIMITER $$

CREATE PROCEDURE Selecionar_Produtos(IN quantidade INT)
BEGIN
 SELECT * FROM produtos LIMIT quantidade;
END $$

CREATE PROCEDURE Cadastrar_Produto(
	IN p_nome VARCHAR(100),
	IN p_preco DECIMAL (10,2))
BEGIN
 INSERT INTO produtos (nome, preco) 
 VALUES (p_nome, p_preco);
END $$

CREATE PROCEDURE Buscar_Produto(IN termo VARCHAR(100))
BEGIN
 SELECT * FROM produtos 
 WHERE nome LIKE CONCAT('%', termo, '%');
END $$

CREATE PROCEDURE Atualizar_Preco_Produto(
	IN p_id, IN novo_preco DECIMAL(10,2))
BEGIN 
 UPDATE produtos SET preco = novo_preco
 WHERE id = p_id;
END $$

CREATE PROCEDURE Contar_Produtos(OUT total INT)
BEGIN
 SELECT COUNT(*) INTO total FROM produtos;
END $$

DELIMITER;