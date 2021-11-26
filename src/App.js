import './App.css';
import { Grid } from '@mui/material';
import styled from 'styled-components';
import TraderView from './components/TraderView';
import Signup from './components/Signup';
import Login from './components/Login';
import { useEffect, useState } from 'react';
import ManagerView from './components/Manager';
import ClientView from './components/ClientView';
import { Button } from '@tsamantanis/react-glassmorphism'

function App() {
  const [type, setType] = useState('')
  const logout = () => setType('')
  const [userObj, setUserObj] = useState([])
  useEffect(() => {
    console.log('logged in user is:', userObj)
  }, [userObj])
  return (
    <MainGrid container flex flexDirection={'row'} style={{ height: '100vh' }}>
      <Grid item md={12} lg={12}
        style={{
          backgroundColor: '#000000',
          backgroundImage: 'linear-gradient(147deg, #000000 0%, #04619f 74%)',
          border: '2px solid white',
        }}
      >
        <Grid item md={12} lg={12} style={{ display: 'flex', alignItems: 'center', justifyContent:'center'}}>
          <LogoutButton text="Logout" onClick={() => {
            logout()
          }} />
        </Grid>
        {/* <TradingView /> */}
        {type === '' ? <Login
          setLoginType={async (val) => {
            setType(val)
          }}
          getData={async (val) => {
            await setUserObj(val)
          }}
        /> :
          type === 'M' && userObj ?
            <>
              <ManagerView logout={logout} managerData={userObj} />
            </>
            : type === 'T' && userObj ?
              <>
                <TraderView traderData={userObj} logout={logout} />
              </>
              : type === 'C' && userObj &&
              <><ClientView logout={logout} clientData={userObj} /></>
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
const LogoutButton = styled(Button)`

`;