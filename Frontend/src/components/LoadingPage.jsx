import React from 'react';

function LoadingPage() {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white rounded-lg shadow-lg p-6 w-80 text-center">
        <h2 className="text-xl font-bold mb-2">Loading</h2>
        <p className="mb-4">Please wait...</p>
      </div>
    </div>
  );
}

export default LoadingPage;
