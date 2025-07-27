import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './pages/Login'
import Signup from './pages/Signup'
import Eventpage from './pages/Eventpage'
import LoadingPage from './components/LoadingPage'
import NavBar from './components/NavBar'
import HomePage from './pages/HomePage'

function App() {
  return (
    <BrowserRouter>
    <div>
      <NavBar />
        <Routes>
          <Route path='/login' element={<Login />} />
          <Route path='/' element={<Signup />} />
          <Route path='/event' element={<Eventpage />} />
          <Route path='/home' element={<HomePage />} />
        </Routes>
    </div>
    </BrowserRouter>
  )
}

export default App
