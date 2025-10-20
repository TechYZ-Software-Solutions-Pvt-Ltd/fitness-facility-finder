import React from 'react';
import { Box, BoxProps } from '@mui/material';

interface FormActionsProps extends Omit<BoxProps, 'position'> {
  children: React.ReactNode;
  position?: 'left' | 'center' | 'right';
  spacing?: number;
}

const FormActions: React.FC<FormActionsProps> = ({
  children,
  position = 'right',
  spacing = 2,
  sx,
  ...props
}) => {
  const getPositionStyles = () => {
    switch (position) {
      case 'left':
        return { justifyContent: 'flex-start' };
      case 'center':
        return { justifyContent: 'center' };
      case 'right':
        return { justifyContent: 'flex-end' };
      default:
        return { justifyContent: 'flex-end' };
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        gap: spacing,
        mt: 3,
        ...getPositionStyles(),
        ...sx
      }}
      {...props}
    >
      {children}
    </Box>
  );
};

export default FormActions;
