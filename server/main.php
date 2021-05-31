<!DOCTYPE html>
<html>
<head>
    <title>Main.php</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="basic-layout.css">
    <script src="js-file-main.js"></script>
    <script src="https://kit.fontawesome.com/8d63c9c4a4.js" crossorigin="anonymous"></script>
</head>
<body>
    <nav>
        <div class="navbar-brand navbar-tab">
            <button class="navbar-brandlinks" onclick="openTab(event, 'mainBlock')">CO<sub>2</sub>-Sensor</button>
        </div>
        <div class="navbar-tab">
            <button class="navbar-tablinks" onclick="openTab(event, 'dataBlock')" id="defaultOpen"><i class="far fa-list-alt"></i> Data</button>
            <button class="navbar-tablinks" onclick="openTab(event, 'informationBlock')"><i class="fas fa-info"></i> Information</button>
            <button class="navbar-tablinks" onclick="openTab(event, 'settingsBlock')"><i class="far fa-edit"></i> Settings</button>
            <button class="navbar-tablinks right"><i class="fas fa-sign-in-alt"></i></button>
        </div>
    </nav>
    <main>
        <div id="mainBlock" class="tabcontent">
            <aside class="mainBlock-aside">
                <p>..</p>
            </aside>
            <section class="mainSection">
                <?php
                echo "Hello World!";
                ?>
            </section>
        </div>
        <div id='dataBlock' class="tabcontent">
            <aside class="mainBlock-aside">
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
                <input type="text" id="dataSearch" onkeyup="dataSearch" placeholder="Search.." title="Search for CO2-Sensor">

                <?php
                $sql = "SELECT Room FROM devices";
                $result = mysqli_query($conn, $sql);
                ?>
                
                <ul class="dataSearchList">
                    <?php while($row = mysqli_fetch_assoc($result)) { ?>
                    <button><li>
                        <p><?php echo $row['Room'] ?></p>
                    </li></button>
                    <?php } ?>
                </ul>

            </aside>
            <section class="mainSection">
                <?php
                    $cur_room = 156;
                    $sql = "SELECT ID, Alarm FROM devices WHERE Room=$cur_room";
                    $result = mysqli_query($conn, $sql);
                    echo "Alarm: " . mysqli_fetch_assoc($result)["Alarm"];
                ?>
            </section>
        </div>
        <div id="informationBlock" class="tabcontent">
            <h3>Information-Block</h3>
        </div>
        <div id="settingsBlock" class="tabcontent">
            <h3>Settings-Block</h3>
        </div>
    </main>
    <script>
        document.getElementById("defaultOpen").click();
    </script>
</body>
</html>
