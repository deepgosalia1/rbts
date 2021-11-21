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

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

const TraderView = (props) => {
    return (
        <>
            <Grid container flex flexDirection={'row'}>
                {/* <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}></Grid> */}
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <TradingPage logout={props.logout}/>
                </Grid>
                <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown' }}>
                    <SearchPage/>
                </Grid>
            </Grid>
        </>
    )
}

export default withStyles(styles)(TraderView)