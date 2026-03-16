from datetime import datetime
from typing import List

class Business:
    def __init__(self, name: str, category: str, description: str):
        self.name = name
        self.category = category
        self.description = description
        self.added_time = datetime.now()

    def __str__(self):
        return f"{self.name} ({self.category}) - Added: {self.added_time.strftime('%Y-%m-%d %H:%M:%S')}"

class Directory:
    def __init__(self):
        self.businesses: List[Business] = []
        self.total: int = 0

    def add_business(self, name: str, category: str, description: str):
        business = Business(name, category, description)
        self.businesses.append(business)  # Stack (LIFO)
        self.total += 1

    def get_recent_businesses(self, num: int = 3) -> List[Business]:
        return self.businesses[-num:] if num <= self.total else self.businesses

    def get_all_businesses(self) -> List[Business]:
        return self.businesses

# Test block (run to check)
if __name__ == "__main__":
    dir = Directory()
    dir.add_business("Tech Hub Kano-updated", "Tech", "Software solutions")
    dir.add_business("MAAUN Cafe", "Food", "Campus coffee shop")
    dir.add_business("Nigerian Books", "Retail", "Local bookstore")
    print("Recent Businesses (LIFO):")
    for b in dir.get_recent_businesses():
        print(b)
    print(f"Total Businesses: {dir.total}")
