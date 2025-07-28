

import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom';
import { useAuth } from '../services/AuthContext';

const ProtectedRoute = ({children}) => {
    const {isAuthenticated} = useAuth();

    if(!isAuthenticated){
        return <Navigate to="/login" replace />;
    }
  return children;
}

export default ProtectedRoute