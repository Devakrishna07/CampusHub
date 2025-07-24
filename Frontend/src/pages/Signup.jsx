import React, { useState } from 'react';
import api from "../services/api";
import InputField from '../components/InputField';
import logo from "../assets/logo.png";
import { useNavigate, Link } from 'react-router-dom';

function Signup() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const [email, setEmail] = useState('');
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        if (password !== password2) {
            alert("passwords do not match");
            return;
        }
        try {
            const response = await api.post('/users/register/', {
                username,
                password,
                password2,
                first_name: firstname,
                last_name: lastname,
                email
            });

            alert("user created successfully");
            navigate('/login');

        } catch (err) {
            alert("Try again later");
            console.error(err);
        }
    }

    return (
        <div className="w-screen min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-black to-gray-900 px-4">
            <img src={logo} alt="logo" className='h-10 md:h-24 absolute top-3 left-3' />
            <form
                onSubmit={handleLogin}
                className="flex flex-col w-[95%] sm:w-[85%] md:w-[60%] lg:w-[40%] backdrop-blur-md bg-white/15 border border-white/20 shadow-xl py-6 px-6 items-center justify-center rounded-xl overflow-hidden"
            >
                <h1 className="text-2xl sm:text-3xl font-bold text-white mb-6 self-start">Signup</h1>
                <InputField type='text' name="username" placeholder={"username"} value={username} onchange={(e) => setUsername(e.target.value)} />
                <InputField type='email' name="email" placeholder={"Email"} value={email} onchange={(e) => setEmail(e.target.value)} />
                <InputField type='text' name="firstname" placeholder={"First Name"} value={firstname} onchange={(e) => setFirstname(e.target.value)} />
                <InputField type='text' name="lastname" placeholder={"Last Name"} value={lastname} onchange={(e) => setLastname(e.target.value)} />
                <InputField type='password' name="password" placeholder={"Password"} value={password} onchange={(e) => setPassword(e.target.value)} />
                <InputField type='password' name="password2" placeholder={"Confirm Password"} value={password2} onchange={(e) => setPassword2(e.target.value)} />
                <button className="bg-white w-[70%] sm:w-[50%] md:w-[40%] rounded-full p-2 font-bold mt-4 mb-6 hover:bg-black hover:text-white hover:rounded-xl transition-all">
                    Signup
                </button>
                <div className="w-full flex items-center justify-center pb-3">
                    <h1 className='font-bold text-white hover:text-blue-500 cursor-pointer text-sm sm:text-base'>
                        <Link to="/login">login existing account ?</Link>
                    </h1>
                </div>
            </form>
        </div>
    )
}

export default Signup;
