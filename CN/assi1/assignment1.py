import ipaddress  # Import the 'ipaddress' module for working with IP addresses and networks

# Function to calculate subnet information
def calculate_subnet_info(ip_address, subnet_mask):
    # Create an IPv4 network object based on the input IP address and subnet mask
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    
    # Calculate the number of subnets and hosts per subnet
    num_subnets = len(list(network.subnets()))
    num_hosts_per_subnet = network.num_addresses - 2  # Subtract 2 for network and broadcast addresses
    
    # Create empty lists to store network IDs and broadcast IDs for each subnet
    network_ids = []
    broadcast_ids = []
    
    # Calculate and store network and broadcast IDs for each subnet
    for subnet in network.subnets():
        network_ids.append(subnet.network_address)
        broadcast_ids.append(subnet.broadcast_address)
    
    # Return the calculated values
    return num_subnets, num_hosts_per_subnet, network_ids, broadcast_ids

# Main function
def main():
    # Prompt the user to select a class (A, B, C)
    print("Select the class (A, B, C):")
    selected_class = input().strip().upper()
    
    # Check if the selected class is valid (A, B, or C)
    if selected_class not in ['A', 'B', 'C']:
        print("Invalid class selection. Please choose A, B, or C.")
        return
    
    # Determine the subnet mask based on the selected class
    subnet_mask = {'A': '8', 'B': '16', 'C': '24'}[selected_class]
    
    # Prompt the user to enter an IP address within the selected class
    print(f"Enter the IP address (Class {selected_class}):")
    ip_address = input().strip()
    
    # Calculate subnet information using the provided IP address and subnet mask
    num_subnets, num_hosts_per_subnet, network_ids, broadcast_ids = calculate_subnet_info(ip_address, subnet_mask)
    
    # Display the calculated subnet information
    print(f"1. Number of subnets will be created: {num_subnets}")
    print(f"2. Number of hosts per subnet: {num_hosts_per_subnet}")
    print("3. Network id and broadcast id of each network:")
    for i in range(num_subnets):
        print(f"   Subnet {i+1}: Network ID - {network_ids[i]}, Broadcast ID - {broadcast_ids[i]}")
    
    # Display the range of subnet mask for the selected class
    subnet_range_start = network_ids[0]
    subnet_range_end = broadcast_ids[-1]
    print(f"4. Range of subnet mask (Class {selected_class}): {subnet_range_start} - {subnet_range_end}")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the program
