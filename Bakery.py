import sys
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def order():
    root = tk.Tk()
    root.withdraw()
    
    menu_items = {
        "Bread": 8.0, "Croissant": 9.0, "Muffin": 8.0, "Cake": 20.0,
        "Milkshake": 12.0, "Chocolate": 2.0,"Veg Puffs": 6.0, "Egg Puffs": 7.0
    }
    
    cart = {}
    purchase = True
    
    menu_display = "Welcome to Fresh Bakes\nHere is the menu!\n\n"
    menu_display += f"{'Item':<24} {'Price':>6}\n"
    menu_display += "-" * 30 + "\n"
    for item, price in menu_items.items():
        menu_display += f"{item:<24} {price:>6.2f}\n"
        
    messagebox.showinfo("Fresh Bakes Menu", menu_display)
    
    while purchase:
        item = simpledialog.askstring("Order", "What are you buying?\n(Type the item name from the menu)")
        
        if item is None:
            break
            
        matched_item = None
        for key in menu_items.keys():
            if key.lower() == item.strip().lower():
                matched_item = key
                break
                
        if not matched_item:
            messagebox.showerror("Invalid Item", f"Sorry, '{item}' is not on the menu. Please try again.")
            messagebox.showinfo("Fresh Bakes Menu", menu_display)
            continue 
            
        num = simpledialog.askinteger("Quantity", f"How many {matched_item}s would you like?", minvalue=1)
        if num is None:
            continue
            
        cost = menu_items[matched_item] * num
        cart_key = f"{matched_item}({num})"
        
        if cart_key in cart:
            cart[cart_key] += cost
        else:
            cart[cart_key] = cost
            
        continue_shopping = messagebox.askyesno("Continue?", "Do you want to continue shopping?")
        if not continue_shopping:
            purchase = False

    if cart:
        total = sum(cart.values())
        
        bill_display = f"{'Item':<24} {'Price':>6}\n"
        bill_display += "-" * 30 + "\n"
        for item, price in cart.items():
            bill_display += f"{item:<24} {price:>6.2f}\n"
        bill_display += "-" * 30 + "\n"
        bill_display += f"{'Total':<24} {total:>6.2f}\n\n"
        bill_display += "Thanks for shopping!\nVisit again!"
        
        def save_bill():
            filepath = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                title="Save Bill"
            )
            if filepath:
                with open(filepath, "w") as f:
                    f.write(bill_display)
                messagebox.showinfo("Success", f"Bill saved successfully to:\n{filepath}")

        root.deiconify()
        root.title("Your Bill")
        
        tk.Label(root, text=bill_display, font=("Courier", 10), justify="left").pack(padx=20, pady=20)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=(0, 20))
        
        tk.Button(btn_frame, text="Print/Save Bill", command=save_bill).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Close", command=root.destroy).pack(side=tk.LEFT, padx=10)
        
        root.mainloop()
    else:
        root.destroy()

if __name__ == "__main__":
    order()
