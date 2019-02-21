import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './socialMedia.css';
import { Button } from 'react-bootstrap'
import { changeSocialMedia } from '../../actions/user'

class SocialMedia extends Component {

  handleClick = (e) => {
    this.props.dispatch(changeSocialMedia(e.target.name))
  }

  render() {
    return (
      <div className="flex center">
        <img className="flex-icon" src="/img/facebook.png" name="facebook
        " onClick={this.handleClick} alt=""/>
        <img className="flex-icon" src="/img/twitter.png" name="twitter" onClick={this.handleClick} alt=""/>
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
