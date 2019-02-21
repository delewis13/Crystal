import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './socialMedia.css';
import { Button } from 'react-bootstrap'
import { changeSocialMedia } from '../../actions/user'

class SocialMedia extends Component {

  handleClick = (e) => {
    // Add the appropriate highlight classes
    let facebook = document.getElementById('facebook')
    let twitter = document.getElementById('twitter')
    
    e.target.classList.toggle('flex-icon-focus')
    if (e.target.id === 'facebook') {
      twitter.classList.remove('flex-icon-focus')
    } else if (e.target.id === 'twitter') {
      facebook.classList.remove('flex-icon-focus')
    } else {
      alert('Unexpected behaviour')
    }

    // Depending on what classes now exist on the element, dispatch appropriately
    if (e.target.classList.contains('flex-icon-focus')) {
      this.props.dispatch(changeSocialMedia(e.target.name))
    } else {
      this.props.dispatch(changeSocialMedia(""))
    }
  }

  render() {
    return (
      <div className="flex center">
        <img className="flex-icon" src="/img/facebook.png" id="facebook" name="facebook" onClick={this.handleClick} alt=""/>
        <img className="flex-icon" src="/img/twitter.png" id="twitter" name="twitter" onClick={this.handleClick} alt=""/>
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    socialMedia: state.socialMedia
  }
}

export default connect(mapStateToProps)(SocialMedia)
