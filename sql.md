
<!-- CREATE TABLE -->
create table appointments (
id SERIAL PRIMARY KEY NOT NULL,
name VARCHAR(200) NOT NULL,
start_datetime TIMESTAMP NOT NULL,
end_datetime TIMESTAMP NOT NULL,
description TEXT NOT NULL,
private BOOLEAN NOT NULL);


<!-- INSERT INTO TABLE -->
INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
VALUES
('My appointment', '2020-12-15 14:00:00', '2020-12-15 15:00:00',
 'An appointment for me', false);