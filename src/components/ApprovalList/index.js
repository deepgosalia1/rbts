import React, { useEffect, useState } from 'react';
import { Grid, IconButton, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { withStyles } from '@mui/styles'
import { Box, Button, Text, TextInput } from 'grommet';
import { ApproveTopupRequet, getBTCPrice, getPendingTransactions, RejectTopup, ApproveTrade, RejectTrade } from '../ServerApi';
import styled from 'styled-components';
import { DataGrid } from '@mui/x-data-grid';
import CheckIcon from '@mui/icons-material/Check';
import ClearIcon from '@mui/icons-material/Clear';
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

const ApprovalList = (props) => {
    const { Header = 'Needs Approval', showSearch = false, showHeader = true, traderData, btc } = props
    const [resultList, setResultList] = useState([])

    const loadPendingTransactions = async () => {
        await getPendingTransactions().then((res) => {
            console.log(ObjectsToArray(res))
            if (res) setResultList(ObjectsToArray(res))
        })
    }

    const columns = [
        { field: 'txid', headerName: 'TX ID', width: 90 },
        {
            field: 'cid',
            headerName: 'CID',
            width: 90,
            editable: true,
        },
        {
            field: 'txtype',
            headerName: 'Type',
            width: 100,
            renderCell: (params) => {
                let cellValue = params.row.txtype === 0 ? 'Buy' : params.row.txtype === 1 ? 'Sell' : 'Recharge'
                return (
                    <div>
                        {cellValue}
                    </div>
                )
            },
        },
        {
            field: 'txamount',
            headerName: 'Amount',
            width: 110,
            renderCell: (params) => {
                let cellValue = params.row.txtype === 2 ? `${params.row.fiatamount || 0} USD` : `${params.row.txamount} BTC`
                return (
                    <div>
                        {cellValue}
                    </div>
                )
            },
        },
        {
            field: 'txdate',
            headerName: 'Order Date',
            width: 150,
            renderCell: (params) => {
                let cellValue = formatDate(params.row.txdate)
                return (
                    <div>
                        {cellValue}
                    </div>
                )
            },
        },
        {
            field: 'txstatus',
            headerName: 'Decision',
            sortable: false,
            width: 160,
            renderCell: (params) => {
                return (
                    <div style={{ display: 'flex', flexDirection: 'row' }}>
                        <IconButton aria-label="delete" onClick={async () => {
                            // state Update with filter to remove the clicked row
                            if (params.row.txtype === 2) {
                                await ApproveTopupRequet(params.row.txid, params.row.cid, params.row.fiatamount, formatDate(new Date(params.row.txdate)), traderData.userid).then(() => {
                                    setResultList(prev => prev.filter(p => p.id != params.row.id))

                                })
                            } else {
                                // place the approval Buy/Sell api here
                                await ApproveTrade(params.row.txid, btc, params.row.txtype, traderData.userid, params.row.commtype, params.row.cid).then(() => {
                                    setResultList(prev => prev.filter(p => p.id != params.row.id))
                                })
                            }
                        }}>
                            <CheckIcon />
                        </IconButton>
                        <IconButton aria-label="delete" onClick={async () => {
                            // state Update with filter to remove the clicked row
                            if (params.row.txtype === 2) {
                                RejectTopup(params.row.txid, params.row.cid, formatDate(new Date(params.row.txdate)), traderData.userid).then(() => {
                                    setResultList(prev => prev.filter(p => p.id != params.row.id))

                                })
                            } else {
                                // place the rejected Buy/Sell api here
                                await RejectTrade(params.row.txid, params.row.txtype, traderData.userid, params.row.cid).then(() => {
                                    setResultList(prev => prev.filter(p => p.id != params.row.id))
                                })
                            }
                        }}>
                            <ClearIcon />
                        </IconButton>
                    </div>
                )
            },
        },
    ];

    useEffect(() => {
        loadPendingTransactions()
    }, [])

    return (
        <>
            <DivHeader>
                {showHeader && <HeaderText>
                    {Header}
                </HeaderText>}
                <TableDiv>
                    <DataGrid
                        rows={resultList}
                        columns={columns}
                        pageSize={5}
                        autoHeight
                        disableSelectionOnClick
                        isCellEditable={false}
                        style={{ color: 'white' }}
                        rowsPerPageOptions={[5]}
                        getRowId={(params) => { return params.txid }}
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