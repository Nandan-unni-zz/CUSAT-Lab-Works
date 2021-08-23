<?php
    include "mysql.php";
    session_start();
    if (isset($_SESSION["uid"])) {
        if (isset($_POST["submit"])) {
            $title = $_POST["title"];
            $content = $_POST["content"];
            $query = "INSERT INTO notes (title, content, authorId, isPinned) VALUES ('".$title."', '".$content."', ".$_SESSION["uid"].", 0);";
            mysqli_query($connection, $query);
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
    <title>Notes | Create Note</title>
</head>
<body>
    <img src="assets/img/notes.svg" />
    <form class="portal createNote" method="POST" action="">
        <h2><?php include "templates/icon.html" ?> Create Note</h2>
        <fieldset>
            <legend><label for="title">Note Title</label></legend>
            <input id="title" name="title" type="text" />
        </fieldset>
        <fieldset>
            <legend><label for="content">Note Content</label></legend>
            <textarea name="content" id="content"></textarea>
        </fieldset>
        <p class="portalErr"><?php echo $errMsg ?></p>
        <nav>
            <a href="home.php">Cancel</a>
            <input name="submit" type="submit" value="Create Note" />
        </nav>
    </form>
</body>
</html>
<?php
    } else {
        header("Location: /notes");
    }
?>
