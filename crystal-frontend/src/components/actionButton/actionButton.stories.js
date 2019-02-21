import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import ActionButton from './actionButton';

storiesOf('actionButton', module)
  .add('Basic', () => <ActionButton />);