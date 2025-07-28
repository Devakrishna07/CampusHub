import React from 'react'
import { SideLinedText } from '../components/LinedText'

function HomePage() {
  return (
    <div className='w-screen flex flex-col items-center justify-start min-h-screen bg-gradient-to-r from-black to-gray-900'>
        <div className='w-[95%] backdrop-blur-lg bg-white/10 border border-white/20 flex flex-col md:flex-row items-center justify-evenly mt-[55px]'>
        {/*Carousel here*/}
        <div className='w-full md:w-[50vw] h-[25dvh] md:h-[50vh] bg-gradient-to-r flex items-center justify-center m-2'>
            <h1 className='text-white text-3xl font-bold italic'>Image here</h1>
        </div>
        {/*Text here*/}
        <div className='flex-grow flex items-center justify-center my-2'>
            <h1 className='text-white text-2xl font-bold italic'>text here</h1>
        </div>
        </div>

        {/*Latest Events*/}
        <div className='w-[95%] flex flex-col items-center justify-start backdrop-blur-lg bg-white/10 border border-white/10 rounded-lg m-2 p-2'>
        <SideLinedText text={"Latest Events"}/>
        </div>
      
    </div>
  )
}

export default HomePage
