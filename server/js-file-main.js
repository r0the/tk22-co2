
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

async function getDataFromServer(url, postData) {
  const response = await fetch(url, {
    method: 'POST',
    body: JSON.stringify(postData),
    headers : {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  return await response.json()

  /*
  if (response.ok) {
    // get the response body (the method explained below)
    let returnedData = await response.json();
    return returnedData;
  } else {
    alert("HTTP-Error: " + response.status);
  }*/
}

function postDataFromServer(sync) {
  alert(sync);
}

async function generateDataAside() {
  console.log("generateDataAside");
  rooms = await getDataFromServer("data.php", { function: "getRoomNr", addInfo: ""});
  console.log("Rooms: " + rooms);
  document.getElementById("test2").innerHTML = rooms;
  if (document.getElementById("dataSearchList").getElementsByTagName("li").length != rooms.length) {
    //create button for every element in rooms
    for (room in rooms) {
      var btn = document.createElement("button");
      btn.setAttribute("onclick", "selectButtonDataAside(" + rooms[room] + ")");
      var li = document.createElement("li");
      li.textContent = rooms[room];
      btn.appendChild(li);
      document.getElementById("dataSearchList").appendChild(btn);
    }
  }
  else {
    document.getElementById("test3").innerHTML = "buttons already generated";
  }
}

function selectButtonDataAside(room) {
  document.getElementById("test2").innerHTML = "You are looking at the data of room: ";
  document.getElementById("test3").innerHTML = room;
}