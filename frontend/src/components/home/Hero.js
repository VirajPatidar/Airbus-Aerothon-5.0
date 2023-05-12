import { Box, styled, Typography } from "@mui/material";
import { Container } from "@mui/system";
import React from "react";
import heroImg from "../../images/supply.png";
import CustomButton from "./CustomButton";

const Hero = () => {
    const CustomBox = styled(Box)(({ theme }) => ({
        display: "flex",
        justifyContent: "center",
        gap: theme.spacing(10),
        paddingBottom: theme.spacing(10),
        [theme.breakpoints.down("md")]: {
            flexDirection: "column",
            alignItems: "center",
            textAlign: "center",
        },
    }));

    const Title = styled(Typography)(({ theme }) => ({
        fontSize: "48px",
        color: "#000336",
        fontWeight: "bold",
        margin: theme.spacing(4, 0, 4, 0),
        [theme.breakpoints.down("sm")]: {
            fontSize: "40px",
        },
    }));

    return (
        <Box sx={{ backgroundColor: "#E6F0FF", minHeight: "80vh" }}>
            <Container>
                <CustomBox>
                    <Box sx={{ flex: "1" }}>
                        <Typography
                            variant="body2"
                            sx={{
                                fontSize: "18px",
                                color: "#687690",
                                fontWeight: "500",
                                mt: 10,
                                mb: 4,
                            }}
                        >
                            Presenting Team A320's solution
                        </Typography>
                        <Title variant="h4">
                            Optimizing Washing Machine Manufacturing Supply Chain Using Data Lake
                        </Title>
                        <Typography
                            variant="body2"
                            sx={{ fontSize: "18px", color: "#5A6473", my: 4 }}
                            align="justify"
                        >
                            The main objective of this problem statement is to reduce
                            redundant intermediate data in the supply chain management process
                            of a washing machine manufacturing company by improving data
                            authenticity and efficiency across departments
                        </Typography>
                        <CustomButton
                            backgroundColor="#0F1B4C"
                            color="#fff"
                            buttonText="Get Started"
                            heroBtn={true}
                        />
                    </Box>

                    <Box sx={{ flex: "1.25" }}>
                        <img
                            src={heroImg}
                            alt="heroImg"
                            style={{ maxWidth: "100%", marginTop: "10rem", borderRadius: '8px' }}
                        />
                    </Box>
                </CustomBox>
            </Container>
        </Box>
    );
};

export default Hero;
