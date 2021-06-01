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

function dataSearchFunc() {
  //document.getElementById("testtest").innerHTML = document.getElementById("dataSearch").value;
  var button, filter, li;
  filter = document.getElementById("dataSearch").value.toUpperCase();
  sfilter = filter.toString();
  button = document.getElementById("dataSearchList").getElementsByTagName("button");
  for (i = 0; i++;) {
    li = button[i].getElementsByTagName("li")[0];
    sli = li.toString();
    if (li.innerHTML.toUpperCase().includes("filter")) {
      document.getElementById("test2").innerHTML = "true";
    }
    else {
      document.getElementById("test2").innerHTML = "false";
    }
  }
}