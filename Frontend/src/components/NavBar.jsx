import React, { useState } from 'react'
import logo from '../assets/logo.png'
import { useNavigate, Link } from 'react-router-dom'
import { FaUser } from 'react-icons/fa'

function NavBar() {
    const navElements = [
        {id:1, name : "Home", Link : "/HomePage"},
        {id:2, name:"Events", Link: "/Events" },
        {id:3, name:"Clubs", Link: "/Clubs"},
        {id:4, name:"Contact", Link:"/Contact"},
    ]
  return (
    <div className='w-full flex items-center justify-between fixed top-0 left-0 z-10 backdrop-blur-md bg-white/10 border border-white/10 shadow-lg rounded-b-xl h-[50px] overflow-hidden'>
        <img src={logo} alt="logo" className='h-[40px] m-2' />
        <div className='flex-grow flex items-center justify-end'>
            {/* nav text md*/}
            <div className='hidden md:flex w-[50%] items-center justify-end px-2'>
                {navElements.map((nav, index) => (
                <h3 key={index} className='text-sm font-bold text-white mx-2 hover:text-black hover:rounded-full hover:bg-white'><Link to={nav.Link}>{nav.name}</Link></h3>
            ))}
            </div>
            {/*User logo and effects*/}
            <div className='hidden md:flex mx-3'>
                <h1><FaUser className='text-4xl bg-white rounded-full p-1 hover:bg-black hover:text-white'/></h1>
            </div>
        </div>

    </div>
  )
}

export default NavBar
