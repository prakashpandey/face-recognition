create database face_recognition

create table face_activity(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, time INT);

insert into face_activity(time) values(1527171361);



create table total_people_detected(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, count INT);

insert into total_people_detected(count) values(1);

update total_people_detected set count=count+1 where id=1;


