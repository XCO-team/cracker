<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['psw'];
    $pass = $_POST["uname"];
    if (empty($name)) {
        echo "Name is empty";
    } else {
        if ($name == "kamy" and $pass == "kamy"){
            echo $name;
        }
        else{
            echo "no";
        }
        
    }
}
?>