<?php
    include "mysql.php";
    session_start();
    $errMsg = "";
    if (isset($_POST['upload'])) {
        $regno = $_POST["regno"];
        $name = $_POST["name"];
        $course = $_POST["course"];
        $email = $_POST["email"];
        $phone = $_POST["phone"];
        $semester = $_POST["semester"];
        $description = $_POST["description"];
        $photo = $_FILES["photo"];
        $password = hash("sha512", $_POST["password"]);
        $query = "SELECT * FROM students_20219023 WHERE regno='$regno'";
        $studentData = mysqli_query($connection, $query);
        if (mysqli_num_rows($studentData) > 0) {
            $errMsg = "Register already in use !";
        } else {
            $query = "INSERT INTO students_20219023 (regno, name, course, email, phone, semester, description, photo, password) VALUES ('$regno', '$name', '$course', '$email', '$phone', '$semester', '$description', '$photo', '$password');";
            mysqli_query($connection, $query);
            header("Location: login.php");
        }
    }
?>
<html lang="en">
<head>
    <link rel="stylesheet" href="styles.css" />
    <title>Student | Signup</title>
</head>
<body>
    <div class="central-wrapper">
        <form class="portal" method="POST" action="">
            <h2>Signup</h2>
            <div class="portal-item">
                <label>Register Number</label>
                <input name="regno" type="text" required />
            </div>
            <div class="portal-item">
                <label>Name</label>
                <input name="name" type="text" pattern="[A-Za-z]+" maxlength="50" oninvalid="setCustomValidity('Only alphabets are allowed !')" required />
            </div>
            <div class="portal-item">
                <label>Course</label>
                <input name="course" type="text" required />
            </div>
            <div class="portal-item">
                <label>Email</label>
                <input name="email" type="email" required />
            </div>
            <div class="portal-item">
                <label>Phone</label>
                <input name="phone" type="number" min="5000000000" max="9999999999" required />
            </div>
            <div class="portal-item">
                <label>Semester</label>
                <select name="semester" type="text">
                    <option value="s1">Semester 1</option>
                    <option value="s2">Semester 2</option>
                    <option value="s3">Semester 3</option>
                    <option value="s4">Semester 4</option>
                    <option value="s5">Semester 5</option>
                    <option value="s6">Semester 6</option>
                    <option value="s7">Semester 7</option>
                    <option value="s8">Semester 8</option>
                </select>
            </div>
            <div class="portal-item">
                <label>Description</label>
                <textarea name="description"></textarea>
            </div>
            <div class="portal-item">
                <label>Photo</label>
                <input name="photo" type="file" required />
            </div>
            <div class="portal-item">
                <label>Password</label>
                <input name="password" type="password" minlength="8" required />
            </div>
            <p style="color: tomato; padding: 20px 0;"><?php echo $errMsg ?></p>
            <nav>
                <a href="./login.php">Already have an account ?</a>
                <input name="upload" type="submit" value="Upload Student Details" />
            </nav>
        </form>
    </div>
</body>
</html>
