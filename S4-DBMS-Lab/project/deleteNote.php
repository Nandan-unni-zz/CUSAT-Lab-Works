<?php
    include "mysql.php";
    session_start();
    if (isset($_SESSION["uid"])) {
        $id = $_GET['id'];
        if (isset($_POST["delete"])) {
            $query = "DELETE FROM notes WHERE nid='$id';";
            mysqli_query($connection, $query);
            header("Location: home.php");
        } elseif (isset($_POST["cancel"])) {
            header("Location: home.php");
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
    <title>Notes | Delete</title>
</head>
<body>
    <form class="portal confirm-dlt" method="POST" action="">
        <p>Are you sure you want to delete the note ?</p>
        <nav>
            <input type="submit" name="delete" value="Delete" />
            <input type="submit" name="cancel" value="Cancel" />
        </nav>
    </form>
</body>
</html>
<?php
    } else {
        header("Location: /notes");
    }
?>