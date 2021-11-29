import React, { useState } from "react";
import styled from 'styled-components';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { Box, Text } from 'grommet';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'


export default function Datepick(props) {
  const { setDates, startDate, endDate, searchData } = props


  return (
    <>
      <Grid container flex flexDirection={'row'} style={{ zIndex: 5 }}>
        <Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown', justifyContent: 'center' }}>
          <div style={{ display: 'flex', flex: 1, justifyContent: 'center', marginLeft: 350, flexDirection: 'row' }}>
            <BTCText>Search transactions for a particular date</BTCText>
            <div style={{ display: 'flex', flex: 1, justifyContent: 'center', marginRight: 10, flexDirection: 'row', marginTop: 10 }}>
              <DatePicker
                selectsRange={true}
                startDate={startDate}
                endDate={endDate}
                onChange={(update) => {
                  setDates(update)
                }}
                withPortal
              />
            </div>
          </div>
          <div style={{ justifyContent: 'center', marginRight: 500, marginTop: 10 }}>
            <ConfirmButton
              onClick={() => {
                searchData()
              }}>Search</ConfirmButton>
          </div>
        </Grid>
      </Grid>
    </>
  );
}


const ConfirmButton = styled.div`
cursor: pointer;
border: 1px solid grey;
border-radius: 5px;
backdrop-filter: blur(10px);
font-size: 18px;
padding: 5px;
display: flex;
max-height: 10px;
max-width: 50px;
align-items: center;
text-align: center;
justify-content: center;
background-color: #000000;
background-image: linear-gradient(147deg, #000000 0%, #2c3e50 74%);
color: white;
&:hover {
    opacity: 0.5;
    backdrop-filter: blur(35px);
};
`;

const HeaderText = styled(Text)`
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
font-weight: 200;
max-height: 10px;
font-size: 18px;
line-height: 10px;
color: rgba(255, 255, 255, 0.64);
display: flex;
width: 250px; height: 50px;
align-items: center;
`;

const BTCText = styled(Text)`
display: flex;
backdrop-filter: blur(70px);
padding: 10px 50px;
max-height: 10px;
border-radius: 10px;
color: whitesmoke;
font-family: sans-serif;
text-shadow:
-1px -1px 0 #000,  
1px -1px 0 #000,
-1px 1px 0 #000,
1px 1px 0 #000;
font-size: 18px;
width: 330px
`;

