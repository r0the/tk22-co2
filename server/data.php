<?php

$servername = "localhost";
$username = "root";
$password = "schuan";
$dbname = "co2messen";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
#echo "Connected successfully";

$sql = "SELECT Room FROM devices";
$result = $conn->query($sql);
$list = array();
/*$roomNr = $_REQUEST("roomNr");
if ($roomNr != "") {
  $sql = "SELECT * FROM devices WHERE Room='$roomNr'";
}*/

if ($result->num_rows > 0) {
  // output data of each row
  while($row = mysqli_fetch_assoc($result)) {
		array_push($list, $row["Room"]);
	}
}

echo json_encode($list);
?>
