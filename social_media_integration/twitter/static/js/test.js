function server(){
  let url = "/acceleration_get"
    $.getJSON(
    url,
    function(data) {
        $('#Result').text(data);
        getAcceleration(data);
    }
  );
}
setInterval(server, 5000)
function getAcceleration(accel) {
  if(accel != null){
    acceleration = accel['accel']
    timestamp = accel['timestamp']
    sessionID = accel['sessionID']

    last_time = timestamp[timestamp.length - 1];
    day = getDay(last_time)

    if (day == "Tuesday"){
      var x=document.getElementById('myTable').rows[parseInt(1,10)].cells;
      x[parseInt(2,10)].innerHTML=sessionID
    }



    //graph(acceleration)
  }

  return accel
}

function getDay(last_time){
  var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var now = new Date();
  var day = days[ now.getDay(last_time) ];

  return day
}
day = getDay()
console.log(day);






// Time difference
function timeDifference(first_time, last_time) {
  var date1 = '2019-02-05 15:57:38.001';
  var date2 = '2019-02-05 15:59:55.001';
  var d2 = new Date(date2);
  var d1 = new Date(date1);
    var sec_num = (d2 - d1) / 1000;
    var days    = Math.floor(sec_num / (3600 * 24));
    var hours   = Math.floor((sec_num - (days * (3600 * 24)))/3600);
    var minutes = Math.floor((sec_num - (days * (3600 * 24)) - (hours * 3600)) / 60);
    var seconds = Math.floor(sec_num - (days * (3600 * 24)) - (hours * 3600) - (minutes * 60));

    if (hours   < 10) {hours   = "0"+hours;}
    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}

    return  days+':'+ hours+':'+minutes+':'+seconds;
}
session_duration = timeDifference()
console.log(session_duration)
