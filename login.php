<?php
    // $conn = mysqli_connect("localhost","root");
    // mysqli_select_db($conn ,'CE');
    // session_start();
    $username = $_POST['Username'];
    $password = $_POST['Password'];
    // $result = mysqli_query($conn,"select *from member where Username = '$username' and Password = '$password'");
    // $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
    // $count = mysqli_num_rows($result);
    $_SESSION['un']=$username;
    if($username=="admin" && $password=="123") {
        echo "<h1><center>
        Logged In Succesfully<br/>
        </center></h1>";
        header( "refresh:1; url=a.php?' . SID . '" );
    }
    else {
            echo "<h1><center>
            Invalid Username/Password<br />
            Please Try Again
            </center></h1>";
            header( "refresh:1; url=account.php" );
    }
?>
