import {gql} from "apollo-boost";

export const GET_CUSTOMERS = gql`
  query 
  {
  customers {
    edges {
      node {
        name
        orderCount
        customerPaymentAmount
        requestsSet {
          edges {
            node {
              number
              xprefSet {
                edges {
                  node {
                    number
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
`;
export const LIST_CUSTOMERS = gql`
  query{
  customers {
    edges {
      node {
        id
        name
      }
    }
  }
}
`;

export const FIND_CUSTOMER_BY_NAME = gql`
  query($name: String){
  customers(name_Icontains: $name) {
    edges {
      node {
        id
        name
        code
      }
    }
  }
}
`;

export const GET_SUMMARY = gql`
  query 
  topSum{
  routineCount
  servicesCount
  projectCount
  exCount
  ordersCount
}
`;

export const CREATE_PROFORMA = gql`
  mutation{
  createProforma(input: {
    number: 654202,
    reqId: 10,
    dateFa: "1397-12-03",
    expDateFa: "1397-12-08",
    verified:false,
    isActive:true,
    summary: "جزئیات پیش فاکتور"
  }) {
    clientMutationId
  }
}
`;

export const GET_ORDER = gql`
query($nodeId: ID!){
  node(id: $nodeId) {
    id
    ...on RequestNode{
      number
      customer {
        name
      }
    }
  }
}
`;

export const CREATE_PAYMENT = gql`
  mutation{
  createPayment(input: {
    xprefId: 75
    number: 203200,
    amount: 35000000,
    dateFa: "1397-12-08",
    summary: "something new from graphql",
    
  }) {
    clientMutationId
  }
}
`;

export const CREATE_REQUEST = gql`
  mutation AddReq($number: Int!, $date: String!, $customer:ID!, $summary: String) {
    createRequest(
      input: {
        customer:$customer,
        number:$number,
        dateFa:$date,
        summary:$summary
      }
    ) {
     requests {
      id
    }
    }
  }
`;
export const CREATE_SPEC = gql`
   mutation (
  $reqId:ID!,
  $qty: Int!, 
  $type: ID!, 
  $kw:Float!, 
  $rpm: Int!,
  $voltage:Int!,
  $tech: Boolean!,
  $price: Boolean!,
  $permission: Boolean!,
  $sent: Boolean!,
  $cancelled: Boolean!
) {
    createSpec(
      input: {
        reqId:$reqId,
        qty:$qty,
        type:$type,
        kw:$kw,
        rpm:$rpm,
        voltage:$voltage,
        permission:$permission,
        tech: $tech,
        sent:$sent,
        price:$price,
        cancelled:$cancelled
      }
    ) {
    reqSpec {
      id
    }
    }
  }
`;

export const GET_SPEC_SET = gql`
query ($id: ID!){
  specs: order(id:$id) {
    id
    reqspecSet {
      edges {
        node {
          kw
          rpm
          voltage
          tech
        }
      }
    }
  }
}
`;