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

$rawReceive = file_get_contents('php://input');
$dataReceive = (array) (json_decode($rawReceive));

$output = "111";

if ($dataReceive['function'] === "getRoomNr") {
  getRoomNr();
}

function getRoomNr() {
  global $conn;
  $sql = "SELECT Room FROM devices";
  $result = $conn->query($sql);
  $list = array();

  if ($result->num_rows > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
      array_push($list, $row["Room"]);
    }
  }
  $GLOBALS['output'] =  $list;
}

echo json_encode($output);




?>