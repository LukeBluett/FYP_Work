<?php
    session_start();
?>
<html>
    <head>
        <style>
            .main {
                background-color: black;
                color: white;
                text-align: center;
                margin: 10%;
                padding: 5%;
            }
        </style>
    </head>
    <body>
        <div class="main">
            <h1>To Do</h1>
            <br>
            <form action="TD.php" method="post">
                Enter task: 
                <input type="text" name="task">
                
                <input type="submit" value="Submit">
            </form>

            <?php
                if(isset($_SESSION['task'])) {
                    $_SESSION['task'] .= "<br>" . $_POST['task'];
                } else {
                    $_SESSION['task'] = $_POST['task'];
                }
                echo $_SESSION['task'];
            ?>
        </div>
    </body>
</html>