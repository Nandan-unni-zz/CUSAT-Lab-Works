<?php
    include "mysql.php";
    session_start();
?>
<html>
    <head>
        <link rel="stylesheet" href="styles.css" />
        <title>Student | Signup</title>
    </head>
    <body>
        <div class="">
        <?php
            $query = "SELECT * FROM students_20219023 WHERE regno='".$_SESSION["regno"]."';";
            $studentData = mysqli_query($connection, $query);
            if (mysqli_num_rows($studentData) > 0) {
                $student = mysqli_fetch_array($studentData);
                echo $student["regno"];
                echo "<br />";
                echo $student["name"];
                echo "<br />";
                echo $student["course"];
                echo "<br />";
                echo $student["semester"];
                echo "<br />";
                echo $student["description"];
            }
        ?>
        </div>
    </body>
</html>
