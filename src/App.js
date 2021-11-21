import './App.css';
import { Grid } from '@mui/material';
import styled from 'styled-components';
import TraderView from './components/TraderView';
import Signup from './components/Signup';
import Login from './components/Login';
import { useEffect, useState } from 'react';
import TradingPage from './components/TradingPage';

function App() {
  const [type, setType] = useState('T')
  const logout = () => setType('')
  useEffect(() => {
  }, [])
  return (
    <MainGrid container flex flexDirection={'row'} style={{ height: '100vh' }}>
      <Grid item md={12} lg={12}
        style={{
          backgroundColor: '#000000',
          backgroundImage: 'linear-gradient(147deg, #000000 0%, #04619f 74%)',
          border: '2px solid white',
        }}
      >
        {/* <TradingView /> */}
        {type === '' ? <Login
          setLoginType={async (val) => {
            setType(val)
          }} /> :
          type === 'M' ?
            <>
              {/* <ManagerView logout={logout}/> */}
            </>
            : type === 'T' ?
              <>
                <TraderView logout={logout}/>
              </>
              :
              <><TradingPage logout={logout}/></>
        }
        {/* <Signup/> */}
      </Grid>
    </MainGrid>

  );
}

export default App;
const MainGrid = styled(Grid)`
// background: radial-gradient(circle at 100%, #333, #333 50%, #eee 75%, #333 75%);
// backdrop-filter: blur(72px);
`