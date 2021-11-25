import react, { Component } from 'react';
import Plot from 'react-plotly.js'
import { Box, Text } from 'grommet';
import styled from 'styled-components';
import Datepick from '../Datepicker';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'


class TradingView extends Component {
	render(){
		return(
			<div>
				<Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown',justifyContent:'center' }}>
                    <Datepick/>
                </Grid>
				
                <Boxx style={{ height: 'fit-content', justifyContent:'center', marginTop: 100,marginLeft: 200}}> 
				 
				<Plot
					data={[
						{
							type:'bar',
							x:['Yesterday','Today','three'],
							y:[100,200,50]}
						]}
					layout={ { width:1000,height: 500,title: 'Daily Bar chart' } }
					
				/>
				</Boxx> 
				<Boxx style={{ height: 'fit-content', justifyContent:'center', marginTop: 100,marginLeft: 200}}>
				<Plot
					data={[
						{
							type:'bar',
							x:['Day1','Day2','Day3','Day4','Day5','Day6','Day7'],
							y:[100,200,50,100,200,50,100]}
						]}
					layout={ { width:1000,height: 500,title: 'Weekly Bar chart' } }
				/>
				</Boxx> 
				<Boxx style={{ height: 'fit-content', justifyContent:'center', marginTop: 100,marginLeft: 200}}>
				<Plot
					data={[
						{
							type:'bar',
							x:['January','February','March','April','May','June','July','August','September','October','November','December'],
							y:[100,200,50,100,200,50,100,200,50,100,200,50,100,200,50]}
						]}
					layout={ { width:1000,height: 500,title: 'Monthly Bar chart' } }
				/>
				</Boxx>
				
			</div>
		)
	}
}

export default TradingView;

const Boxx = styled(Box)`
display: inline-block;
background: radial-gradient(circle, rgba(0,212,255,1) 6%, rgba(2,0,36,1) 81%, rgba(9,31,121,1) 100%);
z-index: 1;
border-radius: 75px;
position: relative;
background-clip: border-box;
cursor: pointer;
`

const HeadText = styled(Text)`
display: flex;
backdrop-filter: blur(70px);
padding: 10px 50px;
border-radius: 10px;
color: whitesmoke;
font-family: sans-serif;
text-shadow:
-1px -1px 0 #000,  
1px -1px 0 #000,
-1px 1px 0 #000,
1px 1px 0 #000;`;