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

    // Declare variables
  var input, filter, ul, li, a, i;
  input = document.getElementById("dataSearch");
  filter = input.value.toUpperCase();
  ul = document.getElementById("dataSearchList");
  button = ul.getElementsByTagName("button");

    // Loop through all list items, and hide those that don't match the search query
  for (i = 0; i < button.length; i++) {
    a = button[i].getElementsByTagName("a").value;
    if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
      button[i].style.display = "";
      document.getElementById("testtest").innerHTML = filter;
    } else {
      button[i].style.display = "none";
    }
  }
}