CREATE DATABASE IF NOT EXISTS main;
USE main;

CREATE TABLE IF NOT EXISTS `users`(
    `id`               INT(20) AUTO_INCREMENT,
    `name`             VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO users (name) VALUES ("Tetsuya Aoki");
