import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Footer from "./components/Footer";
import Header from "./components/Header";
import HomeScreen from "./components/screens/HomeScreen";
import ProductScreen from "./components/screens/ProductScreen";
import CartScreen from "./components/screens/CartScreen";
import LoginScreen from "./components/screens/LoginScreen";
import RegisterScreen from "./components/screens/RegisterScreen";

function App() {
  return (
    <Router>
      <Header />
      <main className="py-3">
          <Routes>
            <Route path="/" element={<HomeScreen/>} exact />
            <Route path="/login" element={<LoginScreen/>} exact />
            <Route path="/register" element={<RegisterScreen/>} exact />
            <Route path="/product/:id" element={<ProductScreen/>} exact />
            <Route path="/cart/:id?" element={<CartScreen/>} exact />
          </Routes>
      </main>

      <Footer />
    </Router>
  );
}

export default App;
