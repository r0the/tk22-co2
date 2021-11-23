let btn = document.querySelector('#btn');
let sidebar = document.querySelector('.sidebar');
let searchBtn = document.querySelector('.bx-search');
document.getElementById("defaultOpen");

btn.onclick = function() {
  sidebar.classList.toggle('active');
}
searchBtn.onclick = function() {
  sidebar.classList.toggle('active');
}

function openTabSidebar(evt, tabName) {
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName('tabContent');
  for (i = 0; i < tabcontent.length; i++) {
    if (tabcontent[i].classList.contains('active')) {
      tabcontent[i].classList.toggle('active');
    }
    if (tabcontent[i].classList.contains(tabName)) {
      tabcontent[i].classList.toggle('active');
    }
  }
  if (tabName == 'analytics') {
    generateAnalyticsAside()
  }
}

function searchAnalyticsAside() {
  var filter, ul, a, li, i;
  filter = document.getElementById('analytics_search').value.toUpperCase();
  ul = document.getElementById('analytics_ul');
  li = document.getElementsByClassName('analytics_room_li');

  for (i = 0; i < li.length; i++) {
    if (li[i].id.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = '';
    } else {
      li[i].style.display = 'none';
    }
  }
}

async function getDataFromServer(url, postData) {
    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(postData),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    return await response.json();
}

async function generateAnalyticsAside() {
  rooms = await getDataFromServer('data.php', { function: 'getRoomNr', addInfo: ''});

  console.log(rooms.length);
  if (document.getElementById('analytics_ul').getElementsByTagName('li').length < rooms.length) {
    //create 'a' for every element in Rooms
    for (room in rooms) {
      console.log('1')
      var a = document.createElement('a');
      a.setAttribute('onclick', 'selectAnalyticsDataAside(' + rooms[room] + ')');
      var span = document.createElement('span');
      var i = document.createElement('i');
      i.setAttribute('class', 'bx bxs-microchip');
      var li = document.createElement('li');
      li.setAttribute('class', 'analytics_room_li');
      li.setAttribute('id', rooms[room]);
      var ul = document.getElementById('analytics_ul');
      span.appendChild(document.createTextNode(rooms[room]));
      a.appendChild(i);
      a.appendChild(span);
      li.appendChild(a);
      ul.appendChild(li);
    }
  } else {
    document.getElementById('analytics_search').value = '';
    searchAnalyticsAside();
    console.log('already generated');
  }
}

async function selectAnalyticsDataAside(room) {
  dataRoom = await getDataFromServer("data.php", { function: "getRoomData", addInfo: room });
  document.getElementById("room").innerHTML = "Room: " + dataRoom['Room'];
  document.getElementById("id").innerHTML = "ID: " + dataRoom['ID'];
}
