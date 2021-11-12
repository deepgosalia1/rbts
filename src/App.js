import logo from './logo.svg';
import './App.css';
import TradingView from './components/TradingPage';
import { Sidebar } from 'grommet';
import Header from './components/Header'
import Footer from './components/Footer'
import { Grid } from '@mui/material';

function App() {
  return (
    <Grid container flex flexDirection={'column'}>
      <Grid item sm={12} md={12} lg={12}>
        <Sidebar
          header={<Header />}
          gap={'xxsmall'}
          footer={<Footer />}
          style={{ backgroundColor: 'grey' }}
        />
      </Grid>
      <Grid item sm={12} md={12} lg={12}  alignSelf={'center'}>
        <TradingView />
      </Grid>
    </Grid>

  );
}

export default App;
