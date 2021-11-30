import react, { useState } from 'react';
import Plot from 'react-plotly.js'
import { Box, Text } from 'grommet';
import styled from 'styled-components';
import Datepick from '../Datepicker';
import { Grid, Input, MenuItem, MenuList, TextField } from '@mui/material'
import { getDailyData, getMonthlyData, getWeeklyData } from '../ServerApi';
import formatDate from '../utils/getFormattedDate';
import ObjectsToArray from '../utils/objToArray';


const Histograms = (props) => {
	const [dateRange, setDateRange] = useState([null], [null])
	const [[xDaily, yDaily, yDailySum], setDaily] = useState([null], [null], [null])
	const [[xWeekly, yWeekly, yWeeklySum], setWeekly] = useState([null], [null], [null])
	const [[xMonthly, yMonthly, yMonthlySum], setMonthly] = useState([null], [null], [null])
	const [startDate, endDate] = dateRange;
	const [showHisto, setHisto] = useState(false);
	const getHistogramData = async () => {
		try {
			await getDailyData(formatDate(String(startDate)), formatDate(String(endDate))).then((res) => {
				// console.log('daily', res)
				if (res) {
					// ObjectsToArray(res)
					let x = [], y = [], ySum = [], data = ObjectsToArray(res)
					data.forEach(element => {
						x.push(element.txdate)
					});

					data.forEach(element => {
						y.push(element.count)
						ySum.push(element.sum)
					});
					setDaily([x, y, ySum])
					console.log(xDaily, yDaily, [x, y, ySum])
				}
			})
			await getWeeklyData(formatDate(String(startDate)), formatDate(String(endDate))).then((res) => {
				// console.log('weekly', ObjectsToArray(res))
				if (res) {
					// ObjectsToArray(res)
					let x = [], y = [], ySum = [], data = ObjectsToArray(res)
					data.forEach(element => {
						x.push(element.txdate)
					});

					data.forEach(element => {
						y.push(element.count)
						ySum.push(element.sum)
					});
					setWeekly([x, y, ySum])
				}
			})
			await getMonthlyData(formatDate(String(startDate)), formatDate(String(endDate))).then((res) => {
				// console.log('monthly', res)
				if (res) {
					// ObjectsToArray(res)
					let x = [], y = [], ySum = [], data = ObjectsToArray(res)
					data.forEach(element => {
						x.push(element.txdate)
					});

					data.forEach(element => {
						y.push(element.count)
						ySum.push(element.sum)
					});
					setMonthly([x, y, ySum])
				}
			})
		} catch (error) {
			alert('Error occured while fetching data for histograms.')
		}
	}
	return (
		<div style={{}}>
			<Grid item flex style={{ width: 'fit-content', flex: 1, border: '1px solid brown', justifyContent: 'center' }}>
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
						setHisto(true)
					}} />
			</Grid>
			{showHisto && <Grid container flex flexDirection={'column'}>

				<Grid item style={{ display: 'flex', flexDirection: 'row', justifyContent:'center' }} flexDirection={'row'}>
					<Boxx style={{ width: 'fit-content', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

						<Plot
							data={[
								{
									type: 'bar',
									x: xDaily,
									y: yDaily
								}
							]}
							layout={{ title: 'Daily TXN Count' }}
						/>
					</Boxx>
					<Boxx style={{ width: 'fit-content', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

						<Plot
							data={[
								{
									type: 'bar',
									x: xDaily,
									y: yDailySum
								}
							]}
							layout={{ title: 'Daily TXN Amount Sum' }}
						/>
					</Boxx>
				</Grid>


				<Grid item style={{ display: 'flex', flexDirection: 'row', justifyContent:'center' }} flexDirection={'row'}>
					<Boxx style={{ width: 'fit-content', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

						<Plot
							data={[
								{
									type: 'bar',
									x: xWeekly,
									y: yWeekly
								}
							]}
							layout={{ title: 'Weekly TXN Count' }}
						/>
					</Boxx>
					<Boxx style={{ width: 'fit-content', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

						<Plot
							data={[
								{
									type: 'bar',
									x: xWeekly,
									y: yWeeklySum
								}
							]}
							layout={{ title: 'Weekly TXN Amount Sum' }}
						/>
					</Boxx>
				</Grid>


				<Grid item style={{ display: 'flex', flexDirection: 'row', justifyContent:'center' }} flexDirection={'row'}>
					<Boxx style={{ width: 'fit-content', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

						<Plot
							data={[
								{
									type: 'bar',
									x: xMonthly,
									y: yMonthly
								}
							]}
							layout={{ title: 'Monthly TXN Count' }}
						/>
					</Boxx>
					<Boxx style={{ width: 'fit-content', height: 'fit-content', alignItems: 'center', marginTop: 20 }}>

						<Plot
							data={[
								{
									type: 'bar',
									x: xMonthly,
									y: yMonthlySum
								}
							]}
							layout={{ title: 'Monthly TXN  Amount Sum' }}
						/>
					</Boxx>
				</Grid>
			</Grid>}
		</div>
	)
}

export default Histograms;

const Boxx = styled(Box)`
display: flex;
// background: radial-gradient(circle, rgba(0,212,255,1) 6%, rgba(2,0,36,1) 81%, rgba(9,31,121,1) 100%);
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
