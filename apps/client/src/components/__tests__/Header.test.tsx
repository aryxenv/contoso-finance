import { render, screen } from '@testing-library/react';
import { FluentProvider, webDarkTheme } from '@fluentui/react-components';
import { Header } from '../Header';

function renderWithProviders(ui: React.ReactElement) {
  return render(<FluentProvider theme={webDarkTheme}>{ui}</FluentProvider>);
}

describe('Header', () => {
  it('renders the brand name', () => {
    renderWithProviders(<Header />);
    expect(screen.getByText('Contoso Finance')).toBeInTheDocument();
  });

  it('renders the GitHub repository link', () => {
    renderWithProviders(<Header />);
    const link = screen.getByLabelText('GitHub repository');
    expect(link).toBeInTheDocument();
    expect(link).toHaveAttribute('href', 'https://github.com/aryxenv/contoso-finance');
    expect(link).toHaveAttribute('target', '_blank');
    expect(link).toHaveAttribute('rel', 'noopener noreferrer');
  });

  it('renders inside a header element', () => {
    const { container } = renderWithProviders(<Header />);
    expect(container.querySelector('header')).toBeInTheDocument();
  });
});
