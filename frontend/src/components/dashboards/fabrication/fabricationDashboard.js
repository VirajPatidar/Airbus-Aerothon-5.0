import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ForecastChart from '../global/forecastChart';
import InterData from './interData';
import { useRecoilValue } from 'recoil';
import { userData } from '../../../atoms';

//MUI
import { Box, Card, CardContent, Container, Grid, Typography } from '@mui/material';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';


const FabricationDashboard = () => {

    const user = useRecoilValue(userData);
    const [interData, setInterData] = useState(null);
    const [globalData, setGlobalData] = useState(null);

    const [stamps, setStamps] = useState('');

    const initialFormData = Object.freeze({
        item: "",
        raw_material: "",
        quantity: "",
    });

    const [open, setOpen] = React.useState(false);
    const [open2, setOpen2] = React.useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const handleClickOpen2 = () => {
        setOpen2(true);
    };

    const handleClose2 = () => {
        setOpen2(false);
    };

    const handleSubmit2 = () => {
        axios.patch(`http://127.0.0.1:8000/api/manufactory/fabrication/`, {
            id_list: stamps.split(',').map(Number),
        })
            .then((res) => {
                window.location.reload()
            })
            .catch(err => {
                console.log(err)
            });
    };

    const handleSubmit = () => {
        axios.post(`http://127.0.0.1:8000/api/manufactory/fabrication/`, {
            item: formData.item,
            raw_material: formData.raw_material,
            quantity: formData.quantity,
        })
            .then((res) => {
                window.location.reload()
            })
            .catch(err => {
                if (err.response.status === 400) {
                    alert("Duplicate Entry");
                }
                console.log(err)
            });
    };

    const [formData, updateFormData] = useState(initialFormData);
    const handleChange = (e) => {
        updateFormData({
            ...formData,
            [e.target.name]: e.target.value.trim(),
        });
    };


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
        <Container>
            <Box my={5}>
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
            <Box mt={10}>
                <Typography variant='h5' gutterBottom>
                    Inventory Analysis and Forecast
                </Typography>
                <ForecastChart />
            </Box>
            <Box mt={10}>
                <Typography variant='h5' gutterBottom>
                    Unstamped Raw Data Generated Today
                    <Button sx={{ marginLeft: '10px' }} variant="outlined" onClick={handleClickOpen}>
                        Create
                    </Button>
                    {user.is_officer &&
                        <Button sx={{ marginLeft: '10px' }} variant="outlined" onClick={handleClickOpen2}>
                            Stamp Data
                        </Button>
                    }
                </Typography>
                {interData && <InterData tableData={interData.data} />}
            </Box>
            <Box>
                <Dialog open={open} onClose={handleClose}>
                    <DialogTitle>Create Item</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            Create an Item for Stamping
                        </DialogContentText>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            name="item"
                            label="Item"
                            type="text"
                            fullWidth
                            variant="standard"
                            onChange={handleChange}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            name='raw_material'
                            label="Raw Material"
                            type="text"
                            fullWidth
                            variant="standard"
                            onChange={handleChange}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            name='quantity'
                            label="Quantity"
                            type="text"
                            fullWidth
                            variant="standard"
                            onChange={handleChange}
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button variant='outlined' onClick={handleClose}>Cancel</Button>
                        <Button variant='contained' onClick={handleSubmit}>Create</Button>
                    </DialogActions>
                </Dialog>
                <Dialog open={open2} onClose={handleClose2}>
                    <DialogTitle>Stamp Item</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            Enter the Item IDs separated by commas for the items you would like to stamp and approve. Example: '1,4,8'
                        </DialogContentText>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            name="item"
                            label="Item"
                            type="text"
                            fullWidth
                            variant="standard"
                            onChange={(e)=> setStamps(e.target.value.trim())}
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button variant='outlined' onClick={handleClose2}>Cancel</Button>
                        <Button variant='contained' onClick={handleSubmit2}>Stamp</Button>
                    </DialogActions>
                </Dialog>
            </Box>
        </Container >
    );
}

export default FabricationDashboard;