import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './actionButton.css';
import { Button } from 'react-bootstrap';
import FacebookLogin from 'react-facebook-login/dist/facebook-login-render-props';

class ActionButton extends Component {
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
          content = <div>Please log in to facebook externally</div>;
        } else {
          content = (
            <FacebookLogin
            appId="375886966477417"
            autoLoad={true}
            fields="name,email,feed"
            onClick={this.componentClicked}
            callback={this.responseFacebook}
            render={renderProps => (
              <div onClick={renderProps.onClick}>Facebook</div>
            )}
            />
          )
        }
      } else if (this.props.socialMedia === 'twitter') {
        content = (<div>Twitter</div>)
      }
    } else if (this.props.socialMedia === "") {
    content = (<div>Select a platform</div>)
  }
  return content
}

  render() {
      return (
        <Button className="action-button" id="action-button" ref="actionButton">
          {this.buttonContent()}
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
    socialMedia: state.user.socialMedia
  }
}

export default connect(mapStateToProps)(ActionButton)
