import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getAllData, getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import ManagerClientSearchPage from '../ManagerClientSearch';
import ManagerTraderSearchPage from '../ManagerTraderSearch';
import Datepick from '../Datepicker';
import TradingView from '../Histograms';
import Histograms from '../Histograms';
import SearchPage from '../SearchPage';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

const ManagerView = (props) => {
    const { managerData } = props
    const [traderData, setTraderData] = useState()
    const [clientData, setClientData] = useState()
    const getDefaultData = async () => {
        await getAllData('trader').then((res) => {
            console.log(`results are: `, res)
            setTraderData(res)
        })
        await getAllData('client').then((res) => {
            console.log(`results are: `, res)
            setClientData(res)
        })
    }
    useEffect(() => {
        getDefaultData()
    }, [])
    return (
        <>
            <Grid container flex flexDirection={'row'}>
                {/* <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}></Grid> */}
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    {clientData && <SearchPage transactions={clientData} clientSearch={true} />}
                </Grid>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    {traderData && <SearchPage transactions={traderData} />}
                </Grid>
            </Grid>
            <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                <Histograms />
            </Grid>
        </>
    )
}

export default withStyles(styles)(ManagerView)
