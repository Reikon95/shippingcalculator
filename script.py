def ground_shipping_cost(weight):
  if weight <= 2:
  	return (1.50 * weight) + 20
  elif (weight > 2) and (weight <= 6):
  	return (3.00 * weight) + 20
  elif (weight > 6) and (weight <= 10):
  	return (4 * weight) + 20
  else:
    return (4.75 * weight) + 20
  
print(ground_shipping_cost(8.4))

prem_ground_shipping = 125.00

def drone_shipping_cost(weight):
  if weight <= 2:
  	return (4.50 * weight) 
  elif (weight > 2) and (weight <= 6):
  	return (9.00 * weight) 
  elif (weight > 6) and (weight <= 10):
  	return (12 * weight) 
  else:
    return (14.75 * weight) 

print(drone_shipping_cost(1.5))

def cheapest_method(weight):
  if (ground_shipping_cost(weight) < drone_shipping_cost(weight)) and (ground_shipping_cost(weight) < prem_ground_shipping):
    return ground_shipping_cost(weight)
  elif (drone_shipping_cost(weight)) < (prem_ground_shipping) and (drone_shipping_cost(weight) < ground_shipping_cost(weight)):
    return drone_shipping_cost(weight)
  else:
    return prem_ground_shipping
print(cheapest_method(1))
