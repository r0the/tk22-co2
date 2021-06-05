<!DOCTYPE html>
<html>
<head>
    <title>Main.html</title>
    <meta charset="utf-8">
    <script src="js-file-main.js"></script>
    <link rel="stylesheet" href="basic-layout.css">
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
                ..
            </section>
        </div>
        <div id='dataBlock' class="tabcontent">
            <aside class="mainBlock-aside">

                Select Room:
                <input type="text" id="dataSearch" onkeyup="dataSearchFunc()" placeholder="Search..." >                
                <ul id="dataSearchList">
                </ul>

            </aside>
            <section class="mainSection">
                <p id="test2"></p>
                <p id="test3"></p>
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
