import * as React from 'react';
import { useRecoilState, } from 'recoil';
import { isLoggedIn, userData } from '../atoms';

// MUI
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import HubIcon from '@mui/icons-material/Hub';
import { AccountCircle, Dashboard, Logout } from '@mui/icons-material';
import { Divider, Link, ListItemIcon } from '@mui/material';
import axios from 'axios';


function Navbar() {
    const [anchorElUser, setAnchorElUser] = React.useState(null);

    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    const [user, setUser] = useRecoilState(userData);
    const [LoggedIn, setLogin] = useRecoilState(isLoggedIn);

    const handleLogout = () => {
        setUser({});
        setLogin(false);
        localStorage.clear();
        axios.defaults.headers["Authorization"] = null;
    }


    return (
        <AppBar position="static">
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                    <HubIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
                    <Typography
                        variant="h6"
                        noWrap
                        component="a"
                        href="/"
                        sx={{
                            mr: 2,
                            display: { xs: 'none', md: 'flex' },
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        Supply Chain Manager
                    </Typography>

                    <HubIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
                    <Typography
                        variant="h5"
                        noWrap
                        component="a"
                        href=""
                        sx={{
                            mr: 2,
                            display: { xs: 'flex', md: 'none' },
                            flexGrow: 1,
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        Supply Chain Manager
                    </Typography>

                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                    </Box>
                    {LoggedIn &&
                        <Box sx={{ flexGrow: 0 }}>
                            <Tooltip title="Open settings">
                                <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                                    <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
                                </IconButton>
                            </Tooltip>
                            <Menu
                                sx={{ mt: '45px' }}
                                id="menu-appbar"
                                anchorEl={anchorElUser}
                                anchorOrigin={{
                                    vertical: 'top',
                                    horizontal: 'right',
                                }}
                                keepMounted
                                transformOrigin={{
                                    vertical: 'top',
                                    horizontal: 'right',
                                }}
                                open={Boolean(anchorElUser)}
                                onClose={handleCloseUserMenu}
                            >
                                <MenuItem>
                                    <ListItemIcon>
                                        <AccountCircle />
                                    </ListItemIcon>
                                    <Typography textAlign="center">{user.name}</Typography>
                                </MenuItem>
                                <Divider />
                                <Link href={`${user.user_type}-dashboard`} underline="none">
                                    <MenuItem>
                                        <ListItemIcon>
                                            <Dashboard />
                                        </ListItemIcon>
                                        <Typography textAlign="center">Dashboard</Typography>
                                    </MenuItem>
                                </Link>
                                <MenuItem onClick={handleLogout}>
                                    <ListItemIcon>
                                        <Logout />
                                    </ListItemIcon>
                                    Logout
                                </MenuItem>
                            </Menu>
                        </Box>
                    }
                </Toolbar>
            </Container>
        </AppBar >
    );
}
export default Navbar;
