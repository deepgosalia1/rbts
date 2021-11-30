import React, { useEffect, useState } from 'react';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Text, TextInput } from 'grommet';
import { getBTCPrice, getSearchData } from '../ServerApi';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import TradingPage from '../TradingPage';
import { SearchAdvanced } from 'grommet-icons';
import { DataGrid } from '@mui/x-data-grid';
import ObjectsToArray from '../utils/objToArray';
import { Button } from '@tsamantanis/react-glassmorphism';

const styles = {
    root: {
        background: "black"
    },
    input: {
        color: "white"
    }
};


const SearchPage = (props) => {
    let transacts = []
    const { Header = '', showSearch = true, showHeader = false, clientMode = false, transactions, clientSearch = false } = props
    // console.log(transactions)
    if (transactions) transacts = ObjectsToArray(transactions)
    const [searchValue, setSearchvalue] = useState('')
    const [resultList, setResult] = useState(transacts?.length > 0 && transacts || [])

    const callSearchAPI = async () => {
        if (searchValue !== '' || searchValue !== undefined || searchValue !== null) {
            if (clientSearch) {
                await getSearchData(searchValue, 'client').then((res) => {
                    console.log(`results for ${searchValue} are: `, res)
                    if (res) setResult(ObjectsToArray(res))
                })
            } else {
                await getSearchData(searchValue, 'trader').then((res) => {
                    console.log(`results for ${searchValue} are: `, res)
                    if (res) setResult(ObjectsToArray(res))
                })
            }
        }
    }

    const SearchClientCols = [
        {
            field: 'cid',
            headerName: 'Client ID',
            width: 80,
        },
        {
            field: 'fname',
            headerName: 'Name',
            width: 150,
            renderCell: (params) => {
                let cellValue = params.row.fname + ' ' + params.row.lname;
                // console.log(cellValue, params)
                return (
                    `${cellValue}`
                )
            }
            ,
        },
        { field: 'email', headerName: 'EMail', width: 200 },
        {
            field: 'btcwallet',
            headerName: 'BTC Wallet',
            width: 100,
        },
        {
            field: 'fiatwallet',
            headerName: 'USD Wallet',
            width: 100,
        },
        {
            field: 'phone',
            headerName: 'Phone',
            // type: 'number',
            width: 100,
        },
        {
            field: 'clientstatus',
            headerName: 'Status',
            width: 100,
            renderCell: (params) => {
                let cellValue = params.row.clientstatus
                // console.log(cellValue, params)
                return (
                    `${cellValue === 1 ? 'Silver' : 'Gold'}`
                )
            }
            ,
        },
        {
            field: 'clientstreet',
            headerName: 'Address 1',
            width: 100,
        },
        {
            field: 'clientzip',
            headerName: 'Zip',
            width: 100,
        },
        {
            field: 'clientstate',
            headerName: 'Location',
            width: 100,
            renderCell: (params) => {
                let cellValue = params.row.clientstate + ', ' + params.row.clientcountry
                return (
                    `${cellValue}`
                )
            }
            ,
        },
    ]

    const SearchTraderCols = [
        {
            field: 'tid',
            headerName: 'Trader ID',
            width: 80,
        },
        {
            field: 'fname',
            headerName: 'Name',
            width: 200,
            renderCell: (params) => {
                let cellValue = params.row.fname + ' ' + params.row.lname;
                return (
                    `${cellValue}`
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
                {showSearch &&
                    <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-around', alignItems: 'center' }}>
                        <Button text={`Search`} onClick={async () => {
                            await callSearchAPI()
                        }} />
                        <SearchInput
                            // placeholder={HeaderText || 'Search'}
                            value={searchValue}
                            onChange={event => setSearchvalue(event.target.value)}
                            onBlur={async () => {
                                // call the search api here once its ready from the backend
                                await callSearchAPI()
                            }}
                            onSubmitCapture={async () => {
                                // call the search api here once its ready from the backend
                                await callSearchAPI()
                            }}
                            color={'white'}
                            icon={<SearchAdvanced color={'grey'} style={{ zIndex: 5 }} onClick={() => { alert('aa') }} />}
                        />
                    </div>}
                <TableDiv>
                    <DataGrid
                        rows={resultList}
                        columns={clientSearch ? SearchClientCols : SearchTraderCols}
                        pageSize={5}
                        autoHeight
                        getRowId={(r) => r.txid || r.cid || r.tid || r.id}
                        disableSelectionOnClick
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