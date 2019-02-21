import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import Header from './header';

storiesOf('header', module)
  .add('Basic', () => <Header />);