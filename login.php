<?php
$valid_username = "admin";
$valid_password = "password123";

// You can simulate a flawed SQL query by not properly sanitizing user inputs
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Simulating SQL Query
    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

    // Flawed validation: no input sanitization or prepared statements

    if ($username == 'admin' && $password == 'password123' || $username == 'admin' && $password == "password' OR '1'='1") {
        echo "<h1>Success!</h1>";
        echo "<p>HEIST{golden_getaway_88}</p>";  // Flag hidden here
    } else {
        echo "<h1>Login Failed</h1>";
        echo "<p>Incorrect username or password</p>";
    }
}
?>
