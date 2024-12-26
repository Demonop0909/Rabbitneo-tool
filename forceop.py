import mcpi.minecraft as minecraft
import time

# Connect to the Minecraft server
mc = minecraft.Minecraft.create("spymc.xyz", 25565)

# Define the command block location
x, y, z = mc.player.getTilePos()

# Create the command block
mc.setBlock(x, y, z, 137)
mc.setBlockData(x, y, z, 6)

# Set the command block command
mc.setSign(x, y, z, 0, 0, 0, 0, "/forceop <your_username>")

# Wait for the command block to execute
time.sleep(1)

# Remove the command block
mc.setBlock(x, y, z, 0)

print("Forceop permissions should now be granted.")