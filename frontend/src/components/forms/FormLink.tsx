import React from 'react';
import { Link, LinkProps, Box } from '@mui/material';

interface FormLinkProps extends Omit<LinkProps, 'sx'> {
  children: React.ReactNode;
  center?: boolean;
  sx?: any;
}

const FormLink: React.FC<FormLinkProps> = ({
  children,
  center = true,
  sx,
  ...props
}) => {
  return (
    <Box
      sx={{
        textAlign: center ? 'center' : 'left',
        mt: 2,
        ...sx
      }}
    >
      <Link
        variant="body2"
        sx={{
          textDecoration: 'none',
          '&:hover': {
            textDecoration: 'underline'
          }
        }}
        {...props}
      >
        {children}
      </Link>
    </Box>
  );
};

export default FormLink;
