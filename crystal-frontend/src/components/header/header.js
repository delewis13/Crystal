import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './header.css';
import 'bootstrap/dist/css/bootstrap.css'
import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap'

const Header = () => (
  <Navbar className="center" bg="light" variant="light">
    <Navbar.Brand className="col-md6 col-md-offset-3" href="#home">
      <img
        alt=""
        src="img/crystal3.svg"
        width="75"
        height="75"
        className="d-inline-block align-top"
      />
      <h1 className="small-margin">{'CRYSTAL'}</h1>
    </Navbar.Brand>
  </Navbar>
)

export default Header;
