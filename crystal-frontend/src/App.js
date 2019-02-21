import React, { Component } from 'react';
import './App.css';
import Dashboard from './components/dashboard/dashboard'
import Header from './components/header/header'
import SocialMedia from './components/socialMedia/socialMedia'
import ActionButton from './components/actionButton/actionButton'
import { Container } from 'react-bootstrap'
import { connect } from 'react-redux'


class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Container>
          <Dashboard />
          <SocialMedia />
          <ActionButton />
        </Container>
      </div>    
    );
  }
}

export default connect()(App);
