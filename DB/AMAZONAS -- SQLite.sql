-- SQLite
SELECT id,
    nombre
FROM Ubicacion_departamento
WHERE nombre = 'Amazonas';
-- SQLite
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Chachapoyas");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Bagua");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Bongará");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Condorcanqui");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Luya");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Rodríguez de Mendoza");
INSERT INTO Ubicacion_provincia (departamento_id, nombre)
VALUES (2, "Utcubamba");
-- CHACHAPOYAS
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Chachapoyas';
-- id = 4
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Chachapoyas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Asunción");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Balsas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Cheto");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Chiliquin");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Chuquibamba");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Granada");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Huancas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "La Jalca");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Leimebamba");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Levanto");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Magdalena");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Mariscal Castilla");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Molinopampa");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Montevideo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Olleros");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Quinjalca");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "San Francisco de Daguas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "San Isidro de Maino");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Soloco");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (4, "Sonche");
-- BAGUA
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Bagua';
-- id = 5
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (5, "Bagua ");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (5, "Aramango");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (5, "Copallin");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (5, "El Parco");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (5, "Imaza");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (5, "La Peca");
-- BONGARÁ
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Bongará';
-- id = 6
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Jumbilla");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Chisquilla");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Churuja");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Corosha");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Cuispes");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Florida");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Jazan");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Recta");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "San Carlos");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Shipasbamba");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Valera");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (6, "Yambrasbamba");
-- CONDORCANQUI
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Condorcanqui';
-- id = 7
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (7, "Nieva");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (7, "El Cenepa");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (7, "Río Santiago");
-- LUYA
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Luya';
-- id = 8
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Lamud");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Camporredondo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Cocabamba");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Colcamar");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Conila");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Inguilpata");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Longuita");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Lonya Chico");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Luya");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Luya Viejo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "María");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Ocalli");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Ocumal");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Pisuquia");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Providencia");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "San Cristóbal");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "San Francisco de Yeso");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "San Jerónimo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "San Juan de Lopecancha");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Santa Catalina");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Santo Tomas");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Tingo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (8, "Trita");
-- RODRÍGUEZ DE MENDOZA
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Rodríguez de Mendoza';
-- id = 9
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "San Nicolás");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Chirimoto");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Cochamal");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Huambo");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Limabamba");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Longar");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Mariscal Benavides");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Milpuc");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Omia");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Santa Rosa");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Totora");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (9, "Vista Alegre");
-- UTCUBAMBA
SELECT id
FROM Ubicacion_provincia
WHERE nombre = 'Utcubamba';
-- id = 10
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "Bagua Grande");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "Cajaruro");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "Cumba");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "El Milagro");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "Jamalca");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "Lonya Grande");
INSERT INTO Ubicacion_distrito (provincia_id, nombre)
VALUES (10, "Yamon");