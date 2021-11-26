import React, { useEffect, useState } from 'react';
import { Grid, IconButton, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Button, Text, TextInput } from 'grommet';
import { ApproveTopupRequet, getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import TradingPage from '../TradingPage';
import { SearchAdvanced } from 'grommet-icons';
import { DataGrid } from '@mui/x-data-grid';
import SearchPage from '../SearchPage';
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};

const rows = [
    { id: 1, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 2, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 3, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 4, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 5, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 6, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 7, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 8, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
    { id: 9, cid: 'Snow', CBalancebtc: 'Jon', CBalancewal: 35, timepass: '' },
];



const ApprovalList = (props) => {
    const { Header = 'Needs Approval', showSearch = false, showHeader = true, traderData } = props

    const [searchValue, setSearchvalue] = useState('')
    const [resultList, setResult] = useState(rows)
    const [pendingData, setData] = useState(rows);
    const callSearchAPI = async () => {
        console.log('Search API is called here.')
    }

    const columns = [
        { field: 'id', headerName: 'TxID', width: 90 },
        {
            field: 'cid',
            headerName: 'CID',
            width: 150,
            editable: true,
        },
        {
            field: 'CBalancebtc',
            headerName: 'BTC balance',
            width: 150,
            editable: true,
        },
        {
            field: 'CBalancewal',
            headerName: 'Wallet Bal',
            type: 'number',
            width: 110,
            editable: true,
        },
        {
            field: 'type',
            headerName: 'Type',
            width: 110,
            editable: true,
        },
        {
            field: 'timepass',
            headerName: 'Decision',
            description: 'This column has a value getter and is not sortable.',
            sortable: false,
            width: 160,
            renderCell: (params) => {
                return (
                    <div style={{ display: 'flex', flexDirection: 'row' }}>
                        <IconButton aria-label="delete" onClick={() => {
                            // state Update with filter to remove the clicked row
                            ApproveTopupRequet(params.txid, params.cid, params.fiatamount, params.txdate).then(() => {
                                setData(prev => prev.filter(p => p.id != params.id))

                            })
                            // add api to update too
                        }}>
                            <CheckIcon />
                        </IconButton>
                        <IconButton aria-label="delete" onClick={() => {
                            // state Update with filter to remove the clicked row
                            setData(prev => prev.filter(p => p.id != params.id))
                            // add api to update too
                        }}>
                            <ClearIcon />
                        </IconButton>
                    </div>
                )
            },
        },
    ];

    return (
        <>
            <DivHeader>
                {showHeader && <HeaderText>
                    {Header}
                </HeaderText>}
                {showSearch && <SearchInput
                    placeholder="Search Clients..."
                    value={searchValue}
                    onChange={event => setSearchvalue(event.target.value)}
                    onBlur={async () => {
                        // call the search api here once its ready from the backend
                        await callSearchAPI()
                    }}
                    // onSubmit={async ()=>{
                    //     // call the search api here once its ready from the backend
                    //      await callSearchAPI()
                    // }}
                    color={'white'}
                    icon={<SearchAdvanced color={'grey'} />}
                />}
                <TableDiv>
                    <DataGrid
                        rows={pendingData}
                        columns={columns}
                        pageSize={5}
                        autoHeight
                        disableSelectionOnClick
                        isCellEditable={false}
                        style={{ color: 'white' }}
                        rowsPerPageOptions={[5]}
                    />
                </TableDiv>

            </DivHeader>
        </>
    )
}
export default withStyles(styles)(ApprovalList)

const DivHeader = styled.div`
display: flex;
flex: 1;
flex-direction: column;
// justify-content: space-between;
align-items: center;
// max-height: 50px;
padding: 10px;
// border-bottom: 0.2px solid white;
// width: 100%;
`;

const SearchInput = styled(TextInput)`
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 400;
font-size: 18px;
line-height: 20px;
color: rgba(255, 255, 255, 0.64);
margin: 10px 0;
display: flex;
border: 2.5px solid linear-gradient(180deg,#48423e,#373030);
`;

const HeaderText = styled(Text)`
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 400;
font-size: 18px;
line-height: 20px;
color: rgba(255, 255, 255, 0.64);
margin: 10px 0;
display: flex;
`;

const TableDiv = styled.div`
display: flex;
flex: 1;
width: 100%;
background: linear-gradient(180deg,#48423e,#373030);
// background: red;
// height: 100px;
// width: 100px;
`;