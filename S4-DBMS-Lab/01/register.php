<?php
    include "dbConnection.php";

    $regNo = $_POST["regNo"];
    $name = $_POST["name"];
    $emailId = $_POST["emailId"];
    $phoneNo = $_POST["phoneNo"];

    $query = "INSERT INTO students (regNo, name, emailId, phoneNo) VALUES ('$regNo', '$name', '$emailId', '$phoneNo');";
    mysqli_query($connection, $query);

    echo "<br /><div style='text-align: center; font-size: 25px;'>";
        echo "<p style='font-size: 30px;'>Student <b>$name</b> registered !</p>";
        echo "<a href='/students/display.php'><b>Display all Students</b></a>";
        echo "<br /><br />";
        echo "<a href='/students/'><b>Register new Student</b></a>";
    echo "</div>";
?>