var attempt = 3;
function validate(){
    var username=document.getElementById("Username").value;
    var password=document.getElementById("Password").value;
    if ( username == "admin" && password == "#123"){
        alert ("Login successfully");
        window.location = "index.html"; // Redirecting to other page.
        return false;
        }
        else{
            attempt --;// Decrementing by one.
            alert("You have left "+attempt+" attempt;");
            // Disabling fields after 3 attempts.
            if( attempt == 0){
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;

        }
        }
        }
        