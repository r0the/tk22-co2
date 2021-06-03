<html>
<body>
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

?>

Select Room:
<form method="POST">
  <input list="froom" name = "froom">
  <datalist id="froom">


<?php
#echo "Connected successfully";


$sql = "SELECT Room FROM devices";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
		?>

		<option value="<?php echo $row['Room']; ?>">  
		<?php echo $row['Room']; ?>
        </option> 	
		
		<?php

	}
	
}
else {
  echo "0 results";
}

?>
<option value="Select all">
		Select all
		</option>
		
		<br>
</datalist>
<input type="submit" name="submit"/>
</form>
<?php

if(isset($_POST['submit'])) {
	$room = $_POST["froom"];
	$currentoptions = "SELECT Alarm, Config FROM devices WHERE Room='$room'";
	$resultcur = $conn->query($currentoptions);

	if ($resultcur->num_rows > 0) {
	// output data of each row
		while($row = $resultcur->fetch_assoc()) {
			?>
			<h4> Current Options: </h4>
			<h5> Room: <?php echo $room ?> </h5>
			<p> <?php echo "Alarm Settings: " . $row["Alarm"]?></p>
			<p> <?php echo " Config settings: " . $row["Config"]; ?></p>
			<p> <?php 
			if ($row["Config"] = "1"){
				echo " Updated: Yes";
			}
			else{
				echo " Updated: No";
			}	
				?></p>
			<br>
			<h4>Change Settings</h4>
			<br>
			<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
			Alarm: <input type="text" name="fal">
			Config:  <input type="text" name="fconf">
			<input type="submit" name = "update">
			</form>
			
		<?php
  }
} else {
  echo "0 results";
}
echo $room;
}	
if(isset($_POST['update'])) {
	$room = $_POST["froom"];
	$fconf = $_POST["fconf"];
	$fal = $_POST["fal"];
	$update = "UPDATE devices SET Updated= '0' WHERE Room = '$room'";
	$updateconf = "UPDATE devices SET Config= '$fconf' WHERE Room = '$room'";
	$updateal = "UPDATE devices SET Alarm= '$fal' WHERE Room = '$room'";
	
	echo $update, $updateconf, $updateal;

	if ($conn->query($update) === TRUE and $conn->query($updateconf) === TRUE and $conn->query($updateal) === TRUE) {
		
		echo "Done! Settings will be updated on next Connection";
	} else {
		echo "Error updating : " . $conn->error;
}}
?>

</body>
</html>