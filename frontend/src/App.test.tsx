import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Basic test to prevent CI/CD failures
test('renders without crashing', () => {
  render(<App />);
  // This test ensures the app renders without throwing errors
  expect(document.body).toBeInTheDocument();
});
