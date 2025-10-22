import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

// Basic test to prevent CI/CD failures
test('renders without crashing', () => {
  // Simple test that just renders the app without throwing errors
  const { container } = render(<App />);
  expect(container).toBeInTheDocument();
});
