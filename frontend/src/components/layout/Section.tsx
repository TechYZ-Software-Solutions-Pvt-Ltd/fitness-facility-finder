import React from 'react';
import { Box, Typography, SxProps, Theme } from '@mui/material';

interface SectionProps {
  children: React.ReactNode;
  title?: string;
  subtitle?: string;
  padding?: number | string;
  margin?: number | string;
  spacing?: number;
  divider?: boolean;
  sx?: SxProps<Theme>;
}

const Section: React.FC<SectionProps> = ({
  children,
  title,
  subtitle,
  padding = 2,
  margin = 0,
  spacing = 2,
  divider = false,
  sx,
}) => {
  return (
    <Box
      sx={{
        p: padding,
        m: margin,
        borderBottom: divider ? 1 : 0,
        borderColor: 'divider',
        ...sx,
      }}
    >
      {(title || subtitle) && (
        <Box sx={{ mb: spacing }}>
          {title && (
            <Typography variant="h5" component="h2" gutterBottom>
              {title}
            </Typography>
          )}
          {subtitle && (
            <Typography variant="body2" color="text.secondary">
              {subtitle}
            </Typography>
          )}
        </Box>
      )}
      {children}
    </Box>
  );
};

export default Section;
