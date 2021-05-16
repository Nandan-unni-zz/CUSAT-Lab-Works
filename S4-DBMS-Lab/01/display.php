<?php
    include "dbConnection.php";

    $query = "SELECT * FROM students";
    $students = mysqli_query($connection, $query);
    $studentsCount = mysqli_num_rows($students);
    
    echo "<style> table, td {border: 1px solid black; border-collapse: collapse; padding: 10px; } </style>";
    echo "<br /><div style='display: flex; flex-direction: column; align-items: center; justify-content: center;'>";
        echo "<table>";
            echo "<tr>";
                echo "<td><b>Register Number</b></td>";
                echo "<td><b>Name</b></td>";
                echo "<td><b>Email Id</b></td>";
                echo "<td><b>Phone Number</b></td>";
            echo "</tr>";

            if ($studentsCount != 0) {
                while ($student = mysqli_fetch_array($students)) {
                    echo "<tr>";
                        echo "<td>".$student['regNo']."</td>";
                        echo "<td>".$student['name']."</td>";
                        echo "<td>".$student['emailId']."</td>";
                        echo "<td>".$student['phoneNo']."</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr>";
                    echo "<td></td>";
                    echo "<td></td>";
                    echo "<td></td>";
                    echo "<td></td>";
                echo "</tr>";
            }
        echo "</table><br /><br />";
        echo "<a style='font-size: 20px;' href='/students/'><b>Register new Student</b></a>";
    echo "</div>";
?>