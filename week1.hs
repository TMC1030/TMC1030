--Q1
timesTen :: Int -> Int
timesTen n = 10 * n

--Q2
sumThree :: Int -> Int -> Int -> Int
sumThree a b c = a + b + c --Each Int requires different seperate arguments

--Q3
areaOfCircle :: Float -> Float
areaOfCircle n = pi * n ^ 2

--Q4
volumeOfCylinder :: Float -> Float -> Float
volumeOfCylinder radius height = areaOfCircle radius * height

--Q5
distance :: Float -> Float -> Float -> Float -> Float
distance a b c d = sqrt((b - d)^2 + (a - c)^2)

--Q6
threeDifferent :: Int -> Int -> Int -> Bool
threeDifferent x y z = x /= y && x /= z && y /= z

--Q7
divisibleBy :: Int -> Int -> Bool
divisibleBy x y = x `mod` y == 0   -- `mod` -> return the remainder

--Q8 
isEven :: Int -> Bool
isEven x = x `mod` 2 == 0

--Q9
averageThree :: Int -> Int -> Int -> Float
averageThree a b c = fromIntegral (a + b + c) / 3 -- fromIntegral -> Converts Int to another numeric type

--10
absolute :: Int -> Int
absolute x = if x < 0 then -x else x