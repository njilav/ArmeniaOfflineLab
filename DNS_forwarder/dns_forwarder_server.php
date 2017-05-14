<?php
$query = '';
$server = '8.8.8.8';
$port = 53;
$response = '';

if(!(isset($_POST['query']) || isset($_GET['query']))) {
	die();
}
else if(isset($_POST['query'])) {
	$query = $_POST['query'];
}
else {
	$query = $_GET['query'];
}
$data = base64_decode($query);

$fp = stream_socket_client("udp://".$server.":".$port, $errno, $errstr);
if (!$fp) {
    echo "ERROR: $errno - $errstr<br />\n";
}
else {
    fwrite($fp, $data);
    $response = fread($fp, 200000);
    fclose($fp);
}

echo base64_encode($response);

?>
