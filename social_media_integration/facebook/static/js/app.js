function logout(){
  FB.logout(function(response) {
    FB.Auth.setAuthResponse(null, 'unknown');

  });
}

function getUserData() {
	FB.api('/me', {fields: 'name,email,feed'}, (response) => {
		document.getElementById('response').innerHTML = 'Hello ' + response.name;
    var posts = response.feed.data
    //console.log(response.feed.data)
    var postsL = posts.length;
    //console.log(postsL)
    for (var i = 0; i < postsL; i++) {
        var post_feed = response.feed.data[i].message;
        for(var j = 0; i <posts.length; i++ ){

          // these are the Facebook feed
          feed = response.feed.data[i].message
          if(typeof feed !== "undefined"){
            var header = document.createElement('h1');
            header.appendChild(document.createTextNode(feed));
            document.body.appendChild(header);
          }
        }
    }
	});
}

window.fbAsyncInit = () => {
	//SDK loaded, initialize it
	FB.init({
		appId      : '375886966477417', // developer account
		xfbml      : true,
    cookies    : true,
		version    : 'v3.2'
	});
};

//load the JavaScript SDK
(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  //add event listener to login button
  document.getElementById('loginBtn').addEventListener('click', () => {
    FB.login(function(response) {
      console.log(response.status)
      getUserData();
    }, {scope: 'public_profile,email'});
  }, false);
