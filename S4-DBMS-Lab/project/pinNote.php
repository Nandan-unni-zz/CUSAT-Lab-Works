<?php
    include "mysql.php";
    session_start();
    if (isset($_SESSION["uid"])) {
        header("Location: home.php");
    } else {
        header("Location: /notes");
    }
?>