import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './dashboard.css';
import 'bootstrap/dist/css/bootstrap.css'
import { Container } from 'react-bootstrap'
import { numberToDesc, personToNumber, numberToPerson, depressionIndicator } from './personalityDescriptors'
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
      <div className="flex-item" key={imageName} id={numberToPerson[imageName]} onClick={this.openModal.bind(this, imageName)}>
            <img className="flex-image" alt="" id={imageName} src={require('./../../img/' + String(imageName) + '.png')} />
      </div>)
    })
  }

  componentDidUpdate() {
    if (this.props.selected > 0 || this.props.selected === "reset") {
      console.log('hi')
      // this.props.selected should be a number
      var i;
      for (i=1; i < 17; i++) {
        let selectedImage = document.getElementById(String(i))
        let selectedDiv = document.getElementById(numberToPerson[i])
        if (i === this.props.selected) {
          selectedDiv.classList.add('highlight')
          console.log(numberToPerson[i])
          //selectedDiv = document.getElementById(numberToPerson[i])
          //selectedDiv.appendChild(<p>{depressionIndicator[numberToPerson[i]]}</p>)
        } else if (i > this.props.selected || i < this.props.selected) {
          selectedImage.classList.add('grayscale')
        } else {
          selectedImage.classList.remove('grayscale')
          selectedDiv.classList.remove('highlight')
        }
      }
    }
  }

  openModal(imageName, e) {
    this.setState({modalOpen: true});
    setTimeout(() => {
      let title = document.getElementById('modal-title')
      let text = document.getElementById('modal-text')
      title.innerHTML = numberToPerson[imageName]
      text.innerHTML = numberToDesc[imageName]
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
        <div className="depression margin-bottom">
          { (this.props.selected > 0) ? `Relative Predisposition to Depression: ${depressionIndicator[numberToPerson[this.props.selected]]}` : ''}
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

const mapStateToProps = (state) => {
  return {
    selected: state.user.selected
  }
}

export default connect(mapStateToProps)(Dashboard);
