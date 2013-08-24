
from Adafruit_MCP230xx import Adafruit_MCP230XX
import time


if __name__ == '__main__':
    mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16)

    # ***************************************************
    # Set num_gpios to 8 for MCP23008 or 16 for MCP23017!
	# If you have a new Pi you may also need to add:
	# busnum = 1
	# ***************************************************
	
	# Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)
    mcp.config(0, mcp.INPUT)
    mcp.config(1, mcp.INPUT)
    mcp.config(2, mcp.INPUT)
    mcp.config(3, mcp.INPUT)
    mcp.config(4, mcp.INPUT)
    mcp.config(5, mcp.INPUT)
    mcp.config(6, mcp.INPUT)
    mcp.config(7, mcp.INPUT)
	# Set pin 3 to input with the pullup resistor enabled
    #mcp.pullup(3, 1)
    #mcp.pullup(4, 1)
    # Read pin 3 and display the results

	
    # Python speed test on output 0 toggling at max speed
    while (True):
        print "%d: %x" % (0, mcp.input(0) >> 0)
        print "%d: %x" % (1, mcp.input(1) >> 1)
        print "%d: %x" % (2, mcp.input(2) >> 2)
        print "%d: %x" % (3, mcp.input(3) >> 3)
        print "%d: %x" % (4, mcp.input(4) >> 4)
        print "%d: %x" % (5, mcp.input(5) >> 5)
        time.sleep(1)

      
