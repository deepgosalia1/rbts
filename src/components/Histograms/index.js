import react, { useState } from 'react';
import Plot from 'react-plotly.js'
import { Box, Text } from 'grommet';
import styled from 'styled-components';
import Datepick from '../Datepicker';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { getDailyData, getMonthlyData, getWeeklyData } from '../ServerApi';
import formatDate from '../utils/getFormattedDate';


const Histograms = (props) => {
	const [dateRange, setDateRange] = useState([null], [null])
	const [daily, setDaily] = useState()
	const [weekly, setWeekly] = useState()
	const [monthly, setMonthly] = useState()
	const [startDate, endDate] = dateRange;
	const getHistogramData = async () => {
		try {
			await getDailyData(formatDate(String(startDate)), formatDate(String(endDate))).then((res) => {
				console.log('daily', res)
				setDaily(res)
			})
			await getWeeklyData(formatDate(String(startDate)), formatDate(String(endDate))).then((res) => {
				console.log('weekly', res)
				setWeekly(res)
			})
			await getMonthlyData(formatDate(String(startDate)), formatDate(String(endDate))).then((res) => {
				console.log('monthly', res)
				setMonthly(res)
			})
		} catch (error) {
			alert('Error occured while fetching data for histograms.')
		}
	}
	return (
		<div style={{}}>
			<Grid item flex style={{ display: 'flex', flex: 1, border: '1px solid brown', justifyContent: 'center' }}>
				<Datepick
					searchData={async () => {
						if (!startDate || !endDate) alert('please select BOTH start-date and end-date')
						else {
							await getHistogramData()
							return
						}
					}}
					startDate={startDate}
					endDate={endDate}
					setDates={(values) => {
						console.log(values)
						setDateRange(values)
					}} />
			</Grid>

			<Boxx style={{ display: 'flex', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

				<Plot
					data={[
						{
							type: 'bar',
							x: ['Yesterday', 'Today', 'three'],
							y: [100, 200, 50]
						}
					]}
					layout={{ width: 1000, height: 500, title: 'Daily Bar chart' }}
				/>
			</Boxx>
			<Boxx style={{ display: 'flex', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>
				<Plot
					data={[
						{
							type: 'bar',
							x: ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7'],
							y: [100, 200, 50, 100, 200, 50, 100]
						}
					]}
					layout={{ width: 1000, height: 500, title: 'Weekly Bar chart' }}
				/>
			</Boxx>
			<Boxx style={{ display: 'flex', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>
				<Plot
					data={[
						{
							type: 'bar',
							x: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
							y: [100, 200, 50, 100, 200, 50, 100, 200, 50, 100, 200, 50, 100, 200, 50]
						}
					]}
					layout={{ width: 1000, height: 500, title: 'Monthly Bar chart' }}
				/>
			</Boxx>

		</div>
	)
}

export default Histograms;

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
