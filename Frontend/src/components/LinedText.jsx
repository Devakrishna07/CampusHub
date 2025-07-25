import React from 'react'

function LinedText({text}) {
  return (
    <div className='w-full flex items-center justify-center'>
      <div className='flex-grow border border-white '></div>
      <h1 className='text-xl text-white px-2'>{text}</h1>
      <div className='flex-grow border border-white'></div>
    </div>
  )
}

export default LinedText

export function SideLinedText({text}) {
  return (
    <div className='flex w-full items-center justify-start'>
        <h1 className='text-white text-xl font-bold pr-2'>{text}</h1>
        <div className='flex-grow border border-white rounded-full'></div>
    </div>
  )
}


