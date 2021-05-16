<?php
    $connection = mysqli_connect("localhost", "nandanunni", "9188750806", "dbms_lab");
    if (!$connection)
        die("<br /><h1 style='text-align: center;'>Database connection failure !</h1>");

    // CREATE TABLE students (regNo INT PRIMARY KEY, name VARCHAR(50), emailId VARCHAR(50), phoneNo VARCHAR(10));
?>