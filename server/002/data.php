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

$functions = array("getRoomNr", "getRoomData");

foreach ($functions as $str) {
  if ($dataReceive['function'] === $str) {
    $str($dataReceive['addInfo']);
  }
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

function getRoomData($room) {
  global $conn;
  $sql = "SELECT * FROM devices WHERE Room=$room";
  $result = $conn->query($sql);
  $row = mysqli_fetch_assoc($result);
  $GLOBALS['output'] = $row;
}


echo json_encode($output);


$conn->close();

?>
