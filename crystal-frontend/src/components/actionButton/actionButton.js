import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './actionButton.css';
import { Button } from 'react-bootstrap'

class ActionButton extends Component {

  handleClick() {
    if (this.props.socialMedia === 'facebook') {
      console.log('Querying facebook...')
    } else if (this.props.socialMedia === 'twitter') {
      console.log('Querying twitter...')
    }
  }

  render() {
    return (
      <Button onClick={this.handleClick()}/>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    socialMedia: state.socialMedia
  }
}

export default connect(mapStateToProps)(ActionButton)
