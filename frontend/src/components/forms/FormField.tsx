import React from 'react';
import { Box, BoxProps } from '@mui/material';

interface FormFieldProps extends BoxProps {
  children: React.ReactNode;
  fullWidth?: boolean;
  flex?: number | string;
  minWidth?: number | string;
}

const FormField: React.FC<FormFieldProps> = ({
  children,
  fullWidth = false,
  flex = 1,
  minWidth,
  sx,
  ...props
}) => {
  return (
    <Box
      sx={{
        flex: fullWidth ? '1 1 100%' : flex,
        minWidth: minWidth || (fullWidth ? '100%' : undefined),
        ...sx
      }}
      {...props}
    >
      {children}
    </Box>
  );
};

export default FormField;
