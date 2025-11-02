
#from langchain_core.tools import tool
from typing import Any, Dict, List
from langchain.tools import tool
from datetime import datetime, date


@tool
def order_details(order_id: str) -> Dict[str, Any]:
    """returns details of the order including customer id
    
    Args:
        order_id: The order ID to retrieve details for
        
    Returns:
        Dictionary containing order information
    """
    return {
        'product_name': 'samsung galaxy a35', 
        'customer_id': 112, 
        'purchase_date': '2025-10-30', 
        'product_class': 'mobile_phone',
        'return_window': '10 days'
    }


@tool
def customer_details(customer_id: int) -> Dict[str, Any]:
    """Tool definition to check customer details including trust score
    
    Args:
        customer_id: The customer ID to retrieve details for
        
    Returns:
        Dictionary containing customer information including trust score
    """
    return {
        'customer_name': 'goku', 
        'customer_age': '25',
        'customer_email': 'test@mail.com',
        'phone': '12345',
        'trust_score': 10
    }


@tool
def approve_or_reject(decision: str) -> Dict[str, Any]:
    """Final Mandatory Tool to approve or reject the return
    
    Args:
        decision: Either "APPROVED" or "REJECTED"
        
    Returns:
        Dictionary containing the final decision
    """
    print(f"{'='*60}\nFINAL DECISION: {decision}\n{'='*60}")
    return {
        'final_decision': decision,
        'timestamp': str(datetime.now()),
        'decision_reason': 'Automated approval based on return policy and customer trust score'
    }
