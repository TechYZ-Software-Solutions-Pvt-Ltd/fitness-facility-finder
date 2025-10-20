import React from 'react';
import { Button, ButtonProps, SxProps, Theme } from '@mui/material';

interface FormButtonProps extends Omit<ButtonProps, 'sx'> {
  variant?: 'contained' | 'outlined' | 'text';
  size?: 'small' | 'medium' | 'large';
  position?: 'left' | 'center' | 'right';
  sx?: SxProps<Theme>;
}

const FormButton: React.FC<FormButtonProps> = ({
  variant = 'contained',
  size = 'medium',
  position = 'right',
  children,
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
    <div style={{ display: 'flex', ...getPositionStyles(), marginTop: '24px' }}>
      <Button
        variant={variant}
        size={size}
        sx={{
          px: 4,
          py: 1,
          fontSize: '1rem',
          fontWeight: 600,
          borderRadius: 1,
          textTransform: 'none',
          boxShadow: variant === 'contained' ? '0 4px 12px rgba(103, 80, 164, 0.3)' : 'none',
          '&:hover': {
            boxShadow: variant === 'contained' ? '0 6px 16px rgba(103, 80, 164, 0.4)' : 'none',
            transform: variant === 'contained' ? 'translateY(-1px)' : 'none'
          },
          '&:disabled': {
            boxShadow: 'none',
            transform: 'none'
          },
          ...sx
        }}
        {...props}
      >
        {children}
      </Button>
    </div>
  );
};

export default FormButton;
