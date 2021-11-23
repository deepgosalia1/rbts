import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import { Button } from '@tsamantanis/react-glassmorphism'
import '@tsamantanis/react-glassmorphism/dist/index.css'

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};
const UserOptions = ['Trader', 'Client','Manager'];
//const commissionOptions = ['BTC', 'Fiat']

function TradingView(props) {
    //const [btc, setBTC] = useState(64646)
    //const [balance, setBalance] = useState(123)
    //const [amount, setAmount] = useState('')
    const [Firstname, setFirstname] = useState('');
    const [Lastname, setLastname] = useState('');
    const [userType, setuserType] = useState('');
    const [Email, setEmail] = useState('');
    const [Password, setPassword] = useState('');
    const [Phone, setPhone] = useState('');
    const [Age, setAge] = useState('');
    const [SSN, setSSN] = useState('');
    const [Add1, setAdd1] = useState('');
    const [Add2, setAdd2] = useState('');
    const [City, setCity] = useState('');
    const [Zip, setZip] = useState('');
    const [Login, setLogin] = useState('');
    const [incorrectInput, SetIncorrect] = useState(false)
    const [snackMessage, setSnackMessage] = useState('')
    const [open, setSnack] = useState(false)




    /*async function currPrice() {
        return await getBTCPrice().then(val => setBTC(val.bpi.USD.rate_float))
    }*/
    const [UserSelectedIndex, setUserSelectedIndex] = React.useState(1);
    //const [commSelectedIndex, setCommSelectedIndex] = React.useState(1);
    const executeTrade = async (Login) => {
        console.log('Logging in ...', Login)
        await setSnack(true)
        setSnackMessage('Logged in.')
    }
    const getUserType = (userType) => {
        console.log('...', userType)
    }
    const handleUserMenuItemClick = (event, index) => {
        setUserSelectedIndex(index);
    };
    /*const handleCommMenuItemClick = (event, index) => {
        setCommSelectedIndex(index);
    };*/
    function checkCorrectNumber(value) {
        var regexp = /^\d+(\.\d+)?$/;
        if (value && !regexp.test(value)) {
            SetIncorrect(true)
        } else {
            SetIncorrect(false)
        }
    }
    
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
                        <HeaderText style={{ display: 'flex', alignItems: 'center', flexDirection: 'row',marginTop: 10 }}>Sign Up</HeaderText>
                    </DivHeader>
                    <LoginBox>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>First Name</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Firstname}
                                    error={incorrectInput}
                                    placeholder={'First Name'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setFirstname(val.target.value.replace(/[^A-Za-z-$\.]/g, ""))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Last Name</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Lastname}
                                    error={incorrectInput}
                                    placeholder={'Last Name'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setLastname(val.target.value.replace(/[^A-Za-z-$\.]/g, ""))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Age</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Age}
                                    error={incorrectInput}
                                    placeholder={'0'}
                                    inputMode={'decimal'}
                                    onChange={(val) => {
                                        setAge(val.target.value.replace(/[^0-9\.]/g, ''))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>SSN</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={SSN}
                                    error={incorrectInput}
                                    placeholder={'0'}
                                    inputMode={'decimal'}
                                    onChange={(val) => {
                                        setSSN(val.target.value.replace(/[^0-9\.]/g, ''))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Email</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Email}
                                    error={incorrectInput}
                                    placeholder={'eg:abc@gmail.com'}
                                    inputMode={'decimal'}
                                    onChange={(val) => {
                                        setEmail()
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Password </HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer
                                    value={Password}
                                    error={incorrectInput}
                                    placeholder={''}
                                    inputMode={'decimal'}
                                    onChange={(val) => {
                                        setPassword()
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                            <HeaderText>Phone Number</HeaderText>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <InputContainer 
                                    value={Phone}
                                    error={incorrectInput}
                                    placeholder={''}
                                    inputMode={'decimal'}
                                    onChange={(val) => {
                                        setPhone(val.target.value.replace(/[^0-9\.]/g, ''))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                            </div>
                        </div>
                        <DivHeader>
                            <HeaderText style={{ display: 'flex', alignItems: 'center', flexDirection: 'row',marginTop: 10 }}>Address Details</HeaderText>
                            </DivHeader>
                        <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row',marginTop: 10 }}>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <Addtext>Line1:</Addtext>
                                <Address
                                    style={{
                                        marginInline: 20, display: 'flex',marginLeft: 10
                                    }}
                                    value={Add1}
                                    error={incorrectInput}
                                    placeholder={'Address'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setAdd1()
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                                <Addtext>Line2:</Addtext>
                                <Address
                                    style={{
                                        marginInline: 20, display: 'flex',marginLeft: 10,
                                    }}
                                    value={Add2}
                                    error={incorrectInput}
                                    placeholder={'Apt no:'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setAdd2()
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                                </div>
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row',marginTop: 10 }}>
                            <div
                                style={{
                                    marginInline: 30, display: 'flex',
                                }}
                            >
                                <Addtext>City:</Addtext>
                                <Address
                                    style={{
                                        marginInline: 20, display: 'flex',marginLeft: 20,
                                    }}
                                    value={City}
                                    error={incorrectInput}
                                    placeholder={'eg:Dallas'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setCity(val.target.value.replace(/[^A-Za-z-$\.]/g, ""))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                                <Addtext>Zip:</Addtext>
                                <Address
                                    style={{
                                        marginInline: 20, display: 'flex',marginLeft: 23
                                    }}
                                    value={Zip}
                                    error={incorrectInput}
                                    placeholder={'#####'}
                                    inputMode={'text'}
                                    onChange={(val) => {
                                        setZip(val.target.value.replace(/[^0-9\.]/g, ''))
                                    }}
                                    onBlur={(val => checkCorrectNumber(val.target.value))}
                                />
                                </div>
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row',marginTop: 10 }}>
                                <HeaderText>Type of User</HeaderText>

                                <Menu id="split-button-menu">
                                        {UserOptions.map((option, index) => (
                                            <MenuItem
                                                key={option}
                                                style={{
                                                    border: index === UserSelectedIndex ? '1px solid black' : 'none',
                                                    color: 'white',
                                                    backdropFilter: 'blur(10px)',
                                                }}
                                                selected={index === UserSelectedIndex}
                                                onClick={(event) => handleUserMenuItemClick(event, index)}
                                            >
                                                {option}
                                            </MenuItem>
                                        ))}
                                    </Menu>
                                
                        </div>
                        <ConfirmButton onClick={async () => {
                                await executeTrade(Login)
                            }}>Login</ConfirmButton>
                    </LoginBox>
                </LoginDiv></div>
            </Grid>
        </Grid >
    )
}

export default withStyles(styles)(TradingView);

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


const Menu = styled(Text)`
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
width: 150px; height: 50px
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
