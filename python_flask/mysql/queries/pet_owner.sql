USE pets_db;
SELECT * FROM owners;
INSERT INTO owners (fname, lname, email) VALUES ('Brandon', 'Reed', 'reed@yahoo.com');
INSERT INTO owners (fname, lname, email) VALUES ('Jackie', 'Maxey', 'maxey@yahoo.com');
INSERT INTO owners (fname, lname, email) VALUES ('Noah', 'Reed', 'noah@yahoo.com');
INSERT INTO owners (fname, lname, email) VALUES ('Gimli', 'M', 'm@m.com');

SELECT * FROM dogs;
INSERT INTO dogs (name, type, age, owners_id) VALUES ('Hollister', 'Affin Pincher', '14', 1);
INSERT INTO dogs (name, type, age, owners_id) VALUES ('Roxy', 'Mix', '6', 10);
INSERT INTO dogs (name, type, age, owners_id) VALUES ('Apacalypto', 'Doberman', '11', 11);

SELECT * FROM dogs
WHERE id = 5;

UPDATE dogs SET type = 'PUG'
WHERE id = 5;

DELETE FROM dogs WHERE id = 5;

SELECT * FROM dogs;
INSERT INTO dogs (name, type, age, owners_id) VALUES ('Apacalypto', 'Doberman', '11', 11);

SELECT * FROM owners
LEFT JOIN dogs ON owners.id = dogs.owners_id;



