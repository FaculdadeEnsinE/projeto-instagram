-- Colunns:
-- id,caption,media_type,like_count,comments_count,media_url,permalink,timestamp,username

-- Tables:
-- medias


/************************************************************/

-- Quantidade total de mídias
SELECT count(*)
FROM medias

-- Quantidade de mídias por tipo
SELECT media_type,count(*)
FROM medias
GROUP BY media_type
ORDER BY media_type

-- Quantidade total de curtidas
SELECT sum(like_count)
FROM medias

-- Quantidade total de comentários
SELECT SUM(comments_count)
FROM medias

-- Postagens com mais comentários
SELECT *
FROM medias
ORDER BY comments_count DESC
LIMIT 5

-- Postagens com mais antigas
SELECT *
FROM medias
ORDER BY timestamp
LIMIT 1

-- Quantidade de postagens por ano, com o mais curtido e mais comentado
SELECT
	YEAR(timestamp) as ANO,
	count(*) QuantidadePost,
	MAX(like_count) PostMaisCurtido,
	MAX(comments_count) PostMaisComentado
FROM medias
GROUP BY YEAR(timestamp)
ORDER BY YEAR(timestamp)
