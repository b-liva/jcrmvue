import {gql} from "apollo-boost";

export const GET_SALES_EXP = gql`
query{
  users(salesExp:true) {
    edges {
      node {
        lastName
        id
      }
    }
  }
}
`;
