def is_valid_IPv4_octet(octet):
    
    if not octet.isdigit():
        return False
    
    num = int(octet)

    if num < 0 or num > 255:
        return False

    if octet[0] == "0" and len(octet) > 1:
        return False
    
    return True

def is_valid_IPv4(ip):
    
    octets = ip.split(".")

    if len(octets) != 4:
        return False

    for octet in octets:
        if not is_valid_IPv4_octet(octet):
            return False
    
    return True

def is_valid_IPv6_hextet(hextet):
    if len(hextet) < 1 or len(hextet) > 4:
        return False
    
    try:
        value = int(hextet, 16)
        if value < 0 or value > 0xFFFF:
            return False
    except ValueError:
        return False
    
    return True

def is_valid_IPv6(ip):
    hextets = ip.split(":")

    if len(hextets) != 8:
        return False

    for hextet in hextets:
        if not is_valid_IPv6_hextet(hextet):
            return False
    
    return True

def is_valid_IP(ip):
    
    return is_valid_IPv4(ip) or is_valid_IPv6(ip)