import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  Row,
  Col,
  Image,
  ListGroup,
  Button,
  Card,
  Form,
} from "react-bootstrap";
import Rating from "../Rating";
import Loader from "../Loader";
import Message from "../Message";
import axios from "../../api/axois";
import { useParams } from "react-router-dom";

function ProductScreen() {
  const { id } = useParams();
  const [error, setError] = useState(null);
  const [product, setProduct] = useState([]);
  const [qty, setQty] = useState(1);
  const [cart, setCart]=useState([])

  useEffect(() => {
    getProducts();
  setCart(JSON.parse(localStorage.getItem("cart")) !==null? JSON.parse(localStorage.getItem("cart")):[])
  }, []);

  const getProducts = async () => {
    try {
      const { data } = await axios.get("/api/products/" + id);
      setProduct(data);
    } catch (error) {
      setError(
        error.response.data.details
          ? error.response.data.details
          : "Request failed with status code 401"
      );
    }
  };
  const addToCartHandler = (product) => {
    const payload= {
      product: product._id,
      name: product.name,
      image: product.image,
      price: product.price,
      countInStock: product.countInStock,
      qty
  }
  if(cart.length===0){
    console.log('if');
    cart.push(payload)
  }
  else{
    // console.log('else');
    // cart.forEach(x=> x.product===product._id ? x.qty+=qty: cart.push(payload))
    if(cart.find(x=> x.product == payload.product)){
      cart.forEach(x=> x.product===payload.product ? x.qty+=qty: qty)
    }else{
      cart.push(payload)
    }
  }
  console.log(cart);
    localStorage.setItem("cart", JSON.stringify(cart))
  };

  return (
    <div>
      <Link to="/" className="btn btn-dark my-3">
        {" "}
        Go Back
      </Link>

      {error ? (
        <Message variant="danger">{error} </Message>
      ) : (
        <Row>
          <Col md={6}>
            <Image src={product.image} alt={product.name} fluid />
          </Col>

          <Col md={3}>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <h3>{product.name}</h3>
              </ListGroup.Item>
              <ListGroup.Item>
                <Rating
                  value={product.rating}
                  text={`${product.numReviews} reviews`}
                  color={"#f8e825"}
                />
              </ListGroup.Item>
              <ListGroup.Item>Price: ${product.price}</ListGroup.Item>

              <ListGroup.Item>
                Description: {product.description}
              </ListGroup.Item>
            </ListGroup>
          </Col>
          <Col md={3}>
            <Card>
              <ListGroup variant="flush">
                <ListGroup.Item>
                  <Row>
                    <Col>Price:</Col>
                    <Col>
                      <strong>${product.price}</strong>
                    </Col>
                  </Row>
                </ListGroup.Item>
                <ListGroup.Item>
                  <Row>
                    <Col>Status:</Col>
                    <Col>
                      {product.countInStock > 0 ? "In Stock" : "Out of Stock"}
                    </Col>
                  </Row>
                </ListGroup.Item>

                {product.countInStock > 0 && (
                  <ListGroup.Item>
                    <Message variant="success">In stock</Message>
                    <Row>
                      <Col>Qty</Col>
                      <Col xs="auto" className="my-1">
                        <Form.Control
                          as="select"
                          value={qty}
                          onChange={(e) => setQty(e.target.value)}
                        >
                          {[...Array(product.countInStock).keys()].map((x) => (
                            <option key={x + 1} value={x + 1}>
                              {x + 1}
                            </option>
                          ))}
                        </Form.Control>
                      </Col>
                    </Row>
                  </ListGroup.Item>
                )}

                {product.countInStock === 0 && (
                  <ListGroup.Item>
                    {" "}
                    <Message variant="danger">Out of stock</Message>
                  </ListGroup.Item>
                )}

                <ListGroup.Item>
                  <Button
                    className="btn-block"
                    disabled={product.countInStock == 0}
                    type="button"
                    onClick={()=>{addToCartHandler(product)}}
                  >
                    Add to Cart
                  </Button>
                </ListGroup.Item>
              </ListGroup>
            </Card>
          </Col>
        </Row>
      )}
    </div>
  );
}

export default ProductScreen;
