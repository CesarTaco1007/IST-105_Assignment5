<?php
// Added comments explaining Git branching
// Ensure the request method is GET before processing
if ($_SERVER["REQUEST_METHOD"] == "GET") {

    // Escape user input to prevent command injection
    $a = escapeshellarg($_GET['a']);
    $b = escapeshellarg($_GET['b']);
    $c = escapeshellarg($_GET['c']);
    $d = escapeshellarg($_GET['d']);
    $e = escapeshellarg($_GET['e']);

    // Construct the command to execute the Python script with arguments
    $command = escapeshellcmd("python3 data_management.py $a $b $c $d $e");

    // Execute the command and capture the output from the Python script
    $output = shell_exec($command);

    // Display the output from the Python script in the HTML format
    echo "<h2>Results:</h2>";
    echo "<p>$output</p>";

} else {
    // Handle invalid requests (non-GET requests)
    echo "Invalid Request";
}
?>
