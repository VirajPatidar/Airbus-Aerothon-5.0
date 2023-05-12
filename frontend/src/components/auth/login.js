import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Copyright from "../copyright";
import { useSetRecoilState } from "recoil";
import { userData, isLoggedIn } from "../../atoms";

//IMAGE
import bg from "../../images/bg.svg";

//MUI
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Snackbar from "@mui/material/Snackbar";
import Slide from "@mui/material/Slide";
import { createTheme } from "@mui/material/styles";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";

const theme = createTheme();

const classes = {
    image: {
        marginTop: 0,
        backgroundImage: `url(${bg})`,
        backgroundRepeat: "repeat",
        backgroundSize: "cover",
        backgroundPosition: "center",
        height: "94vh",
    },
    paper: {
        marginTop: theme.spacing(8),
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: "100%", // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
    spacing: {
        margin: theme.spacing(3),
    },
    snackbar: {
        paddingBottom: theme.spacing(3),
    },
};

function TransitionLeft(props) {
    return <Slide {...props} direction="left" />;
}

export default function Login() {
    const setUser = useSetRecoilState(userData);
    const setLogin = useSetRecoilState(isLoggedIn);
    const navigate = useNavigate();

    const initialFormData = Object.freeze({
        email: "",
        password: "",
    });

    const [formData, updateFormData] = useState(initialFormData);
    const [emailerror, setEmailerror] = useState(false);
    const [passerror, setPasserror] = useState(false);
    const [open, setOpen] = useState(false);
    const [transition, setTransition] = useState(undefined);

    const [message, setMessage] = useState("");

    const handleChange = (e) => {
        setEmailerror(false);
        setPasserror(false);

        updateFormData({
            ...formData,
            [e.target.name]: e.target.value.trim(),
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        console.log(formData);

        // Validation
        const re =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        let submit = true;

        setEmailerror(false);
        setPasserror(false);

        if (formData.email === "" || !re.test(formData.email)) {
            setEmailerror(true);
            submit = false;
            console.log(submit);
            console.log(formData.email);
        }
        if (formData.password === "" || formData.password.length < 6) {
            setPasserror(true);
            submit = false;
            console.log(submit);
            console.log(formData.password);
        }

        if (submit) {
            axios.post(`http://localhost:8000/api/auth/jwt/create/`, {
                email: formData.email,
                password: formData.password,
            })
                .then((res) => {
                    console.log(res);
                    console.log(res.data);

                    localStorage.setItem(
                        "access_token",
                        res.data.access
                    );
                    localStorage.setItem(
                        "refresh_token",
                        res.data.refresh
                    );

                    axios.defaults.headers["Authorization"] = "JWT " + localStorage.getItem("access_token");

                    axios.get(`http://localhost:8000/api/auth/users/me/`)
                        .then((res) => {
                            console.log(res);
                            console.log(res.data);
                            let userType = res.data.user_type;
                            setUser({
                                user_id: res.data.id,
                                name: res.data.name,
                                email: res.data.email,
                                user_type: res.data.user_type,
                                is_officer: res.data.is_officer,
                            });
                            setLogin(true);
                            navigate(`/${userType}-dashboard`);
                        })
                        .catch((err) => {
                            console.log(err);
                            if (err.response.status === 401) {
                                setMessage("Invalid credentials, try again");
                                setTransition(() => TransitionLeft);
                                setOpen(true);
                            }
                            else if (err.response.status === 403) {
                                setMessage("You are not authorised to view this page");
                                setTransition(() => TransitionLeft);
                                setOpen(true);
                            }
                        });

                    setUser({
                        name: res.data.name,
                        email: res.data.email,
                        employment: res.data.employment,
                        id: res.data.teacher_id || res.data.other_id,
                        user_id: res.data.user_id,
                        user_type: res.data.user_type,
                    });
                    setLogin(true);
                    navigate("/dashboard/question");
                })
                .catch((err) => {
                    console.log(err);
                    if (err.response.status === 401) {
                        setMessage("Invalid credentials, try again");
                        setTransition(() => TransitionLeft);
                        setOpen(true);
                    }
                    else if (err.response.status === 403) {
                        setMessage("You are not authorised to view this page");
                        setTransition(() => TransitionLeft);
                        setOpen(true);
                    }
                });
        }
    };

    const handleClose = () => {
        setOpen(false);
    };

    return (
        <Container maxWidth="xl" disableGutters={true} sx={classes.image}>
            <CssBaseline />
            <Box
                sx={{
                    paddingTop: 9,
                    paddingLeft: 4,
                    paddingRight: 4,
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: "primary.main" }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Login
                </Typography>
                <form sx={classes.form}>
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email"
                        name="email"
                        autoComplete="email"
                        autoFocus
                        onChange={handleChange}
                        error={emailerror}
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        autoComplete="current-password"
                        onChange={handleChange}
                        error={passerror}
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        sx={classes.submit}
                        onClick={handleSubmit}
                    >
                        Login
                    </Button>
                    <Box mt={5}>
                        <Copyright />
                    </Box>
                </form>
            </Box>
            <Snackbar
                anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
                open={open}
                onClose={handleClose}
                TransitionComponent={transition}
                message={message}
                key={"bottom center"}
            />
        </Container>
    );
}
