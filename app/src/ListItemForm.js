import React from 'react';
import { Form, Col, Button, Container } from 'react-bootstrap'
import { useFormik } from 'formik';
import * as Yup from 'yup';

const ListItemForm = () => {
    const formik = useFormik({
        initialValues: {
            itemName: '',
            itemDesc: '',
            itemAddr: '',
            itemCity: '',
            itemState: '',
            itemZip: '',
            firstName: '',
            lastName: '',
            email: ''
        },
        validationSchema: Yup.object({
            itemName: Yup.string()
            .max(20, 'Must be 20 characters or less')
            .required('Required'),
            itemDesc: Yup.string()
            .max(1000, 'Must be 1000 characters or less')
            .required('Required'),
            itemAddr: Yup.string()
            .max(50, 'Must be 50 characters or less')
            .required('Required'),
            itemCity: Yup.string()
            .max(50, 'Must be 50 characters or less')
            .required('Required'),
            itemState: Yup.string()
            .max(50, 'Must be 50 characters or less')
            .required('Required'),
            itemZip: Yup.string()
            .max(11, 'Must be 11 characters or less')
            .required('Required'),
            firstName: Yup.string()
            .max(15, 'Must be 15 characters or less')
            .required('Required'),
            lastName: Yup.string()
            .max(20, 'Must be 20 characters or less')
            .required('Required'),
            email: Yup.string()
            .email('Invalid email address')
            .required('Required'),
        }),
        onSubmit: values => {
            alert(JSON.stringify(values, null, 2));
        },
    });
    const handleSubmit = values => {alert(JSON.stringify(values, null, 2))}
    return (
        <Container fluid className="d-flex vh-100 pt-25 bg-dark text-white justify-content-center" >

            <Form onSubmit={handleSubmit} noValidate>
                <Form.Group controlId="itemName">
                <Form.Label>Item Title</Form.Label>
                <Form.Control type="text" placeholder="Title" required />
                <Form.Control.Feedback type="invalid">
                    Please provide a title for the listing.
                </Form.Control.Feedback>
                </Form.Group>

                <Form.Group controlId="itemDesc">
                <Form.Label>Description</Form.Label>
                <Form.Control as="textarea" rows="3" required />
                </Form.Group>

                <Form.Group controlId="itemAddr">
                <Form.Label>Address</Form.Label>
                <Form.Control type="text" placeholder="Address" required />
                <Form.Control.Feedback type="invalid">
                    Please provide a valid address.
                </Form.Control.Feedback>
                </Form.Group>

                <Form.Row>
                    <Form.Group as={Col} md="6" controlId="itemCity">
                        <Form.Label>City</Form.Label>
                        <Form.Control type="text" placeholder="City" required />
                        <Form.Control.Feedback type="invalid">
                            Please provide a valid city.
                        </Form.Control.Feedback>
                    </Form.Group>
                    <Form.Group as={Col} md="3" controlId="itemState">
                        <Form.Label>State</Form.Label>
                        <Form.Control type="text" placeholder="State" required />
                        <Form.Control.Feedback type="invalid">
                            Please provide a valid state.
                        </Form.Control.Feedback>
                    </Form.Group>
                        <Form.Group as={Col} md="3" controlId="itemZip">
                        <Form.Label>Zip</Form.Label>
                        <Form.Control type="text" placeholder="Zip" required />
                        <Form.Control.Feedback type="invalid">
                            Please provide a valid zip.
                        </Form.Control.Feedback>
                    </Form.Group>
                </Form.Row>
                
                <Form.Row>
                    <Form.Group as={Col} md="6" controlId="firstName">
                        <Form.Label>First name</Form.Label>
                        <Form.Control
                            required
                            type="text"
                            placeholder="First name"
                        />
                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                    </Form.Group>
                        <Form.Group as={Col} md="6" controlId="lastName">
                        <Form.Label>Last name</Form.Label>
                        <Form.Control
                            required
                            type="text"
                            placeholder="Last name"
                        />
                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                    </Form.Group>
                </Form.Row>
                <Form.Group controlId="email">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Email"
                        required
                    />
                    <Form.Control.Feedback type="invalid">
                        Please provide a valid email
                    </Form.Control.Feedback>
                </Form.Group>
                <Button type="submit">Submit</Button>
            </Form>
        </Container>
    );
};

export default ListItemForm