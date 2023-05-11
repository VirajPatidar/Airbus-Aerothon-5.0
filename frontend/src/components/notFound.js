import React from 'react';
import { Link } from 'react-router-dom';
import Copyright from './copyright'

//MUI
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';


const NotFound = () => {

    return (
        <Box sx={{
            display: 'flex',
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            minHeight: '100vh'
        }}>
            <Typography variant="h1" sx={{fontSize: '12em'}}>
                404
            </Typography>
            <Typography variant="h4" gutterBottom>
                Page Not Found
            </Typography>
            <Link to="/" style={{ textDecoration: 'none', marginTop: '16px' }} color="inherit">
                <Button variant="contained"> Back to Home </Button>
            </Link>
            <Copyright />
        </Box>
    );
}

export default NotFound;