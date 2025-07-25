import React from 'react'
import LinedText, { SideLinedText } from '../components/LinedText'

function Eventpage() {
    return (
        <div className="w-screen min-h-screen bg-gradient-to-r from-black to-gray-900 flex flex-col items-center justify-start pt-4">
            <div className="w-[90%] backdrop-blur-md bg-white/10 border border-white/10 shadow-lg rounded-md p-2 flex flex-col items-center justify-start">
                <div className="w-[50%] aspect-square bg-gradient-to-r from-black to-gray-900 flex items-center justify-center rounded-xl overflow-hidden">
                    <h1 className='text-white font-bold'>heelo</h1>
                </div>
            
            <div className="w-full flex items-center justify-start py-4 ">
                <LinedText text={"Event Details"} />
            </div>
            </div>
        </div>
    )
}

export default Eventpage
