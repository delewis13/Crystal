import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import 'bootstrap/dist/css/bootstrap.css'
import configureStore from './store/configureStore'
import { Provider } from 'react-redux'

const store = configureStore();
const state = store.getState();

store.dispatch({
  type: 'CHANGE_SOCIAL_MEDIA',
  socialMedia: 'twitter'
})

store.dispatch({
  type: 'CHANGE_SOCIAL_MEDIA',
  socialMedia: 'facebook'
})

console.log(store)
console.log(state)

const jsx = (
  <Provider store = {store}>
    <App />
  </Provider>
  )

ReactDOM.render(jsx, document.getElementById('root'))

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();


