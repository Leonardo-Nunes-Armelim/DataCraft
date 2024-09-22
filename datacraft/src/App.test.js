import { render, screen } from '@testing-library/react';
//import App from './App';
import TestComponent from './App';

test('renders learn react link', () => {
  //render(<App />);
  render(<TestComponent />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
