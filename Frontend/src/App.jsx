import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './pages/Login'

function App() {
  return (
    <BrowserRouter>
    <div>
        <Routes>
          <Route path='/' element={<Login />} />
        </Routes>
    </div>
    </BrowserRouter>
  )
}

export default App
