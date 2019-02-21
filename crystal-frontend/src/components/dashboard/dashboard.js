import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './dashboard.css';
import 'bootstrap/dist/css/bootstrap.css'
import { Container } from 'react-bootstrap'
import getPersonalityDescriptors from './personalityDescriptors'
import Modal from 'react-modal';

Modal.setAppElement('#root')

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ModalOpen: false
    };
    this.openModal = this.openModal.bind(this)
    this.closeModal = this.closeModal.bind(this)
  }

  createGrid() {
    let images = []
    var i;
    for (i = 1; i < 17; i++) {
      images.push(i)
    }

    return images.map((imageName) => {return (
      <div className="flex-item" key={imageName} onClick={this.openModal.bind(this, imageName)}>
            <img className="flex-image" alt="" src={'/img/' + String(imageName) + '.png'} />
      </div>)
    })
  }

  openModal(imageName, e) {
    const personalityDescriptors = getPersonalityDescriptors()
    this.setState({modalOpen: true});
    setTimeout(() => {
      let title = document.getElementById('modal-title')
      let text = document.getElementById('modal-text')
      title.innerHTML = 'Your personality type:'
      text.innerHTML = personalityDescriptors[imageName - 1]
  }, 100)
  }

  closeModal() {

    this.setState({modalOpen: false})
  }

  render() {
    return (
      <Container>
        <div className="flex">
          {this.createGrid()}
        </div>
        <Modal
          isOpen={this.state.modalOpen}
          onRequestClose={this.closeModal}
          className="Modal"
          overlayClassName="Overlay"
          closeTimeoutMS={500}
        >
          <div className="Container flex">
            <h1 id="modal-title"></h1>
            <p id="modal-text"></p>
          </div>
        </Modal>
      </Container>
    )
  }
}

export default Dashboard;
