import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import ManagerClientSearchPage from '../ManagerClientSearch';
import ManagerTraderSearchPage from '../ManagerTraderSearch';
import Datepick from '../Datepicker';
import TradingView from '../Histograms';
import Histograms from '../Histograms';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

const ManagerView = (props) => {
    const {managerData} = props 
    return (
        <>
            <Grid container flex flexDirection={'row'}>
                {/* <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}></Grid> */}
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <ManagerClientSearchPage />
                </Grid>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <ManagerTraderSearchPage />
                </Grid>
            </Grid>
            <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                <Histograms />
            </Grid>
        </>
    )
}

export default withStyles(styles)(ManagerView)
