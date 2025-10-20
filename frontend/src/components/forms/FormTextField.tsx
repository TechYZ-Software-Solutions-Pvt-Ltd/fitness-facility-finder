import React from 'react';
import { TextField, TextFieldProps, SxProps, Theme } from '@mui/material';

interface FormTextFieldProps extends Omit<TextFieldProps, 'sx'> {
  variant?: 'outlined' | 'filled' | 'standard';
  sx?: SxProps<Theme>;
}

const FormTextField: React.FC<FormTextFieldProps> = ({ 
  variant = 'outlined', 
  sx,
  ...props 
}) => {
  return (
    <TextField
      variant={variant}
      sx={{
        '& .MuiInputLabel-root': {
          fontSize: '1rem',
          fontWeight: 500
        },
        '& .MuiInputBase-input': {
          fontSize: '1rem',
          py: 1.5
        },
        '& .MuiFormHelperText-root': {
          fontSize: '0.875rem',
          fontWeight: 400
        },
        '& .MuiOutlinedInput-root': {
          borderRadius: 1
        },
        ...sx
      }}
      {...props}
    />
  );
};

export default FormTextField;
