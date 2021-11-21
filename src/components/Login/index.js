import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getBTCPrice, loginUserAPI } from '../ServerApi';
import styled from 'styled-components';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import bcrypt from 'bcryptjs';
const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

function Login(props) {
    const [Username, setUsername] = useState('')
    const [Password, setPassword] = useState('');
    // const [Login, setLogin] = useState('');
    const [incorrectInput, SetIncorrect] = useState(false)
    const [snackMessage, setSnackMessage] = useState('')
    const [open, setSnack] = useState(false)

    const executeLogin = async () => {
        console.log('Logging in ...')
        let pass_hash = await bcrypt.hash(Password, await bcrypt.genSalt(6));
        await loginUserAPI('1',Username, pass_hash)
        console.log('psh',pass_hash)
        await setSnack(true)
        setSnackMessage('Logged in.')
    }
    function checkCorrectNumber(value) {
        var regexp = /^\d+(\.\d+)?$/;
        if (value && !regexp.test(value)) {
            SetIncorrect(true)
        } else {
            SetIncorrect(false)
        }
    }
    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setSnack(false);
    };

    /*useEffect(() => {
        // currPrice() // fetching btc price
    }, [])*/
    return (
        <Grid
            container
            display={'flex'}
            flexDirection={'row'}
            justifyContent={'center'}
            style={{
                height: '100%',
                width: '100%',
                padding: 10,
            }}>
            <Grid item sm={12} md={12} lg={12}
                style={{
                    // backgroundColor:'green'
                }}
            >
                <Heading>
                    <Boxx style={{}}>
                        <HeadText>
                            Welcome to Bitcoin Trading System
                        </HeadText>
                    </Boxx>
                </Heading>
                <div style={{ height: 'fit-content', display:'flex', justifyContent:'center', marginTop: 100 }}>
                    <LoginDiv>
                    <DivHeader>
                        <HeaderText style={{ display: 'flex', alignItems: 'center', flexDirection: 'row',marginTop: 10 }}>Login</HeaderText>
                    </DivHeader>
                    <LoginBox>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Username</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Username}
                                    error={incorrectInput}
                                    placeholder={'Username'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setUsername(val.target.value)
                                    }}
                                    // onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Password</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Password}
                                    error={incorrectInput}
                                    placeholder={'Password'}
                                    type={'password'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setPassword(val.target.value)
                                        // console.log(val)
                                    }}
                                    // onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <ConfirmButton onClick={() => {
                            executeLogin(Login)
                        }}>Confirm</ConfirmButton>
                    </LoginBox>
                </LoginDiv></div>
            </Grid>
        </Grid >
    )
}

export default withStyles(styles)(Login);

const Boxx = styled(Box)`
display: inline-block;
background: radial-gradient(circle, rgba(0,212,255,1) 6%, rgba(2,0,36,1) 81%, rgba(9,31,121,1) 100%);
z-index: 1;
border-radius: 75px;
position: relative;
background-clip: border-box;
cursor: pointer;
`

const Heading = styled.div`
z-index:2;
display: flex;
justify-content: center;
`
const HeadText = styled(Text)`
display: flex;
backdrop-filter: blur(70px);
padding: 10px 50px;
border-radius: 10px;
color: whitesmoke;
font-family: sans-serif;
text-shadow:
-1px -1px 0 #000,  
1px -1px 0 #000,
-1px 1px 0 #000,
1px 1px 0 #000;`;


const Addtext = styled(Text)`
display: flex;
backdrop-filter: blur(70px);
padding: 10px 0px;
border-radius: 0px;
color: whitesmoke;
font-family: sans-serif;
text-shadow:
-1px -1px 0 #000,  
1px -1px 0 #000,
-1px 1px 0 #000,
1px 1px 0 #000;`;

const LoginDiv = styled.div`
background: linear-gradient(180deg,#48423e,#373030);
display: flex;
width: 40%;
padding: 5px;
flex-direction: column;
border-radius: 5px;
`;

const DivHeader = styled.div`
display: flex;
justify-content: space-between;
align-items: center;
max-height: 50px;
padding: 5px;
border-bottom: 0.2px solid white;
// width: 100%;
`;

const HeaderText = styled(Text)`
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 400;
font-size: 18px;
line-height: 20px;
color: rgba(255, 255, 255, 0.64);
margin: 5px 5px;
display: flex;
width: 150px; height: 50px;
align-items: center;
`;

const Radiobtn = styled(Text)`
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 300;
font-size: 18px;
line-height: 20px;
color: rgba(255, 255, 255, 0.64);
margin: 0px 0;
display: flex;
`;

const LoginBox = styled.div`
padding: 10px;
display: flex;
flex-direction: column;
`;

const InputContainer = styled(TextField)`
// color: rgba(0, 0, 0, 0.87);
cursor: text;
display: inline-flex;
position: relative;
font-size: 10rem;
box-sizing: border-box;
align-items: center;
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 400;
line-height: 1.1876em;
letter-spacing: 0.00938em;
background: grey;
width: 100%
`;

const Address = styled(TextField)`
// color: rgba(0, 0, 0, 0.87);
cursor: text;
display: inline-flex;
position: relative;
font-size: 10rem;
box-sizing: border-box;
align-items: center;
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 400;
line-height: 1.1876em;
letter-spacing: 0.00938em;
background: grey;
width: 100%;
`;

const ConfirmButton = styled.div`
cursor: pointer;
border: 1px solid grey;
border-radius: 5px;
backdrop-filter: blur(10px);
padding: 10px;
margin-top: 15px;
display: flex;
max-height: 300px;
align-items: center;
text-align: center;
justify-content: center;
background-color: #000000;
background-image: linear-gradient(147deg, #000000 0%, #2c3e50 74%);
color: white;
&:hover {
    opacity: 0.5;
    backdrop-filter: blur(35px);
};
`;
