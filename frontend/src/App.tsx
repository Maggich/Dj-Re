import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/login/login";
import Register from "./components/register/register";
import Main from "./components/main/main";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/main" element={<Main />} />
    </Routes>
  );
}

export default App;