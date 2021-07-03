<?php

    $con = mysqli_connect('localhost','root');
    mysqli_select_db($con ,'CE');

    $email = $_POST["Email"];
    $Username = $_POST["Username"];
    $pass = $_POST["Password"];

    $query = " INSERT INTO member(Username,Email,Password)
    VALUES ('$Username','$email','$pass')";
    mysqli_query($con, $query);

    echo "<h1><center>
    Registration Successful
    </center></h1>";
    header("refresh:2;url=index.html");

?>
