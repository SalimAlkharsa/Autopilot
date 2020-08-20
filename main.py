# Creating Variables
FVelx = float(0.0)  # Final x velocity
FVely = float(0.0)  # Final y velocity
FVelz = float(0.0)  # Final z velocity
# Using Time Variable; As of Right Now, A Place Holder Will Be Used
DummyTime = float(0.0)  # Used to pass in the time elapsed function
# Iterant
i = 1


# Creating Functions:


#Elapsed Time   #Entire function commented out for quick time to test other features
def ElapsedTime(DumyTime):
    #SensorTime = float(input("Time "))
    #InitialTime = DummyTime
    #Elapsed = SensorTime - InitialTime
    #InitialTime = Elapsed
    #return InitialTime
    return 2.0 #Dummy variable

# Height formula
def HeightFunction():
    # In reality I would use sensor data but in the early stages I       will use a dummy number
    yacceleration = 4.0
    time = ElapsedTime(DummyTime)
    height = float(0.5 * yacceleration * time * time)
    return height


# Final XVelocity
def FinalVelx(FVelx):
    xacceleration = 4  # Actual thing would be sensor input
    time = ElapsedTime(DummyTime)
    IVelx = FVelx
    nFVelx = IVelx + xacceleration * time
    IVelx = nFVelx
    return IVelx


# Final YVelocity
def FinalVely(FVely):
    yacceleration = 4.0  # Actual thing would be sensor input
    time = ElapsedTime(DummyTime)
    IVely = FVely
    nFVely = IVely + yacceleration * time
    IVely = nFVely
    return IVely


# Final ZVelocity
def FinalVelz(FVelz):
    zacceleration = 4.0  # Actual thing would be sensor input
    time = ElapsedTime(DummyTime)
    IVelz = FVelz
    nFVelz = IVelz + zacceleration * time
    IVelz = nFVelz
    return IVelz


#Function For Resultant Velocity
def ResultantVel():
    Fx = FinalVelx(FVelx)
    Fy = FinalVely(FVely)
    Fz = FinalVelz(FVelz)
    RVel = (Fx**2+Fy**2+Fz**2)**(1/2)
    return RVel


# Creating a loop to apply everything
while i != 0:
    i += 1
    print("Height:" + str(HeightFunction()))
    FVelx = float(FinalVelx(FVelx))
    print("X-Velocity:" + str(FVelx))
    FVely = float(FinalVely(FVely))
    print("Y-Velocity:" + str(FVely))
    FVelz = float(FinalVelz(FVelz))
    print("Z-Velocity:" + str(FVelz))
    print("Resultant Velocity:" + str(ResultantVel()))
    if i % 25 == 0:
        i = int(input("Enter 0 to stop the loop  "))
    else:
        pass
