import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text, TextInput } from 'grommet';
import { getBTCPrice } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import TradingPage from '../TradingPage';
import { SearchAdvanced } from 'grommet-icons';
import { DataGrid } from '@mui/x-data-grid';
import ObjectsToArray from '../utils/objToArray';
import formatDate from '../utils/getFormattedDate';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};
const rows = [
    { id: 1, lastName: 'Snow', firstName: 'Jon', age: 35 },
    { id: 2, lastName: 'Lannister', firstName: 'Cersei', age: 42 },
    { id: 3, lastName: 'Lannister', firstName: 'Jaime', age: 45 },
    { id: 4, lastName: 'Stark', firstName: 'Arya', age: 16 },
    { id: 5, lastName: 'Targaryen', firstName: 'Daenerys', age: null },
    { id: 6, lastName: 'Melisandre', firstName: null, age: 150 },
    { id: 7, lastName: 'Clifford', firstName: 'Ferrara', age: 44 },
    { id: 8, lastName: 'Frances', firstName: 'Rossini', age: 36 },
    { id: 9, lastName: 'Roxie', firstName: 'Harvey', age: 65 },
];


const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    {
        field: 'firstName',
        headerName: 'First name',
        width: 150,
    },
    {
        field: 'lastName',
        headerName: 'Last name',
        width: 150,
    },
    {
        field: 'age',
        headerName: 'Age',
        type: 'number',
        width: 110,
    },
    {
        field: 'fullName',
        headerName: 'Full name',
        description: 'This column has a value getter and is not sortable.',
        sortable: false,
        width: 160,
        valueGetter: (params) =>
            `${params.getValue(params.id, 'firstName') || ''} ${params.getValue(params.id, 'lastName') || ''
            }`,
    },
];


const ListPage = (props) => {
    let transacts = []
    const { Header = '', showSearch = true, showHeader = false, clientMode = false, transactions } = props
    if (transactions) transacts = ObjectsToArray(transactions)
    const [resultList, setResult] = useState(transacts.length > 0 && transacts || rows)

    const clientTransactionCols = [
        { field: 'txid', headerName: 'Transact. ID', width: clientMode ? 200: 150 },
        {
            field: clientMode ? 'tid' : 'cid',
            headerName: clientMode ? 'Trader ID' : 'Client ID',
            width: clientMode ? 200: 100,
            renderCell: (params) => {
                let cellValue = clientMode ? params.row.tid : params.row.cid
                return (
                    `${cellValue === null ? '-' : cellValue}`
                )
            }
            ,
        },
        {
            field: 'txtype',
            headerName: 'Type',
            width: clientMode ? 200: 100,
            renderCell: (params) => {
                let cellValue = params.row.txtype
                return (
                    `${cellValue === 0 ? 'Buy' : cellValue === 1 ? 'Sell' : 'Wallet'}`
                )
            }
            ,
        },
        {
            field: 'txamount',
            headerName: 'Amount',
            width: clientMode ? 200: 100,
            renderCell: (params) => {
                let cellValue = params.row.txtype === 2 ? `${params.row.fiatamount} USD` : `${params.row.txamount} BTC`
                return (
                    `${cellValue}`
                )
            }
            ,
        },
        {
            field: 'txdate',
            headerName: 'Date',
            // type: 'number',
            width: clientMode ? 200: 150,
            renderCell: (params) => {
                let cellValue = params.row.txdate
                return (
                    `${formatDate(cellValue)}`
                )
            }
            ,
        },
        {
            field: 'Status',
            headerName: 'Status',
            width: clientMode ? 200: 100,
            renderCell: (params) => {
                let cellValue = params.row.txstatus
                // console.log(cellValue, params)
                return (
                    `${cellValue === 1 ? 'Approved' : cellValue !== 0 ? 'Rejected' : 'Pending'}`
                )
            }
            ,
        },
    ]
    return (
        <>
            <DivHeader>
                {showHeader && <HeaderText>
                    {Header}
                </HeaderText>}

                <TableDiv>
                    <DataGrid
                        rows={transacts.reverse()}
                        columns={clientTransactionCols}
                        pageSize={5}
                        autoHeight
                        getRowId={(r) => r.txid || r.cid || r.id}
                        disableSelectionOnClick
                        style={{ color: 'white' }}
                        rowsPerPageOptions={[5]}
                    />
                </TableDiv>

            </DivHeader>
        </>
    )
}

export default withStyles(styles)(ListPage)

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