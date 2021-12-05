import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getBTCPrice, placeTrade, placeTopUpRequest, placeIndependentTrade, placeTraderDependentTrade } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import { Button } from '@tsamantanis/react-glassmorphism'
import '@tsamantanis/react-glassmorphism/dist/index.css'
import { Modal } from 'react-bootstrap';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import formatDate from '../utils/getFormattedDate';

const Alert = React.forwardRef(function Alert(props, ref) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});
const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};
const TradeOptions = ['Buy', 'Sell'];
const traderOptions = ['Independent', 'Trader'];
const commissionOptions = ['BTC', 'USD']

function TradingView(props) {
    const { traderView = false, userData, updateTxn = undefined } = props
    const [btc, setBTC] = useState(64646)
    const [amount, setAmount] = useState(0)
    const [snackMessage, setSnackMessage] = useState('')
    const [incorrectInput, SetIncorrect] = useState(false)
    async function currPrice() {
        return await getBTCPrice().then(val => setBTC(val.bpi.USD.rate_float))
    }
    const [tradeSelectedIndex, setTradeSelectedIndex] = React.useState(1);
    const [commSelectedIndex, setCommSelectedIndex] = React.useState(1);
    const [open, setSnack] = useState(false)
    const [show, setShow] = useState(false);
    const [type, setType] = useState('B')
    const [topUpValue, setTopUpValue] = useState(0)
    const [viaTrader, setViaTrader] = useState(0);

    const handleModalClose = () => {
        setShow(false);
    }
    const handleShow = () => setShow(true);

    const executeTrade = async (amount) => {
        // comment this if-loop for testing purposes
        if (userData.fiatwallet < amount) {
            alert('Insufficient Funds in wallet!')
            return
        }
        if (!amount || amount <= 0) {
            alert('Invalid Input')
            return
        }
        console.log('clientdata', userData)
        if (!viaTrader) {
            await placeIndependentTrade(
                userData.userid,
                Number(amount),
                tradeSelectedIndex,
                formatDate(new Date()),
                btc
            ).then(() => {
                setSnack(true)
                setSnackMessage('Transaction Confirmed.')
                if (updateTxn) updateTxn()
            }).catch((e) => {
                setSnack(true)
                setSnackMessage('Transaction couldnt be placed.')
            })
        }
        else {
            await placeTraderDependentTrade(
                userData.userid,
                Number(amount),
                tradeSelectedIndex,
                commSelectedIndex,
                formatDate(new Date()),
                btc,
                commissionOptions[commSelectedIndex]
            ).then(() => {
                setSnack(true)
                setSnackMessage('Transaction Placed.')
                if (updateTxn) updateTxn()
            }).catch((e) => {
                setSnack(true)
                setSnackMessage('Transaction couldnt be placed.')
            })
        }

    }
    const handleTradeMenuItemClick = (event, index) => {
        setTradeSelectedIndex(index);
    };
    const handleCommMenuItemClick = (event, index) => {
        setCommSelectedIndex(index);
    };
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

    useEffect(() => {
        currPrice() // fetching btc price

    }, [])

    return (
        <>
            <Dialog open={show} onClose={handleModalClose} fullWidth color={'black'}>
                <DialogTitle>Top up Wallet</DialogTitle>
                <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="name"
                        label={type === 'B' ? "BTC Amount" : "USD Amount"}
                        type="decimal"
                        fullWidth
                        variant="filled"
                        value={topUpValue}
                        onChange={(val) => {
                            setTopUpValue(val.target.value)
                        }}
                        placeholder={`Enter the amount of ${type == 'B' ? 'BTC' : 'USD'} you want to ${type == 'B' ? 'purchase' : 'deposit'} at current price`}
                    />
                </DialogContent>
                <DialogActions style={{ backgroundColor: 'lightGrey', display: 'flex', justifyContent: 'space-between' }}>
                    <Text onClick={handleModalClose} color={'black'} style={{ cursor: 'pointer', padding: 10, display: 'flex', color: 'black', zIndex: 5 }}>Cancel</Text>
                    <Text onClick={() => {
                        handleModalClose()
                        placeTopUpRequest(userData.userid, topUpValue, formatDate(new Date())).then(() => {
                            setSnack(true)
                            setSnackMessage('Placed Topup request.')
                        })
                    }} color={'black'} style={{ cursor: 'pointer', padding: 10, display: 'flex', color: 'black', zIndex: 5 }}>Confirm</Text>
                </DialogActions>
            </Dialog>
            <Grid
                container
                display={'flex'}
                flexDirection={'column'}
                justifyContent={'center'}
                style={{
                    // flex:1,
                    height: '100%',
                    width: '100%',
                    padding: 10,
                }}>
                <Grid item sm={12} md={12} lg={12}>
                    {/* <LogoutButton text="Logout" onClick={() => {
                        props?.logout()
                    }} /> */}

                    <BTCPriceDiv>
                        <Boxx style={{}}>
                            <BTCText>
                                Current BTC price: ${btc}
                            </BTCText>
                        </Boxx>
                    </BTCPriceDiv>
                    <div style={{ height: 'fit-content', display: 'flex', justifyContent: 'center', marginTop: 50 }}>
                        <TradeDiv>
                            {!traderView && <DivHeader>
                                <HeaderText
                                >BTC Balance : {userData.btcwallet}
                                </HeaderText>
                                {!traderView ? <HeaderText>Welcome : {userData.fname}</HeaderText> : <></>}
                                <HeaderText
                                    style={{
                                        textDecorationLine: !traderView ? 'underline' : 'none'
                                    }}
                                    onClick={() => {
                                        if (traderView) return
                                        setType('W')
                                        handleShow()
                                    }}
                                >Wallet Balance : {userData.fiatwallet}
                                </HeaderText>
                            </DivHeader>}
                            <TradeBox>
                                <div style={{ display: 'flex', alignItems: 'center', flexDirection: 'row' }}>
                                    <HeaderText>Enter Amount</HeaderText>
                                    <div
                                        style={{
                                            marginInline: 30, display: 'flex',
                                        }}
                                    >
                                        <InputContainer
                                            value={amount}
                                            error={incorrectInput}
                                            placeholder={'0'}
                                            inputMode={'decimal'}
                                            onChange={(val) => {
                                                setAmount(val.target.value.replace(/[^0-9\.]/g, ''))
                                            }}
                                            onBlur={(val => checkCorrectNumber(val.target.value))}
                                        />
                                    </div>
                                    <div style={{ display: 'flex', justifyContent: 'center', }}>
                                        <MenuList id="split-button-menu">
                                            {TradeOptions.map((option, index) => (
                                                <MenuItem
                                                    key={option}
                                                    style={{
                                                        border: index === tradeSelectedIndex ? '1px solid black' : 'none',
                                                        color: 'white',
                                                        backdropFilter: 'blur(10px)',
                                                    }}
                                                    selected={index === tradeSelectedIndex}
                                                    onClick={(event) => handleTradeMenuItemClick(event, index)}
                                                >
                                                    {option}
                                                </MenuItem>
                                            ))}
                                        </MenuList>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', justifyContent: 'space-between', }}>
                                    <HeaderText>Place Trade via:</HeaderText>
                                    <MenuList style={{ display: 'flex', flexDirection: 'row', }}>
                                        {traderOptions.map((option, index) => (
                                            <MenuItem
                                                key={option}
                                                style={{
                                                    border: index === viaTrader ? '1px solid blue' : 'none',
                                                    color: 'white',
                                                    backdropFilter: 'blur(10px)',
                                                }}
                                                selected={index === viaTrader}
                                                onClick={(event) => setViaTrader(index)}
                                            >
                                                {option}
                                            </MenuItem>
                                        ))}
                                    </MenuList>
                                </div>
                                {viaTrader ? <div style={{ display: 'flex', justifyContent: 'space-between', }}>
                                    <HeaderText>Commision Method</HeaderText>
                                    <MenuList style={{ display: 'flex', flexDirection: 'row', }}>
                                        {commissionOptions.map((option, index) => (
                                            <MenuItem
                                                key={option}
                                                style={{
                                                    border: index === commSelectedIndex ? '1px solid red' : 'none',
                                                    color: 'white',
                                                    backdropFilter: 'blur(10px)',
                                                }}
                                                selected={index === commSelectedIndex}
                                                onClick={(event) => handleCommMenuItemClick(event, index)}
                                            >
                                                {option}
                                            </MenuItem>
                                        ))}
                                    </MenuList>
                                </div> : <></>}
                                <ConfirmButton onClick={async () => {
                                    await executeTrade(amount)
                                }}>{traderView ? 'Confirm' : 'Place Order'}</ConfirmButton>
                            </TradeBox>
                        </TradeDiv></div>
                </Grid>
                <Snackbar open={open} autoHideDuration={2000} onClose={handleClose}>
                    <Alert onClose={handleClose} severity={"info"} sx={{ width: '100%' }}>
                        Transaction order placed, pending approval
                    </Alert>
                </Snackbar>
            </Grid >
        </>
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

const BTCPriceDiv = styled.div`
z-index:2;
display: flex;
justify-content: center;
`
const BTCText = styled(Text)`
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
1px 1px 0 #000;
`;

const TradeDiv = styled.div`
background: linear-gradient(180deg,#48423e,#373030);
display: flex;
// width: 40%;
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
margin: 10px 0;
display: flex;
cursor: pointer;
`;

const TradeBox = styled.div`
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

const LogoutButton = styled(Button)`

`;