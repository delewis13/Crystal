import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './actionButton.css';
import { Button } from 'react-bootstrap';
import FacebookLogin from 'react-facebook-login/dist/facebook-login-render-props';
import { addUserPosts, loading, changeSocialMedia, selected } from '../../actions/user'
import request from 'request';
import { personToNumber } from '../dashboard/personalityDescriptors'

class ActionButton extends Component {
  state = {
    isLoggedIn: false,
    userId: ' ',
    name: '',
    email: '',
    feed: ''
  }

  reset = () => {
    if (this.props.selected > 0) {
      this.props.dispatch(addUserPosts(''))
      this.props.dispatch(loading(false))
      this.props.dispatch(changeSocialMedia(''))
      this.props.dispatch(selected('reset'))
    }
  }

  triggerLoading = () => {this.props.dispatch(loading(true))}

  responseFacebook = (response) => {
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

      // all messages have been collected and stored into a list

      //randomly select 50 message from list and store to another list
      let myLongString = ""
      for (var i = 0; i < 50; i++) {

        // get random message from list
        var random = allMessages[Math.floor(Math.random()*allMessages.length)]
        myLongString += " " + random

        // add random message to messagesList
        messagesList.push(random)
      }

      this.props.dispatch(addUserPosts(messagesList))
      console.log(myLongString)

      // Send request to backend
      const url = window.location.href.split('/')
      let endpoint = 'api/myLongString'
      if (url[2].slice(0,9) === "localhost") {
        endpoint = 'http://localhost:8080/' + endpoint
      } else if (url[2] === "aiae.ml") {
        endpoint = 'https://aiae.ml/' + endpoint
      }
      console.log(`Fetching endpoint ${endpoint}`)
      fetch(endpoint, {
        method: 'POST'
      }).then((response) => {return response.text()}).then((personality) => {
        let personalityNum = personToNumber[personality];
        this.props.dispatch(selected(personalityNum))
        this.props.dispatch(loading(false))
      })

      // fetch(`localhost:5000/api/myLongString`, {
      //   method: 'POST'
      //   }).then((response) => {
      //     console.log(response)
      //     let personality;
      //     // Somehow get our string
      //     let personalityNum = personToNumber[personality];
      //     this.props.dispatch(selected(personalityNum))
      //   })
    }

  componentDidMount() {
    this.refs.actionButton.disabled = true;
  }

  componentDidUpdate() {
    if (this.props.socialMedia) {
      this.refs.actionButton.disabled = false;
    } else if (!this.props.socialMedia) {
      this.refs.actionButton.disabled = true
    }
  }

  buttonContent() {
    let content;
    if (this.props.socialMedia !== "") {
      if (this.props.socialMedia === 'facebook') {
        if (this.state.isLoggedIn) {
          content = <h4>Please log in to facebook externally</h4>;
        } else {
          return (
            <FacebookLogin
            appId="2234128353535616"
            autoLoad={false}
            fields="name,email,feed"
            onClick={this.triggerLoading}
            callback={this.responseFacebook}
            render={renderProps => (
              <h4 onClick={renderProps.onClick}>Facebook</h4>
            )}
            />)
        }
      } else if (this.props.socialMedia === 'twitter') {
        content = (<h4>Twitter</h4>)
      }
    } else if (this.props.socialMedia === "") {
    content = (<h4>Select a platform</h4>)
  }
  return content
}

  render() {
      return (
        <Button className="action-button" id="action-button" ref="actionButton" onClick={this.reset}>
        { (this.props.selected > 0) ?
          <div>Reset</div>
        : this.buttonContent() }
        </Button>
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

const mapStateToProps = (state) => {
  return {
    socialMedia: state.user.socialMedia,
    selected: state.user.selected
  }
}

export default connect(mapStateToProps)(ActionButton)
