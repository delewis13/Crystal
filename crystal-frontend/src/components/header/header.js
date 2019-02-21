import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './header.css';
import 'bootstrap/dist/css/bootstrap.css'
import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap'

const Header = () => (
  <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
    <Container>
      <Navbar.Brand href="#home">Crystal</Navbar.Brand>
    </Container>
  </Navbar>
)

export default Header;
