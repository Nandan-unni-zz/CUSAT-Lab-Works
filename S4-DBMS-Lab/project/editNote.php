<?php
    include "mysql.php";
    session_start();
    if (isset($_SESSION["uid"])) {
        $id = $_GET['id'];
        if (isset($_POST["edit"])) {
            $title = $_POST['title'];
            $content = $_POST['content'];
            $query = "UPDATE notes SET title='$title', content='$content' WHERE nid='$id';";
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
        <h2><?php include "templates/icon.html" ?> Edit Note</h2>
        <?php 
            $query = "SELECT * FROM notes WHERE nid='$id';";
            $noteData = mysqli_query($connection, $query);
            $note = mysqli_fetch_array($noteData); 
        ?>
        <fieldset>
            <legend><label for="title">Note Title</label></legend>
            <input id="title" name="title" type="text" value="<?php echo $note['title'] ?>" />
        </fieldset>
        <fieldset>
            <legend><label for="content">Note Content</label></legend>
            <textarea name="content" id="content"><?php echo $note['content'] ?></textarea>
        </fieldset>
        <p class="portalErr"><?php echo $errMsg ?></p>
        <nav>
            <a href="home.php">Cancel</a>
            <input name="edit" type="submit" value="Edit Note" />
        </nav>
    </form>
</body>
</html>
<?php
    } else {
        header("Location: /notes");
    }
?>