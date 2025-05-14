import requests
import json
from typing import List, Dict, Any

class APITestResult:
    def __init__(self, product_id: int, defect_type: str, details: str):
        self.product_id = product_id
        self.defect_type = defect_type
        self.details = details

    def __str__(self) -> str:
        return f"Product ID {self.product_id}: {self.defect_type} - {self.details}"

def validate_product(product: Dict[str, Any]) -> List[APITestResult]:
    """
    Validates a single product against the defined rules.
    Returns a list of APITestResult objects for any violations found.
    """
    defects = []
    product_id = product.get('id', 'Unknown')

    # Validate title
    title = product.get('title', '')
    if not isinstance(title, str) or not title.strip():
        defects.append(APITestResult(
            product_id,
            "Invalid Title",
            "Title must be a non-empty string"
        ))

    # Validate price
    price = product.get('price', 0)
    if not isinstance(price, (int, float)) or price < 0:
        defects.append(APITestResult(
            product_id,
            "Invalid Price",
            f"Price must be a non-negative number, got: {price}"
        ))

    # Validate rating
    rating = product.get('rating', {})
    rate = rating.get('rate', 0)
    if not isinstance(rate, (int, float)) or rate > 5:
        defects.append(APITestResult(
            product_id,
            "Invalid Rating",
            f"Rating must be less than or equal to 5, got: {rate}"
        ))

    return defects

def test_fakestore_api() -> None:
    """
    Tests the Fake Store API and prints any validation errors found.
    """
    API_URL = "https://fakestoreapi.com/products"
    
    try:
        # Make the API request
        response = requests.get(API_URL)
        
        # Check status code
        if response.status_code != 200:
            print(f"❌ API request failed with status code: {response.status_code}")
            return

        print("✅ API request successful (Status Code: 200)")
        
        # Parse the response
        products = response.json()
        if not isinstance(products, list):
            print("❌ Expected a list of products, got something else")
            return

        # Validate each product
        all_defects = []
        for product in products:
            defects = validate_product(product)
            all_defects.extend(defects)

        # Print results
        if not all_defects:
            print("✅ All products passed validation!")
        else:
            print("\n🔍 Found the following defects:")
            for defect in all_defects:
                print(f"\n{defect}")

        print(f"\nTotal products tested: {len(products)}")
        print(f"Total defects found: {len(all_defects)}")

    except requests.RequestException as e:
        print(f"❌ Network error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse API response: {e}")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

if __name__ == "__main__":
    test_fakestore_api() 