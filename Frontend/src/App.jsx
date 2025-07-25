import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './pages/Login'
import Signup from './pages/Signup'
import Eventpage from './pages/Eventpage'

function App() {
  return (
    <BrowserRouter>
    <div>
        <Routes>
          <Route path='/login' element={<Login />} />
          <Route path='/' element={<Signup />} />
          <Route path='/event' element={<Eventpage />} />
        </Routes>
    </div>
    </BrowserRouter>
  )
}

export default App
