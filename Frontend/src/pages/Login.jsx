import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import logo from '../assets/logo.png';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async(e) => {
        e.preventDefault();
        try{
            const response = await api.post('/users/token/', {
                username,
                password
            });
            const {access, refresh} = response.data;

            localStorage.setItem('accessToken',access);
            localStorage.setItem('refreshToken',refresh);
            alert("login sucessfull");
            navigate('/home');
        }catch (err){
            console.error(err);
            alert("login failed");
        }
    };

  return (
    <div className="w-screen min-h-screen bg-gradient-to-r from-black to-gray-900 flex items-center justify-center">
        <img src={logo} alt="CampusHub" className="absolute top-1 left-1 w-40" />
        <form onSubmit={handleLogin} className="backdrop-blur-md bg-white/10 border border-white/10 shadow-lg rounded-xl p-2 flex flex-col items-center justify-center w-[90%] xl:w-[30%] h-full md:aspect-square">
            <h1 className="md:absolute top-8 left-10 text-white text-2xl font-bold shadow-xl">Login</h1>
            <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} className="rounded-xl p-2 bg-gray-900 m-4 w-[70%] hover:bg-white cursor-pointer" />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="rounded-xl p-2 bg-gray-900 m-4 w-[70%] hover:bg-white cursor-pointer" />
            <button className="bg-white px-4 py-1 rounded-full font-semibold m-3 hover:rounded-xl hover:bg-black hover:text-white">Login</button>
            <div className="flex flex-row w-full md:w-[80%] items-center justify-between pt-3">
                <h3 className="md:text-lg hover:text-blue-500 cursor-pointer"><a>create account</a></h3>
                <h3 className="md:text-lg hover:text-blue-500 cursor-pointer"><a>Forgot password ?</a></h3>
            </div>
        </form>
    </div>
  )
}

export default Login
