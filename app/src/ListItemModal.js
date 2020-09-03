import React from 'react';
import {Nav, Modal, Button} from 'react-bootstrap';
import ListItemForm from './ListItemForm'


class ListItemModal extends React.Component {
    constructor(props) {
        super(props);
        this.wrapper = React.createRef();
        this.state = { isShown: false };
        this.handleClose = this.handleClose.bind(this);
        this.handleShow = this.handleShow.bind(this);
    }
  
    handleClose(event) {
        this.setState({ isShown: false });
    }
    handleShow(event) {
        this.setState({ isShown: true });
    }
  
    render(){
        return (
        <>
            <Nav.Link onClick={this.handleShow}>Sell Item</Nav.Link>
    
            <Modal show={this.state.isShown} onHide={this.handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>Sell Item</Modal.Title>
            </Modal.Header>
            <ListItemForm />
            <Modal.Footer>
                <Button variant="secondary" onClick={this.handleClose}>
                Close
                </Button>
            </Modal.Footer>
            </Modal>
        </>
        );
    }
}

export default ListItemModal