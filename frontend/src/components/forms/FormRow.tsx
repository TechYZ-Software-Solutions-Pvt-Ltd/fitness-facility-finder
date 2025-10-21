import React from 'react';
import { Stack, StackProps } from '@mui/material';

interface FormRowProps extends Omit<StackProps, 'direction'> {
  children: React.ReactNode;
  spacing?: number;
  responsive?: boolean;
}

const FormRow: React.FC<FormRowProps> = ({
  children,
  spacing = 3,
  responsive = true,
  ...props
}) => {
  return (
    <Stack
      direction={responsive ? { xs: 'column', md: 'row' } : 'row'}
      spacing={spacing}
      sx={{ alignItems: 'center', ...props.sx }}
      {...props}
    >
      {children}
    </Stack>
  );
};

export default FormRow;
