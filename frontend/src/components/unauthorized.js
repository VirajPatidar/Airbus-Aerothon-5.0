import React from 'react';
import { Link } from 'react-router-dom';
import Copyright from './copyright'

//MUI
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';


const Unauthorized = () => {

    return (
        <Box sx={{
            display: 'flex',
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            minHeight: '100vh'
        }}>
            <Typography variant="h1" sx={{ fontSize: '12em' }}>
                403
            </Typography>
            <Typography variant="h5" gutterBottom>
                You're unauthorized to view this page
            </Typography>
            <Link to="/" style={{ textDecoration: 'none', marginTop: '16px' }} color="inherit">
                <Button variant="contained"> Back to Home </Button>
            </Link>
            <Copyright />
        </Box>
    );
}

export default Unauthorized;