import React from 'react';
import { Route, Routes } from "react-router-dom";

// import Navbar from './components/navbar';
import NotFound from './components/notFound';
import Home from './components/home';
import Test from './components/test';

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
            {/* <Navbar /> */}
            <Routes>
                <Route path="/" element={<Home />} exact />
                <Route path="/test" element={<Test />} exact />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </ThemeProvider>
    );
}

export default App;