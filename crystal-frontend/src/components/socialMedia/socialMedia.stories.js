import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import SocialMedia from './socialMedia';

storiesOf('socialMedia', module)
  .add('Basic', () => <SocialMedia />);