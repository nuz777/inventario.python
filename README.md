# Inventory Management System (Python)

## 📌 Description
This project is a console-based inventory management system built in Python.  
It allows users to manage products using CRUD operations and store data persistently using CSV files.

---

## 🚀 Features

- Add products
- View inventory
- Search products
- Update products
- Delete products
- Calculate statistics
- Save inventory to CSV
- Load inventory from CSV
- Error handling and validations

---

## 🧱 Data Structure

The inventory is stored as a list of dictionaries:

```python
{
    "nombre": str,
    "precio": float,
    "cantidad": int
}
