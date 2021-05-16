<?php
    include "dbConnection.php";

    $username = $_POST["username"];
    $password = md5($_POST["password"]);

    $existing_user = mysqli_query($connection, "SELECT * FROM loginmd WHERE username='$username'");
    if ($existing_user) {
        if (mysqli_num_rows($existing_user) > 0) {
            include "createAccount.html";
            echo "<p style='text-align: center; color: red; font-size: 20px;'>Username already taken !</p>";
        } else {
            $query = "INSERT INTO loginmd (username, password) VALUES ('$username', '$password')";
            mysqli_query($connection, $query);
            echo "<br /><div style='text-align: center; font-size: 25px;'>";
                echo "<p style='font-size: 30px;'>Account created for <b>$username</b> !</p>";
                echo "<a href='/loginmd/'><b>Login</b></a>";
                echo "<br /><br />";
                echo "<a href='/loginmd/createAccount.html'><b>Create new Account</b></a>";
            echo "</div>";
        }
    } else {
        include "createAccount.html";
        echo "<p style='text-align: center; color: red; font-size: 20px;'>".mysqli_error()."</p>";
    }
?>