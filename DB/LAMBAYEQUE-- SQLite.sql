-- SQLite
SELECT id
FROM Ubicacion_departamento
WHERE nombre = 'Lambayeque';
-- SQLite
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (1, "Chiclayo");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (1, "Ferreñafe");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (1, "Lambayeque");
-- SQLite
SELECT nombre
from Ubicacion_provincia
where departamento_id = 1;
--SQLite
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Lambayeque';
--SQLite
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Lambayeque");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Chochope");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Illimo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Jayanca");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Mochumi");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Morrope");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Motupe");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Olmos");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Pacora");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Salas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "San José");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (3, "Tucume");
--SQLite
SELECT nombre
FROM Ubicacion_distrito
WHERE provincia_id = 3;
--SQLite
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Chiclayo';
--SQLite
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Chiclayo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Chongoyape");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Eten");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Eten Puerto");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "José Leonardo Ortiz");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "La Victoria");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Lagunas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Monsefu");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Nueva Arica");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Oyotun");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Picsi");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Pimentel");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Reque");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Santa Rosa");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Saña");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Cayalti");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Patapo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Pomalca");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Pucala");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (1, "Tuman");
--SQLite
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Ferreñafe';
--SQLite
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (2, "Ferreñafe");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (2, "Cañaris");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (2, "Incahuasi");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (2, "Manuel Antonio Mesones Muro");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (2, "Pitipo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (2, "Pueblo Nuevo");