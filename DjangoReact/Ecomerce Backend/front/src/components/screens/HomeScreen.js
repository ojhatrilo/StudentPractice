import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import Product from "../Product";
import Message from "../Message";
import axios from "../../api/axois";

function HomeScreen() {
  const [error, setError] = useState(null);
  const [products, setProduct] = useState([]);
  useEffect(() => {getProducts()},[]);

  const getProducts = async () => {
    try {
      const { data } = await axios.get("/api/products/");
      setProduct(data)
    } catch (error) {
      setError(
        error.response.data.details
          ? error.response.data.details
          : "Request failed with status code 401"
      );
    }
  };
  return (
    <div>
      <h1 className="text-center">Latest Products</h1>

      {error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <Row>
          {products.map((product) => (
            <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
              {/* <h3>{product.name}</h3> */}
              <Product product={product} />
            </Col>
          ))}
        </Row>
      )}
    </div>
  );
}

export default HomeScreen;
