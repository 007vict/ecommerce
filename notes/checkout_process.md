# Checkout process

1.Cart -> Checkout view
    ?
    - Login/Register or Enter an Email (as Guest)
    - Shipping Address
    - Billin Info
        - Billing Address
        - Credit Card / Payment

2.Billing App/Component
    - Billing Profile
        - User or Email (Guest Email)
        - generate payment processor token (Stripe or Braintree)

3.Orders / Invoices Component
    - Connect the Billing Profile
    - Shipping / Billing Address
    - Cart
    - Status -- Shipped? Cancelled?