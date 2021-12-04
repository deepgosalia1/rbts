import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getAllData, getAllTransactions, getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import TradingPage from '../TradingPage';
import SearchPage from '../SearchPage';
import ApprovalList from '../ApprovalList';
import ListPage from '../ListPage';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

const TraderView = (props) => {
    const { traderData } = props
    const [btc, setBTC] = useState()
    const [transactions, setTransactions] = useState()
    const [clientData, setClientData] = useState()
    useEffect(() => {
        async function currPrice() {
            return await getBTCPrice().then(val => setBTC(val.bpi.USD.rate_float))
        }
        currPrice()
        getAllTransactions().then(setTransactions)
            getAllData('client').then((res) => {
                // console.log(clientData)
            setClientData(res)
        })
    }, [])
    return (
        <Grid container flex flexDirection={'column'}>
            <Grid container flex flexDirection={'row'}>
                {/* <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <TradingPage logout={props.logout} traderView = {true} />
                </Grid> */}
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    {clientData && <SearchPage clientSearch={true} transactions={clientData} />}
                </Grid>
            </Grid>
            <Grid container flex flexDirection={'row'}>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <ListPage Header={'Recent Transactions'} showHeader transactions={transactions} />
                </Grid>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    {btc && traderData && <ApprovalList traderData={traderData} currBTC={btc} />}
                </Grid>
            </Grid>
        </Grid>
    )
}

export default withStyles(styles)(TraderView)