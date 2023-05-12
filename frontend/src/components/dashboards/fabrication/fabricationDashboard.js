import React, { useState, useEffect } from 'react';
import axios from 'axios';

//MUI
import { Box, Card, CardContent, Grid, Typography } from '@mui/material';
import ForecastChart from '../global/forecastChart';
import InterData from './interData';

const FabricationDashboard = () => {

    const [interData, setInterData] = useState(null);
    const [globalData, setGlobalData] = useState(null);

    useEffect(() => {
        axios.defaults.headers["Authorization"] = "JWT " + localStorage.getItem("access_token");
        axios.get(`http://127.0.0.1:8000/api/manufactory/fabrication/`)
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setInterData(res.data);

            })
            .catch(err => {
                console.log(err)
            });

        axios.get(`http://127.0.0.1:8000/api/manufactory/approved`)
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setGlobalData(res.data);

            })
            .catch(err => {
                console.log(err)
            });
    }, [])

    return (
        <Box m={5}>
            <Box sx={{ my: 5, pb: 5, px: 10 }}>
                <Grid container spacing={6}>
                    <Grid item xs={12} sm={6} md={3}>
                        <Card raised sx={{ height: '100%', display: 'flex', flexDirection: 'column', backgroundColor: '#ffe082' }}>
                            <CardContent sx={{ flexGrow: 1, textAlign: "center", pb: 0, mb: 0 }}>
                                <Typography gutterBottom variant="h5" component="h2">
                                    Items Stamped and Published
                                </Typography>
                                <Typography variant="h2">
                                    {globalData && globalData.fabrications.quantity}
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                    <Grid item xs={12} sm={6} md={3}>
                        <Card raised sx={{ height: '100%', display: 'flex', flexDirection: 'column', backgroundColor: '#b9f6ca' }}>
                            <CardContent sx={{ flexGrow: 1, textAlign: "center", pb: 0, mb: 0 }}>
                                <Typography gutterBottom variant="h5" component="h2">
                                    Items Requiring Stamping
                                </Typography>
                                <Typography variant="h2">
                                    {interData && interData.quantity}
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                    <Grid item xs={12} sm={6} md={3}>
                        <Card raised sx={{ height: '100%', display: 'flex', flexDirection: 'column', backgroundColor: '#b2ebf2' }}>
                            <CardContent sx={{ flexGrow: 1, textAlign: "center", pb: 0, mb: 0 }}>
                                <Typography gutterBottom variant="h5" component="h2">
                                    Estimated Demand (Qty.) for next Week
                                </Typography>
                                <Typography variant="h2">
                                    972
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                    <Grid item xs={12} sm={6} md={3}>
                        <Card raised sx={{ height: '100%', display: 'flex', flexDirection: 'column', backgroundColor: '#e6ee9c' }}>
                            <CardContent sx={{ flexGrow: 1, textAlign: "center", pb: 0, mb: 0 }}>
                                <Typography gutterBottom variant="h5" component="h2">
                                    Estimated Demand (Qty.) for next Month
                                </Typography>
                                <Typography variant="h2">
                                    4708
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                </Grid>
            </Box>
            <Box sx={{ display: 'flex' }}>
                <Box>

                </Box>
                <Box sx={{ width: { xs: '100%', md: '55%' } }}>
                    <Typography variant='h5' gutterBottom>
                        Inventory Analysis
                    </Typography>
                    <ForecastChart />
                </Box>
                <Box ml={3} sx={{ width: { xs: '100%', md: '45%' } }}>
                    <Typography variant='h5' gutterBottom>
                        Unstamped Raw Data Generated Today
                    </Typography>
                    {interData && <InterData tableData={interData.data} />}
                </Box>
            </Box>
        </Box>
    );
}

export default FabricationDashboard;