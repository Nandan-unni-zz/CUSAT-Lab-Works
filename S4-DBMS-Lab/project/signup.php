<?php
    include "mysql.php";
    if ($_SESSION["uid"]) {
        header("Location: home.php");
    }
    $errMsg = "";
    if (isset($_POST['submit'])) {
        $name = $_POST["name"];
        $username = $_POST["username"];
        $password = md5(trim($_POST["password"]));
        $cpassword = md5(trim($_POST["cpassword"]));
        if (strpos($username, ' ') || preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $username)) {
            $errMsg = "Username can contain only alphabets, numbers & underscore (_)";
        } elseif (strcmp($password, $cpassword) === 0) {
            $query = "SELECT * FROM users WHERE username='$username';";
            $userData = mysqli_query($connection, $query);
            if (mysqli_num_rows($userData) > 0) {
                $errMsg = "Username already taken !";
            } else {
                $query = "INSERT INTO users (name, username, password) VALUES ('$name', '$username', '$password');";
                $userData = mysqli_query($connection, $query);
                header("Location: /notes");
            }
        } else {
            $errMsg = "Passwords didn't match !";
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/index.css" />
    <link rel="stylesheet" href="assets/css/portal.css" />
    <title>Notes | Signup</title>
</head>
<body>
    <img src="assets/img/notes.svg" />
    <form class="portal" method="POST">
        <h2><?php include "templates/icon.html" ?> Signup</h2>
        <fieldset>
            <legend><label for="name">Name</label></legend>
            <input id="name" name="name" type="text" />
        </fieldset>
        <fieldset>
            <legend><label for="username">Username</label></legend>
            <input id="username" name="username" type="text" />
        </fieldset>
        <fieldset>
            <legend><label for="password">Password</label></legend>
            <input id="password" name="password" type="password" />
        </fieldset>
        <fieldset>
            <legend><label for="cpassword">Confirm Password</label></legend>
            <input id="cpassword" name="cpassword" type="password" />
        </fieldset>
        <p class="portalErr"><?php echo $errMsg ?></p>
        <nav>
            <a href="/notes">Already have an account ?</a>
            <input name="submit" type="submit" value="Signup" />
        </nav>
    </form>
</body>
</html>
