var cur_selected_sensor;

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
}

function getDataFromServer() {
  var objXMLHttpRequest = new XMLHttpRequest();
  var arr;
  objXMLHttpRequest.onreadystatechange = function() {
    if(objXMLHttpRequest.readyState === 4) {
      if(objXMLHttpRequest.status === 200) {
        alert(objXMLHttpRequest.responseText);
        arr = this.responseText;
        document.getElementById("test2").innerHTML = arr;
        document.getElementById("test3").innerHTML = arr[1];
      }
      else {
        alert("Error Code: " + objXMLHttpRequest.status);
        alert('Error Message: ' + objXMLHttpRequest.statusText);
      }
    }
  }
  objXMLHttpRequest.open("GET", "data.php");
  objXMLHttpRequest.send();
}