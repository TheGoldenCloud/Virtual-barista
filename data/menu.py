mymenu = [
    {
        "id": "kiosk_cof_01",
        "name": "Espresso",
        "category": "Hot Coffee",
        "price_eur": 2.0,
        "description": "Quick, rich single-origin shot from Ethiopia. Perfect for a fast morning start.",
        "bean_origin": "Ethiopia Yirgacheffe",
        "prep_time_sec": 45,
        "in_stock": True,
        "packaging": "Paper Shot Cup",
        "sizes": ["Single", "Double"],
        "customizations": {
            "decaf": [True, False],
            "milk": ["None"],
            "syrups": []
        }
    },
    {
        "id": "kiosk_cof_02",
        "name": "Cappuccino To-Go",
        "category": "Hot Coffee",
        "price_eur": 3.0,
        "description": "Double shot with creamy steamed milk in a portable cup with a sip lid.",
        "bean_origin": "House Blend",
        "prep_time_sec": 90,
        "in_stock": True,
        "packaging": "Insulated Paper Cup + Lid",
        "sizes": ["Regular (250ml)", "Large (350ml)"],
        "customizations": {
            "decaf": [True, False],
            "milk": ["Whole", "Oat", "Almond", "Lactose-Free"],
            "syrups": ["Vanilla", "Caramel", "Hazelnut"],
            "extra_shots": [0, 1]
        }
    },
    {
        "id": "kiosk_cof_03",
        "name": "Iced Vanilla Latte",
        "category": "Iced Coffee",
        "price_eur": 3.8,
        "description": "Chilled espresso, fresh milk, and vanilla syrup served over crushed ice with a straw.",
        "bean_origin": "Colombia Huila",
        "prep_time_sec": 60,
        "in_stock": True,
        "packaging": "Clear Iced Cup + Straw",
        "sizes": ["Medium (350ml)", "Large (450ml)"],
        "customizations": {
            "decaf": [True, False],
            "milk": ["Whole", "Oat", "Almond", "Lactose-Free"],
            "syrups": ["Vanilla", "Sugar-Free Vanilla", "Caramel"],
            "ice_level": ["Normal Ice", "Extra Ice", "Less Ice"]
        }
    },
    {
        "id": "kiosk_cof_04",
        "name": "Nitro Cold Brew Draft",
        "category": "Cold Coffee",
        "price_eur": 4.0,
        "description": "Poured straight from the tap in under 10 seconds. Smooth, naturally sweet, and high-caffeine.",
        "bean_origin": "Brazil Mogiana",
        "prep_time_sec": 10,
        "in_stock": True,
        "packaging": "Clear Iced Cup + Sip Lid",
        "sizes": ["Regular (300ml)", "Large (400ml)"],
        "customizations": {
            "syrups": ["None", "Vanilla", "Caramel"]
        }
    },
    {
        "id": "kiosk_bak_01",
        "name": "Butter Croissant (To-Go)",
        "category": "Grab & Go Bakery",
        "price_eur": 2.2,
        "description": "Baked fresh daily, served in a paper bag.",
        "prep_time_sec": 15,
        "in_stock": True,
        "packaging": "Paper Pastry Bag",
        "allergens": ["Gluten", "Lactose", "Eggs"],
        "sizes": ["Standard"],
        "customizations": {
            "warmed": [True, False]
        }
    },
    {
        "id": "kiosk_bak_02",
        "name": "Triple Chocolate Cookie",
        "category": "Grab & Go Bakery",
        "price_eur": 2.5,
        "description": "Rich chewy cookie packed with dark and milk chocolate chunks.",
        "prep_time_sec": 10,
        "in_stock": True,
        "packaging": "Individual Wrapper",
        "allergens": ["Gluten", "Lactose", "Eggs", "Soy"],
        "sizes": ["1 Cookie"],
        "customizations": {}
    },
    {
        "id": "kiosk_merch_01",
        "name": "Ethiopia Yirgacheffe 250g Beans",
        "category": "Beans To-Go",
        "price_eur": 12.0,
        "description": "Sealed bag of whole beans or ground on the spot for your home brewing setup.",
        "prep_time_sec": 60,
        "in_stock": True,
        "packaging": "Sealed Valve Bag",
        "sizes": ["250g Bag"],
        "customizations": {
            "grind_size": ["Whole Beans", "Espresso", "Moka Pot", "Filter / V60", "Turkish"]
        }
    }
]