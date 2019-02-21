import React, { Component } from 'react';
import { connect } from 'react-redux';
import store from '../../store/configureStore';
import './header.css';

const Header = () => (
      <div className="flex">
        {this.createGrid()}
      </div>
)

export default Header;
