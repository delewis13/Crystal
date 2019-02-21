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
    return (
      <Button className="action-button" id="action-button" ref="actionButton" onClick={this.handleClick()}>Choose a platform</Button>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    socialMedia: state.socialMedia
  }
}

export default connect(mapStateToProps)(ActionButton)
