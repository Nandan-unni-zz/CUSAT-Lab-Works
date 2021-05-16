<?php
    include "dbConnection.php";

    $username = $_POST["username"];
    $password = hash("sha256", $_POST["password"]);

    $query = "SELECT * FROM loginsha WHERE username='$username' AND password='$password'";
    $user = mysqli_query($connection, $query);
    if ($user) {
        if (mysqli_num_rows($user) > 0) {
            $data = mysqli_fetch_array($user);
            echo "<br /><div style='text-align: center; font-size: 25px;'>";
                echo "<p style='font-size: 30px;'>Welcome, <b>".$data["username"]."</b> !</p>";
                echo "<a href='/loginsha/'><b>Logout</b></a>";
            echo "</div>";
        } else {
            include "index.html";
            echo "<p style='text-align: center; color: red; font-size: 20px;'>Incorrect username or password !</p>";
        }
    } else {
        include "index.html";
        echo "<p style='text-align: center; color: red; font-size: 20px;'>".mysqli_error()."</p>";
    }
?>