
var arrRooms
var arrDataServer

function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;
    
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    
    // Get all elements with class="navbar-tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("navbar-tablinks");
    for (i = 0; i <  tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += "active";
    if (tabName == "dataBlock") {
      generateDataAside();
    }
    
}

function getDataFromServer(sync) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      arrDataServer = JSON.parse(this.responseText);
    }
  };
  xmlhttp.open("GET", "data.php", sync);
  xmlhttp.send();
}

function postDataFromServer(sync) {
  alert("POST");
}

function generateDataAside() {
  arrRooms = undefined;
  //alert("generateDataAside");
  getDataFromServer(false);
  arrRooms = arrDataServer;
  var rooms = arrRooms;
  //alert(rooms + " lol");
  document.getElementById("test2").innerHTML = rooms;
  //create button for every element in rooms
  for (room in rooms) {
    var btn = document.createElement("button");
    btn.setAttribute("onclick", "selectButtonDataAside(" + rooms[room] + ")");
    var li = document.createElement("li");
    li.innerHTML = rooms[room];
    btn.appendChild(li);
    document.getElementById("dataSearchList").appendChild(btn);
  }
}

function selectButtonDataAside(room) {
  document.getElementById("test2").innerHTML = "You are looking at the data of room: ";
  document.getElementById("test3").innerHTML = room;
}