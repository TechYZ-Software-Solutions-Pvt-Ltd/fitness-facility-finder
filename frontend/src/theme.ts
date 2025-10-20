import { createTheme } from '@mui/material/styles';

// Approximate Material 3 look-and-feel using MUI v5 theming tokens
// Note: MUI's Joy UI has closer M3 tokens, but we keep @mui/material to minimize churn

export const theme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#6750A4' }, // M3 primary
    secondary: { main: '#7D5260' },
    background: { default: '#FFFBFE', paper: '#FFFFFF' },
    error: { main: '#B3261E' },
    success: { main: '#386A20' },
    warning: { main: '#7D5260' },
    info: { main: '#1D65C1' },
  },
  shape: { borderRadius: 12 },
  typography: {
    fontFamily: '"Roboto", "Inter", "Helvetica", "Arial", sans-serif',
    h1: { fontFamily: '"Shadows Into Light", cursive', fontWeight: 400 },
    h2: { fontWeight: 700 },
    h3: { fontWeight: 600 },
    button: { textTransform: 'none', fontWeight: 600 },
  },
  components: {
    MuiAppBar: {
      styleOverrides: { root: { boxShadow: 'none', borderBottom: '1px solid rgba(0,0,0,0.08)', borderRadius: 0 } },
    },
    MuiPaper: {
      defaultProps: { elevation: 0 },
      styleOverrides: {
        root: {
          borderRadius: 16,
          border: '1px solid rgba(0,0,0,0.06)',
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          paddingLeft: 16,
          paddingRight: 16,
        },
        contained: {
          boxShadow: 'none',
        },
      },
    },
    MuiTextField: {
      defaultProps: { variant: 'outlined' },
    },
    MuiCard: {
      styleOverrides: { root: { borderRadius: 16 } },
    },
    MuiChip: {
      styleOverrides: { root: { borderRadius: 10 } },
    },
  },
});


