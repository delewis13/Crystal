import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './socialMedia.css';
import { Button } from 'react-bootstrap'
import { changeSocialMedia } from '../../actions/user'

class SocialMedia extends Component {

  componentDidMount() {
    this.props.dispatch(changeSocialMedia(""))
  }



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
        { (this.props.selected > 0) ? <div className="margin-bottom">Disclaimer: The information on this site is not intended or implied to be a substitute for professional medical advice, diagnosis or treatment. The depression indicator for the personality trait is to be taken only as a guide and professional medical advice should be sough where required.</div>
        :
        <div><img className="flex-icon" src={require("./../../img/facebook.png")} id="facebook" name="facebook" onClick={this.handleClick} alt=""/>
        <img className="flex-icon" src={require("./../../img/twitter.png")} id="twitter" name="twitter" onClick={this.handleClick} alt=""/></div>
      }
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    socialMedia: state.user.socialMedia,
    selected: state.user.selected
  }
}

export default connect(mapStateToProps)(SocialMedia)
