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

const clientTransactionRows = [
    { txid: 1, tid: 123, txtype: 'Buy', Date: Date.now(), status:'pending' },
    { txid: 2, tid: 123, txtype: 'Sell', Date: Date.now(), status:'approved' },
    { txid: 3, tid: 123, txtype: 'Wallet', Date: Date.now(), status:'reject' },
    { txid: 4, tid: 123, txtype: 'USD Wallet', Date: Date.now(), status:'pending' },
    { txid: 5, tid: 123, txtype: 'Sell', Date: Date.now(), status:'approved' },
    { txid: 6, tid: 123, txtype: 'Buy', Date: Date.now(), status:'approved' },
    { txid: 7, tid: 123, txtype: 'Buy', Date: Date.now(), status:'approved' },
];

const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    {
        field: 'firstName',
        headerName: 'First name',
        width: 150,
        editable: true,
    },
    {
        field: 'lastName',
        headerName: 'Last name',
        width: 150,
        editable: true,
    },
    {
        field: 'age',
        headerName: 'Age',
        type: 'number',
        width: 110,
        editable: true,
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


const SearchPage = (props) => {
    const { Header = '', showSearch = true, showHeader = false, clientMode = false } = props
    const [searchValue, setSearchvalue] = useState('')
    const [resultList, setResult] = useState(rows)

    const callSearchAPI = async () => {
        console.log('Search API is called here.')
    }

    
const clientTransactionCols = [
    { field: 'txid', headerName: 'Transact. ID', width: 200 },
    {
        field: 'tid',
        headerName: 'TID',
        width: 200,
        editable: false,
    },
    {
        field: 'txtype',
        headerName: 'Type',
        width: 200,
        editable: false,
    },
    {
        field: 'Date',
        headerName: 'time',
        // type: 'number',
        width: 250,
        editable: false,
    },
    {
        field: 'Status',
        headerName: 'txstatus',
        // description: 'This column has a value getter and is not sortable.',
        sortable: false,
        width: 200,
        renderCell: (params) => {
            let cellValue = params.row.status
            // console.log(cellValue, params)
            return (
                `${cellValue === 'approved' ? 'Approved' : cellValue === 'rejected' ? 'Rejected' : 'Pending'}`
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
                        rows={! clientMode ? rows: clientTransactionRows}
                        columns={clientMode ? clientTransactionCols : columns}
                        pageSize={5}
                        autoHeight
                        getRowId={(r) => r.txid || r.id}
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

export default withStyles(styles)(SearchPage)

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