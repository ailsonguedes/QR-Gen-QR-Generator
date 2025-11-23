import { MainQr } from './components/MainQR/MainQr'
import { NavBar } from './components/NavBar/NavBar'
import { Footer } from './components/Footer/Footer'

import './App.css'
import '../src/assets/css/theme.css'

function App() {
  return (
    <>
      <NavBar />

      <main className='content-wrapper'>
        <MainQr />
      </main>
      
      <Footer />
    </>
  )
}

export default App
