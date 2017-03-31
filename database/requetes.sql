DROP VIEW IF EXISTS individu_adresse;
CREATE VIEW individu_adresse  AS
SELECT
  i.nom AS nom,
  i.prenom AS prenom,
  a.label AS label,
  c.label AS commune,
  c.cod_pos AS cod_pos,
  p.label AS pays
FROM individu AS i
INNER JOIN adresse AS a ON i.id=a.individu_id
INNER JOIN commune AS c ON a.commune_cod_pos=c.cod_pos AND a.commune_cod_com=c.cod_com
INNER JOIN pays AS p ON a.pays_id=p.id;
