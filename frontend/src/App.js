import React from 'react';
import { Route, Routes } from "react-router-dom";

import Navbar from './components/navbar';
import NotFound from './components/notFound';
import Home from './components/home';
import Test from './components/test';
import Unauthorized from './components/unauthorized';
import Login from './components/auth/login';
import ProtectedRoutes from './components/auth/ProtectedRoutes';
import FabricationDashboard from './components/dashboards/fabrication/fabricationDashboard';
import SubAssemblyDashboard from './components/dashboards/subAssembly/subAssemblyDashboard';
import AssemblyDashboard from './components/dashboards/assembly/assemblyDashboard';

// MUI
import { blue } from '@mui/material/colors';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: {
            main: blue[900],
        },
    },
});


function App() {
    return (
        <ThemeProvider theme={theme}>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} exact />
                <Route path="/login" element={<Login />} exact />
                <Route path="/unauthorized" element={<Unauthorized />} exact />

                <Route element={<ProtectedRoutes allowedRoles='fabrication' />}>
                    <Route path="/fabrication-dashboard" element={<FabricationDashboard />} />
                </Route>

                <Route element={<ProtectedRoutes allowedRoles='sub-assembly' />}>
                    <Route path="/sub-assembly-dashboard" element={<SubAssemblyDashboard />} />
                </Route>

                <Route element={<ProtectedRoutes allowedRoles='assembly' />}>
                    <Route path="/assembly-dashboard" element={<AssemblyDashboard />} />
                </Route>

                <Route path="/test" element={<Test />} exact />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </ThemeProvider>
    );
}

export default App;