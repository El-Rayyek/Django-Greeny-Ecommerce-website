DB Analysis
    products:
        Product:
            -name
            -SKU
            -price
            -describtion
            -tags
            --weight
            -flag :new : feature

        Category:
            -name
            -image
        
        Brand:
            -name
        
        reviews:
            -product
            -user
            -rate
            -create_date
            -review

        images:
            -product
            -image

        Copones:



    users:
        Profile:
            -name
            -email
            -image

        user_number_phone:
            -user
            -phone namber
            -type
        user address:
            -user
            -address
            -title



    Orders:
        Orders
            -Id
            -Order_status[Recieved,Processed,Shipped,Delivered]
            -Order_Time
            -Delivery_Time
            -Sub_Total
            -Discount
            -Delivery Fee
            -Total
            -Delivery Location
        
        Order_Detail:
            -serial
            -order
            -product
            -price
            -brand
            -quantity



