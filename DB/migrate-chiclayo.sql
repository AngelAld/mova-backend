-- SQLite
SELECT id,  nombre
FROM Ubicacion_distrito where nombre LIKE 'Chiclayo%';

-- prev: 1, current: 1228

SELECT Propiedades_ubicacionpropiedad.id FROM Propiedades_ubicacionpropiedad WHERE Propiedades_ubicacionpropiedad.distrito_id = 1;

-- IDS: 2, 4, 5, 6, 7, 8, 14

UPDATE Propiedades_ubicacionpropiedad SET distrito_id = 1228 WHERE Propiedades_ubicacionpropiedad.id IN (2, 4, 5, 6, 7, 8, 14);

DELETE FROM Ubicacion_distrito WHERE id = 1;

SELECT id, nombre FROM Ubicacion_provincia WHERE nombre LIKE 'Chiclayo%';

DELETE FROM ubicacion_provincia WHERE id = 1;

SELECT id, nombre FROM Ubicacion_departamento WHERE nombre LIKE 'Lambayeque%';

SELECT id, nombre FROM Ubicacion_distrito WHERE id = 1128;