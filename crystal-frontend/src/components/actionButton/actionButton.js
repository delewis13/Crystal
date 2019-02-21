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
    email: '',
    feed: ''
  }

  componentClicked = () => console.log('clicked');

  responseFacebook = response => {
    var posts = response.feed.data

    for (var i = 0; i < posts.length; i++) {
        let feed = response.feed.data[i].message
        if(typeof feed !== "undefined"){
          console.log(feed)
        }
      }
    }

  componentDidMount() {
    this.refs.actionButton.disabled = true;
  }

  componentDidUpdate() {
    console.log('hi')
    console.log(this.props.socialMedia)
    if (this.props.socialMedia) {
      this.refs.actionButton.disabled = false;
    } else if (!this.props.socialMedia) {
      this.refs.actionButton.disabled = true
    }
  }

  render() {
    let fbContent;
    return (
      <Button className="action-button" id="action-button" ref="actionButton" onClick={this.handleClick()}>Choose a platform</Button>
    )
  }
}

    if(this.state.isLoggedIn){
      fbContent = null;
    } else {
      fbContent = (
    <FacebookLogin
    appId="375886966477417"
    autoLoad={true}
    fields="name,email,feed"
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
