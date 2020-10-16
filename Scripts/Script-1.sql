CREATE TABLE 7zulu_user_timezones (
`id` int NOT NULL AUTO_INCREMENT,
`username` varchar(100)NOT NULL,
`timezone` varchar(100)NOT NULL,
`time` float,
`record_source` varchar(100)NOT NULL,
`date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);