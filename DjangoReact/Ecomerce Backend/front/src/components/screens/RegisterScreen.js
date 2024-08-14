import React, { useState } from "react";
import axios from '../../api/axois'
import { Link } from "react-router-dom";
import Message from "../Message";
import { Row, Col, Form, Button } from "react-bootstrap";
import FormContainer from "../FormContainer";
import { useNavigate } from 'react-router-dom';

function RegisterScreen() {
  const navigate = useNavigate();
  const [error,setError]= useState(null)
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message,setMessage]= useState(null)
  const [confirmPassword, setConfirmPassword] = useState("");

  const submitHandler = async(e) => {
    e.preventDefault();
    if (password != confirmPassword) {
      setMessage("Password do not Match");
    } else {
      try{
      const {data}= await axios.post('/api/users/register/',
      {'name':name,'email':email,'password':password } )
      if(data){
        navigate('/login')
      }
      }catch(error){
        setError(error.response.data.details)
      }
    }
  };
  return (
    <div>
      <FormContainer>
        <h1>Sign Up</h1>
        {message && <Message variant="danger">{message}</Message>}
        {error && <Message variant="danger">{error}</Message>}

        <Form onSubmit={submitHandler}>
          <Form.Group controlId="name">
            <Form.Label>Name</Form.Label>
            <Form.Control
              type="name"
              placeholder="Enter Name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="email">
            <Form.Label>Email Address </Form.Label>
            <Form.Control
              required
              type="email"
              placeholder="Enter Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control
              required
              type="password"
              placeholder="Enter Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="password">
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control
              required
              type="password"
              placeholder="Confirm Password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Button className="mt-3" type="submit" variant="success">
            Register
          </Button>
        </Form>

        <Row className="py-3">
          <Col>
            Already User?
            <Link to={"/login"}>Sign In</Link>
          </Col>
        </Row>
      </FormContainer>
    </div>
  );
}

export default RegisterScreen;
