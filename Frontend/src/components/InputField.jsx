import React from 'react'

function InputField({type="text", placeholder, name, value, onchange}) {
  return (
    <input 
    type={type}
    placeholder={placeholder}
    name={name}
    value={value}
    onChange={onchange}
    className="p-2 m-2 w-[90%] lg:w-[50%] px-3 text-white bg-gray-900 rounded-full shadow-lg hover:bg-white hover:rounded-xl hover:text-black cursor-pointer"
     />
  )
}

export default InputField