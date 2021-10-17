// var attempt = 3;
function validate(){
    var username=document.getElementById("Username").value;
    var password=document.getElementById("Password").value;
    if ( username == "admin" && password == "#123"){
        alert ("Login successful");
        window.open( "a.html"); // Redirecting to other page.

        return false;
        }
        else{
            alert("Username or Password incorrect");
            return false;

        }
        }
        
        