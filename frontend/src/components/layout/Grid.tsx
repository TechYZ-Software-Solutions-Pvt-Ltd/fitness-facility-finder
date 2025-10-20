import React from 'react';
import { Grid as MuiGrid, GridProps as MuiGridProps, SxProps, Theme } from '@mui/material';

interface GridProps extends Omit<MuiGridProps, 'sx'> {
  children: React.ReactNode;
  spacing?: number;
  sx?: SxProps<Theme>;
}

const Grid: React.FC<GridProps> = ({ children, spacing = 2, sx, ...props }) => {
  return (
    <MuiGrid container spacing={spacing} sx={sx} {...props}>
      {children}
    </MuiGrid>
  );
};

interface GridItemProps extends Omit<MuiGridProps, 'sx'> {
  children: React.ReactNode;
  xs?: number;
  sm?: number;
  md?: number;
  lg?: number;
  xl?: number;
  sx?: SxProps<Theme>;
}

const GridItem: React.FC<GridItemProps> = ({ 
  children, 
  xs = 12, 
  sm, 
  md, 
  lg, 
  xl, 
  sx, 
  ...props 
}) => {
  return (
    <MuiGrid 
      item 
      xs={xs} 
      sm={sm} 
      md={md} 
      lg={lg} 
      xl={xl} 
      sx={sx} 
      {...props}
    >
      {children}
    </MuiGrid>
  );
};

export { Grid, GridItem };
export default Grid;
