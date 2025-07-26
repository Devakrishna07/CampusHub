import React from 'react'

function SpanText1({title, text}) {
  return (
    <div className='w-full'>
        <h1 className='text-white md:text-xl py-3'>
        {title} :
       <span className='font-semibold text-sm md:text-xl italic px-2'>
        {text}
       </span> 
    </h1>
    <hr />
    </div>
  )
}

export default SpanText1
