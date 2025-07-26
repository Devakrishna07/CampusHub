import React from 'react'
import LinedText, { SideLinedText } from '../components/LinedText'
import { useNavigate, Link } from 'react-router-dom'
import { FaFacebook, FaInstagram } from 'react-icons/fa'
import { FaWebAwesome } from 'react-icons/fa6'
import SpanText1 from '../components/SpanText1'

function Eventpage() {
    return (
        <div className="w-screen min-h-screen bg-gradient-to-r from-black to-gray-900 flex flex-col items-center justify-start pt-4">
            <div className="w-[90%] backdrop-blur-md bg-white/10 border border-white/10 shadow-lg rounded-md p-2 flex flex-col items-center justify-start mb-4">
                <div className='w-full flex flex-col-reverse md:flex-row items-center md:items-start justify-center py-4'>
                    {/*left section */}
                    <div className='w-full flex-col items-start justify-start pr-2'>
                        <SideLinedText text={"Title"} />
                        <SpanText1 title={"Date"} text={"21 August 2003"} />
                        <SpanText1 title={"Time"} text={"2:00 pm"} />
                        <SpanText1 title={"Venue"} text={"College Of Engineering Poonjar"} />
                        <SpanText1 title={"Organizer"} text={"FOSS CLUB CEP"} />

                    {/*connect with us*/}
                    <div className='w-full pt-4 flex flex-col px-3 pb-3'>
                        <h1 className='text-white text-xl font-bold'>Connect with Us</h1>
                        <div className='flex items-start justify-start py-4'>
                            <a href="https://picsum.dev/300/200"><FaFacebook className='text-white text-3xl mx-3 hover:text-black hover:bg-white hover:rounded-full' /></a>
                            <a href="https://picsum.dev/300/200"><FaInstagram className='text-white text-3xl mx-4 hover:text-black hover:bg-white hover:rounded-full' /></a>
                            <a href="https://picsum.dev/300/200"><FaWebAwesome className='text-white text-3xl mx-3 hover:text-black hover:bg-white hover:rounded-full' /></a>
                        </div>
                    </div>
                    {/*Organizer Info*/}
                    <div className='w-full flex flex-col items-start justify-start'>
                        <SideLinedText text={"Organizer Info"} />
                        <SpanText1 title={"Organizer"} text={"FOSS CLUB CEP"} />
                        <SpanText1 title={"Coordinator"} text={"Deva Prasad NR"} />
                        <SpanText1 title={"Contact Number"} text={"9446476637"} />
                    </div>
                    </div>
                    {/*right section */}
                    <div className=' flex w-full items-center justify-center pb-4 md:pb-0 px-2 md:px-8'>
                        <div className='w-full aspect-square bg-gradient-to-r from-black to-gray-900'></div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Eventpage
