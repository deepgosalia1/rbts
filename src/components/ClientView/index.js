import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text } from 'grommet';
import { getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import TradingPage from '../TradingPage';
import SearchPage from '../SearchPage';
import ApprovalList from '../ApprovalList';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

const ClientView = (props) => {
    return (
        <Grid container flex flexDirection={'column'}>
            <Grid container flex flexDirection={'row'}>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <TradingPage logout={props.logout} traderView = {false} />
                </Grid>
                {/* <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <SearchPage />
                </Grid> */}
            </Grid>
            <Grid container flex flexDirection={'row'}>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <SearchPage showSearch={false} Header={'Your Transactions'} showHeader clientMode/>
                </Grid>
            </Grid>
        </Grid>
    )
}

export default withStyles(styles)(ClientView)