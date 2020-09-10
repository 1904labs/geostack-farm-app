import React from 'react';
import {
  Nav,
  Navbar,
  Form,
  Button,
  FormControl
} from 'react-bootstrap';



class TopNav extends React.Component {

    render(){
        return (
            <Navbar sticky="top" variant="dark">
                <Navbar.Brand href= "/" >F2C</Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="/">View Map</Nav.Link>
                    <Nav.Link href="#list">View List</Nav.Link>
                    <Nav.Link href="#sell">Sell Item</Nav.Link>
                </Nav>
                <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-light">Search</Button>
                </Form>
            </Navbar>
        )
    }
}

export default TopNav
