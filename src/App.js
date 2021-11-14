import './App.css';
import TradingView from './components/TradingPage';
import { Grid } from '@mui/material';
import styled from 'styled-components';
import Snackbar from '@mui/material/Snackbar';
import TraderView from './components/TraderView';

function App() {
  return (
    <MainGrid container flex flexDirection={'row'} style={{ height: '100vh' }}>
      {/* <Grid item md={2} lg={2}
        style={{
          // backgroundColor: 'green',
          border: '2px solid white',
          borderColor: 'black',
          height: '100%'
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'center', alignSelf: 'center' }}>
          Nav
        </div>

      </Grid> */}
      <Grid item md={12} lg={12}
        style={{
          backgroundColor: '#000000',
          backgroundImage: 'linear-gradient(147deg, #000000 0%, #04619f 74%)',
          border: '2px solid white',
        }}
      >
        {/* <TradingView /> */}
        <TraderView/>
      </Grid>
    </MainGrid>

  );
}

export default App;
const MainGrid = styled(Grid)`
// background: radial-gradient(circle at 100%, #333, #333 50%, #eee 75%, #333 75%);
// backdrop-filter: blur(72px);
`