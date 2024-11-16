# php file to process the existing python file
<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {

        $a = escapeshellarg($_GET['a']);
        $b = escapeshellarg($_GET['b']);
        $c = escapeshellarg($_GET['c']);
        $d = escapeshellarg($_GET['d']);
        $e = escapeshellarg($_GET['e']);

        $command = escapeshellcmd("python3 data_management.py $a $b $c $d $e");
        $output = shell_exec($command);

    echo "<h2>Results:</h2>";
    echo "<p>$output</p>";
} else {
    echo "Invalid Request";
}
?>