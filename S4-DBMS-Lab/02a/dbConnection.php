<?php
    $connection = mysqli_connect("localhost", "nandanunni", "9188750806", "dbms_lab");
    if (!$connection)
        die("<br /><h1 style='text-align: center;'>Database connection failure !</h1>");

    // CREATE TABLE loginsha (id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) UNIQUE, password VARCHAR(100));
?>