<?php
    include "mysql.php";
    session_start();
    $errMsg = "";
    if (isset($_POST['login'])) {
        $regno = $_POST["regno"];
        $password = hash("sha512", $_POST["password"]);
        $query = "SELECT * FROM students_20219023 WHERE regno='$regno'";
        $studentData = mysqli_query($connection, $query);
        if (mysqli_num_rows($studentData) > 0) {
            $student = mysqli_fetch_array($studentData);
            if ($student['password'] === $password) {
                $errMsg = "Success !";
                $_SESSION["regno"] = $student["regno"];
                header("Location: student.php");
            } else {
                $errMsg = "Register number and password didn't match !";
            }
        } else {
            $errMsg = "Student with register no $regno is not registered !";
        }
    }
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Student | Login</title>
</head>
<body>
    <div class="central-wrapper">
        <form class="portal" method="POST" action="">
            <h2>Login</h2>
            <div class="portal-item">
                <label>Register Number</label>
                <input name="regno" type="text" required />
            </div>
            <div class="portal-item">
                <label>Password</label>
                <input name="password" type="password" minlength="8" required />
            </div>
            <p style="color: tomato; padding: 20px 0;"><?php echo $errMsg ?></p>
            <nav>
                <a href="./index.php">Create an account ?</a> &nbsp; &nbsp;
                <input name="login" type="submit" value="Login" />
            </nav>
        </form>
    </div>
</body>
</html>
