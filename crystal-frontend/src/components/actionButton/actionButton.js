import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './actionButton.css';
import { Button } from 'react-bootstrap';
import FacebookLogin from 'react-facebook-login';

export default class ActionButton extends Component {
  state = {
    isLoggedIn: false,
    userId: ' ',
    name: '',
    feed: ''
  }

  //componentClicked = () => console.log('clicked');

  responseFacebook = response => {
    console.log(response)
    let allMessages = [];

    // list which is used to send to backend (prediction model)
    let messagesList = [];

    var posts = response.feed.data;
    // iterate through user posts feed
    for (var i = 0; i < posts.length; i++) {
          // get the message
          let feed = response.feed.data[i].message;
          // if post is not undefined (a picture/video or a like)
          if(typeof feed !== "undefined"){
            console.log(feed);

            allMessages.push(feed)
          } else {
            console.log('Post is not a message that contains readable text');
          }
      }
      /* all messages have been collected and stored into a list
      randomly select 50 message from list and store to another list */
      for (var i = 0; i < 50; i++){
        // get random message from list
        var random = allMessages[Math.floor(Math.random()*allMessages.length)]
        // add random message to messagesList
        messagesList.push(random)
      }
    }

  render() {
    let fbContent;

    if(this.state.isLoggedIn){
      fbContent = null;
    } else {
      fbContent = (
    <FacebookLogin
    appId="375886966477417"
    autoLoad={false}
    fields="name, feed"
    onClick={this.componentClicked}
    callback={this.responseFacebook}
    />
);

    }
      return (
        <div>{fbContent}</div>
        // <Button onClick={this.handleClick()}/>
      )
    }
  }

//   handleClick() {
//     if (this.props.socialMedia === 'facebook') {
//       console.log('Querying facebook...')
//     } else if (this.props.socialMedia === 'twitter') {
//       console.log('Querying twitter...')
//     }
//   }
//
//   render() {
//     return (
//       <Button onClick={this.handleClick()}/>
//     )
//   }
// }

// const mapStateToProps = (state) => {
//   return {
//     socialMedia: state.socialMedia
//   }
// }
//
// export default connect(mapStateToProps)(ActionButton)
