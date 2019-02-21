import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './dashboard.css';
import 'bootstrap/dist/css/bootstrap.css'
import { Container } from 'react-bootstrap'

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nextCron: "",
      emailValid: false,
      cronValid: false,
      easyCron: true,
      hasName: false
    };
  }

  createGrid() {
    let images = []
    var i;
    for (i = 1; i < 17; i++) {
      images.push(String(i) + '.png')
    }
    return images.map((imageName) => {return (<div className="flex-item" key={imageName}><img className="flex-image" alt="" src={'/img/' + imageName} /></div>)})
  }

  render() {
    return (
      <Container>
        <div className="flex">
          {this.createGrid()}
        </div>
      </Container>
    )
  }
}

export default Dashboard;
