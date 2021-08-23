<?php
    include "mysql.php";
    session_start();
    if ($_SESSION["uid"]) {
        header("Location: home.php");
    }
    $errMsg = "";
    if (isset($_POST['submit'])) {
        $username = $_POST["username"];
        $password = md5($_POST["password"]);
        if (strpos($username, ' ') || preg_match('/[\'^£$%&*()}{@#~?><>,|=+¬-]/', $username)) {
            $errMsg = "Username can contain only alphabets, numbers & underscore (_)";
        } else {
            $query = "SELECT * FROM users WHERE username='$username'";
            $userData = mysqli_query($connection, $query);
            if (mysqli_num_rows($userData) > 0) {
                $user = mysqli_fetch_array($userData);
                if ($user['password'] === $password) {
                    $errMsg = "Success !";
                    $_SESSION["uid"] = $user["uid"];
                    header("Location: home.php");
                } else {
                    $errMsg = "Username and password didn't match !";
                }
            } else {
                $errMsg = "User doesn't exist ! Please create an account.";
            }
        }
    }
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/index.css" />
    <link rel="stylesheet" href="assets/css/portal.css" />
    <title>Notes | Login</title>
</head>
<body>
    <img src="assets/img/notes.svg" />
    <form class="portal" method="POST" action="">
        <h2><?php include "templates/icon.html" ?> Login</h2>
        <fieldset>
            <legend><label for="username">Username</label></legend>
            <input id="username" name="username" type="text" />
        </fieldset>
        <fieldset>
            <legend><label for="password">Password</label></legend>
            <input id="password" name="password" type="password" />
        </fieldset>
        <p class="portalErr"><?php echo $errMsg ?></p>
        <nav>
            <a href="signup.php">Create an account ?</a>
            <input name="submit" type="submit" value="Login" />
        </nav>
    </form>
</body>
</html>