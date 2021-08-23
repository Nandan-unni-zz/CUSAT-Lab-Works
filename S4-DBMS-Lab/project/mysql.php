<?php
    $connection = mysqli_connect("localhost", "nandanunni", "9188750806", "notes");
    if (!$connection)
        die("<br /><h1 style='text-align: center;'>Database connection failure !</h1>");

    // CREATE TABLE users (uid INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), username VARCHAR(100) UNIQUE, password VARCHAR(100));
    // CREATE TABLE notes (nid INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(50), content VARCHAR(500), authorId INT, isPinned INT);
?>
