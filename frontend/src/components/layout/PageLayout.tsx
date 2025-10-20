import React from 'react';
import { Box, Container, Paper, SxProps, Theme } from '@mui/material';

interface PageLayoutProps {
  children: React.ReactNode;
  maxWidth?: 'xs' | 'sm' | 'md' | 'lg' | 'xl' | false;
  padding?: number | string;
  margin?: number | string;
  elevation?: number;
  sx?: SxProps<Theme>;
  background?: 'default' | 'paper' | 'transparent';
}

const PageLayout: React.FC<PageLayoutProps> = ({
  children,
  maxWidth = 'lg',
  padding = 3,
  margin = 'auto',
  elevation = 0,
  sx,
  background = 'default',
}) => {
  const getBackgroundColor = () => {
    switch (background) {
      case 'paper':
        return 'background.paper';
      case 'transparent':
        return 'transparent';
      default:
        return 'background.default';
    }
  };

  const content = (
    <Box
      sx={{
        minHeight: '100vh',
        backgroundColor: getBackgroundColor(),
        py: padding,
        ...sx,
      }}
    >
      {maxWidth ? (
        <Container maxWidth={maxWidth} sx={{ mx: margin }}>
          {elevation > 0 ? (
            <Paper elevation={elevation} sx={{ p: 3 }}>
              {children}
            </Paper>
          ) : (
            children
          )}
        </Container>
      ) : (
        children
      )}
    </Box>
  );

  return content;
};

export default PageLayout;
