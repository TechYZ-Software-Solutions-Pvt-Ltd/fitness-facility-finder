import React from 'react';
import { Box, CircularProgress, Typography, SxProps, Theme } from '@mui/material';

interface LoadingSpinnerProps {
  size?: number | string;
  message?: string;
  overlay?: boolean;
  sx?: SxProps<Theme>;
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({
  size = 40,
  message,
  overlay = false,
  sx,
}) => {
  const content = (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 2,
        ...sx,
      }}
    >
      <CircularProgress size={size} />
      {message && (
        <Typography variant="body2" color="text.secondary">
          {message}
        </Typography>
      )}
    </Box>
  );

  if (overlay) {
    return (
      <Box
        sx={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0, 0, 0, 0.5)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 9999,
        }}
      >
        {content}
      </Box>
    );
  }

  return content;
};

export default LoadingSpinner;
