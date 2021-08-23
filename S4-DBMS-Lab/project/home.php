<?php
    include "mysql.php";
    session_start();
    if (isset($_SESSION["uid"])) {
        $createNoteModal = false;
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/index.css" />
    <link rel="stylesheet" href="assets/css/home.css" />
    <title>Notes | Home</title>
</head>
<body>
    <div class="home">
        <menu>
            <nav>
                <h3>
                    <?php
                        $query = "SELECT * FROM users WHERE uid='".$_SESSION["uid"]."'";
                        $userData = mysqli_query($connection, $query);
                        if (mysqli_num_rows($userData) > 0) {
                            $user = mysqli_fetch_array($userData);
                            echo $user['name'];
                        }
                    ?>
                </h3>
                <a href="home.php" class="navitem">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-file-text"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    <span>Notes</span>
                </a>
                <a href="createNote.php" class="navitem">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-plus-square"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                    <span>Create Note</span>
                </a>
                <a href="logout.php" class="navitem">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-log-out"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                    <span>Logout</span>
                </a>
            </nav>
            <h4><?php include "templates/icon.html" ?><span>Notes</span></h4>
        </menu>
        <main>
            <section class="search"></section>
            <div class="notesContainer">
                <h2 class="sectionTitle">Notes</h2>
                <section class="notes">
                    <?php 
                        $query = "SELECT * FROM notes WHERE authorId='".$_SESSION["uid"]."' AND isPinned=0";
                        $notes = mysqli_query($connection, $query);
                        if (mysqli_num_rows($notes) === 0) {
                            echo "<h3>No notes available !</h3>";
                        }
                        while ($note = mysqli_fetch_array($notes)) {
                    ?>
                        <article class="note">
                            <header><h3><?php echo $note['title']; ?></h3></header>
                            <p><?php echo $note['content']; ?></p>
                            <footer>
                                <a href="pinNote.php?id=<?php echo $note['nid'] ?>">
                                    <abbr title="Pin" class="view">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-flag"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path><line x1="4" y1="22" x2="4" y2="15"></line></svg>
                                    </abbr>
                                </a>
                                <a href="editNote.php?id=<?php echo $note['nid'] ?>">
                                    <abbr title="Edit" class="edit">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
                                    </abbr>
                                </a>
                                <a href="deleteNote.php?id=<?php echo $note['nid'] ?>">
                                    <abbr title="Delete" class="delete">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash-2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
                                    </abbr>
                                </a>
                            </footer>
                        </article>
                    <?php } ?>
                </section>
            </div>
        </main>
    </div>
</body>
</html>
<?php
    } else {
        header("Location: /notes");
    }
?>
