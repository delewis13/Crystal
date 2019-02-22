import React, { Component } from 'react';
import './App.css';
import Dashboard from './components/dashboard/dashboard'
import Header from './components/header/header'
import SocialMedia from './components/socialMedia/socialMedia'
import ActionButton from './components/actionButton/actionButton'
import { Container } from 'react-bootstrap'
import { connect } from 'react-redux'
import LoadingOverlay from 'react-loading-overlay'

class App extends Component {
  componentDidMount() {
    console.log(this.props.loading)
  }
  render() {
    return (
      <div className="App">
        <LoadingOverlay 
          active={this.props.loading} 
          spinner
          text="Querying social media...">
          <Header />
          <Container>
            <Dashboard />
            <SocialMedia />
            <ActionButton />
          </Container>
        </LoadingOverlay>
      </div>    
    );
  }
}


const mapStateToProps = (state) => {
  return {
    loading: state.user.loading
  }
}

export default connect(mapStateToProps)(App);
