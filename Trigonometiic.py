import math

def trigonometry_calculator():
    print("Welcome to Harina's Trigonometry Calculator!")
    
    # Ask the user for an angle in degrees
    angle_deg = float(input("Enter an angle in degrees: "))
    
    # Convert the angle to radians because math module uses radians
    angle_rad = math.radians(angle_deg)
    
    # Calculate trigonometric functions
    sine_val = math.sin(angle_rad)
    cosine_val = math.cos(angle_rad)
    
    # Handle the tangent separately because it can be undefined
    try:
        tangent_val = math.tan(angle_rad)
    except:
        tangent_val = "undefined"
    
    # Display the results
    print(f"\nResults for angle {angle_deg}°:")
    print(f"Sine: {sine_val:.4f}")
    print(f"Cosine: {cosine_val:.4f}")
    
    # Handle very large tangent values (e.g., near 90° or 270°)
    if abs(cosine_val) < 1e-10:
        print("Tangent: undefined (cosine is 0)")
    else:
        print(f"Tangent: {tangent_val:.4f}")

# Run the calculator
trigonometry_calculator()
