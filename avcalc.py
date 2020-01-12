x = 1
import math
import time
name = input ("Enter your name : ")
print ("Welcome " + str (name))
print ("Do you want to use calculator?") 
answer = input ("Enter your answer[y/n]: ")
if answer == ("y"): 
 print ("Read the instructions below carefully: ")
 print (" || "," ||", "  ||","  || "," ||","  || "," ||","  || "," ||")
 print (" || "," ||", "  ||","  || "," ||","  || "," ||","  || "," ||")
 print (" || "," ||", "  ||","  || "," ||","  || "," ||","  || "," ||")
 print ("\  /","\  /","\  /","\  /","\  /","\  /","\  /","\  /","\  /")
 print (" \/","  \/","  \/","  \/","  \/","  \/","  \/","  \/","  \/")
 print ("(1)This calculator is typing based only.\n(2)If you enter wrong text you will be taken back to the menu.\n(3)Input data just as prompted then press the enter key once so as to use this calculator correctly.\n(4)When prompted to input numbers do not input the units(only numbers), if you input text the program will crush.\n(5)if you want to customize the calculator right click on the title bar then click on properties.")
 print()
 print ("Finally:")
 print ("(A)This calculator is trademarked by Emmanuel Limisi Muhatia hence no illicit distribution of it.")
 print ("(B)Thank you for reading these.")
 print("(C)May you enjoy using it :)")
 print()
 while x == 1:
  print ("What do you want to calculate?")
  print ("->(1):area\n->(2):volume\n->(3):surface area")
  answer2 = input ("Enter your answer(from the choices provided): ")
  options = ["1","2","3"]
  if answer2 == (options[0]):
    print ("of a?")
    print("->(a):circle\n->(b):rectangle\n->(c):square\n->(d):triangle\n->(e):trapezium\n->(f):parallelogram\n->(g):rhombus\n->(h):kite\n->(i):polygon")
    options2 = ["a","b","c","d","e","f","g","h","i"]
    answer3 = input ("Enter your answer(from the choices provided): ")  
    if answer3 == (options2[0]):
     num1 = input ("Degrees of circle: ")
     num2 = input ("Radius of circle : ")
     result = (float(num1)/360*math.pi*float(num2)*float(num2))
     print ("Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    if answer3 == (options2[1]):
     num1 = input ("Enter length: ")
     num2 = input ("Enter width: ")
     result = (float(num1)*float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    if answer3 == (options2[2]):
     num1 = input ("Enter measurement of side: ")
     result = (float(num1)*float(num1))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    if answer3 == (options2[3]):
     print ("Using? ")
     print("->(a):All three sides\n->(b):Base and height\n->(c):Two sides and included angle")
     options3 = ["a","b","c"]
     answer4 = input ("Enter your answer(from the choices provided): ")
     if answer4 == (options3[1]):
      num1 = input ("Enter measurement of base: ")
      num2 = input ("Enter measurement of height: ")
      result = (0.5*float(num1)*float(num2))
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif answer4 == (options3[2]):
      num1 = input ("Enter measurement of one side: ")
      num2 = input ("Enter measurement of other side: ")
      num3 = input ("Enter value of included angle in degrees: ")
      result = (0.5 * (float(num1) * float(num2)) * (math.sin((math.radians (float(num3))))))
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif answer4 == (options3[0]):
      num1 = input ("Enter length of first side: ")
      num2 = input ("Enter length of second side: ")
      num3 = input ("Enter length of third side: ")
      queen = ((float(num1) + float(num2) + float(num3)))/2
      result = (math.sqrt(float(queen) * (float(queen) - float(num1)) * (float(queen) - float(num2)) * (float(queen) - float(num3))))
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
    if answer3 == (options2[4]):
     num1 = input ("Enter length of longer side: ")
     num2 = input ("Enter length of shorter side: ")
     num3 = input ("Enter measurement of height: ")
     result = (0.5* float(num3) * (float(num2) + float(num1)))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue 
    if answer3 == (options2[5]):
     num1 = input ("Enter measurement of base: ")
     num2 = input ("Enter measurement of perpendicular height: ")
     result = (float(num1) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    if answer3 == (options2[6]):
     print ("using:")
     print ("->(a):diagonals\n->(b):outer dimensions")
     answer4 =input ("Enter your answer: ")
     options3 = ["a","b"]
     if answer4 == (options3[0]):
      num1 = input("Enter measurement of one diagonal: ")
      num2 = input ("Enter measurement of other diagonal: ")
      result = ((float(num1)*float(num2))/2)
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif answer4 == (options3[1]):
      num1 = input ("Enter measurement of base: ")
      num2 = input ("Enter measurement of perpendicular height: ")
      result = (float(num1) * float(num2))
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
    if answer3 == (options2[7]):
     num1 = input("Enter measurement of one diagonal: ")
     num2 = input ("Enter measurement of other diagonal: ")
     result = ((float(num1)*float(num2))/2)
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    if answer3 == (options2[8]):
      print ("Only regular polygons")
      print ("Using?")
      print ("->(a):apothem\n->(b):trinagle")
      opt = ["a","b"]
      rans = input ("Enter your answer(from the choices provided): ")
      if rans == (opt[0]):
        num = input ("Enter number of sides of polygon: ")
        apo = input ("Enter measurement of apothem: ")
        side = input ("Enter measurement of one side of polygon: ")
        peri = (float(side) * float(num))
        result = ((float(peri) * float(apo))/float(2))
        print ("Answer= " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
      if rans == (opt[1]):
       print ("Choose method of calculating area of triangle within polygon")
       print("->(a):All three sides\n->(b):Base and height\n->(c):Two sides and included angle")
       options3 = ["a","b","c"]
       answer4 = input ("Enter your answer(from the choices provided): ")
       if answer4 == (options3[1]):
        num1 = input ("Enter measurement of base: ")
        num2 = input ("Enter measurement of height: ")
        num3 = input ("Enter number of sides of polygon: ")
        result = ((0.5*float(num1)*float(num2)) * float(num3))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
       elif answer4 == (options3[2]):
        num1 = input ("Enter measurement of one side: ")
        num2 = input ("Enter measurement of other side: ")
        num3 = input ("Enter value of included angle in degrees: ")
        num4 = input ("Enter number of sides of polygon: ")
        result = ((0.5 * (float(num1) * float(num2)) * (math.sin((math.radians (float(num3)))))) * float(num4))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
       elif answer4 == (options3[0]):
        num1 = input ("Enter length of first side: ")
        num2 = input ("Enter length of second side: ")
        num3 = input ("Enter length of third side: ")
        num4 = input("Enter number of sides of polygon: ")
        queen = ((float(num1) + float(num2) + float(num3)))/2
        result = ((math.sqrt(float(queen) * (float(queen) - float(num1)) * (float(queen) - float(num2)) * (float(queen) - float(num3)))) * float(num4)) 
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue        
  if answer2 == (options[1]):
   print ("of a?")
   print ("->(a):sphere\n->(b):cube\n->(c):cuboid\n->(d):cylinder\n->(e):pyramid\n->(f):cone")
   options2 = ["a","b","c","d","e","f"]
   answer3 = input ("Enter your answer(from the choices provided): ")
   if answer3 == (options2[0]):
    num1 = input ("Enter radius: ")
    result = (4/3 * math.pi * float(num1) * float(num1) * float(num1))
    print ( "Your answer is = " + str(result))
    print()
    print ("Do you want to go to menu?")
    ans = input ("Enter your answer[y/n]: ")
    if ans == ("n"):
     x += 1
     print ("The program will close in ten seconds, Goodbye " + name)
     print ()
     print ("A       u","   R       e","v       o","i       r    Thank you" )
     print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
     print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
     print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
     print ("    G.  ","        B ","       Y ","       E                 very much")
     print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
     print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
     print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
     time.sleep(10)
    else:
     continue
   if answer3 == (options2[1]):
    print ("Using? ")
    print ("->(a):crossectional area\n->(b):all dimensions")
    options3 = ["a","b"]
    answer4 = input ("Enter your answer(from the choices provided): ")
    if answer4 == (options3[0]): 
     num1 = input ("Enter crossectional area: ")
     num2 = input ("Enter measurement of side: ")
     result = (float(num1) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    elif answer4 == (options3[1]):
     num1 = input ("Enter measurement of side: ")
     result = (float(num1) * float(num1) * float(num1))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
   if answer3 == (options2[2]):
    print ("Using? ")
    print ("->(a):crossectional area\n->(b):all dimensions")
    options3 = ["a","b"]
    answer4 = input ("Enter your answer(from the choices provided): ")
    if answer4 == (options3[0]): 
     num1 = input ("Enter crossectional area: ")
     num2 = input ("Enter measurement of side: ")
     result = (float(num1) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    elif answer4 == (options3[1]):
     num1 = input ("Enter length: ")
     num2 = input ("Enter width: ")
     num3 = input ("Enter height: ")
     result = (float(num1) * float(num2) * float(num3))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
   if answer3 == (options2[3]):
    print ("Using?")
    print ("->(a):crossectional area\n->(b):all dimensions")
    options3 = ["a","b"]
    answer4 = input ("Enter your answer(from the choices provided): ")
    if answer4 == (options3[0]):
     num1 = input ("Enter crossectional area: ")
     num2 = input ("Enter length: ")
     result = (float(num1) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    elif answer4 == (options3[1]):
     num1 = input ("Degrees of circle: ")
     num2 = input ("Radius of circle: ")
     num3 = input ("Enter length of cylinder: ")
     result = (float(num1)/360*math.pi*float(num2)*float(num2) * float(num3))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
   if answer3 == (options2[4]):
    print ("->(a):square based\n->(b):rectangular based\n->(c):triangular based")
    options3 =["a","b","c"]
    answer4 = input ("Enter your answer(from the choices provided): ")
    if answer4 == (options3[0]):
     num1 = input ("Enter measurement of square base side: ")
     num2 = input ("Enter height of pyramid: ") 
     result = (1/3 * (float(num1) * float(num1)) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    elif answer4 == (options3[1]):
     num1 = input ("Enter length of rectangle: ")
     num2 = input ("Enter width of rectangle: ")
     num3 = input ("Enter height of pyramid: ")
     result = (1/3 * (float(num1) * float(num2)) * float(num3))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    elif answer4 == (options3[2]):
     num1 = input ("Enter measurement of triangle's base: ")
     num2 = input ("Enter measurement of triangle's height: ")
     num3 = input ("Enter measuremnt of pyramid's height: ")
     result = (1/3 * (0.5 * float(num1) * float(num2)) * float(num3))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
   if answer3 == (options2[5]):
    print ("Using?")
    print ("->(a):crossectional area\n->(b):all dimensions")
    options3 = ["a","b"]
    answer4 = input ("Enter your answer(from the choice provided): ")
    if answer4 == (options3[0]):
     num1 = input ("Enter crossectional area of circle: ")
     num2 = input ("Enter height of cone : ")
     result = (1/3 * float(num1) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    elif answer4 == (options3[1]):
     num1 = input ("Enter radius of circle: ")
     num2 = input ("Enter height of cone: ")
     result = (1/3 * (math.pi * float(num1) * float(num1)) * float(num2))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
  if answer2 == (options[2]):
    print ("Of a?")
    print("->(a):cube\n->(b):cuboid\n->(c):cylinder\n->(d):wedge\n->(e):pyramid\n->(f):cone\n->(g):prisms\n->(h):sphere")
    print ("Only closed solids")
    gerri = ["a","b","c","d","e","f","g","h"]
    jan = input ("Enter your answer(from the choices provided): ")
    if jan == (gerri[0]):
     num1 = input ("Enter measuremnt of cube's side : ")
     result = ((float(num1) * float(num1)) * float(6))
     print ("Your answer is = " + str(result))     
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)      
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
    if jan == (gerri[1]):
      num1 = input ("Enter measurement of length: ")
      num2 = input ("Enter measurement of width: ")
      num3 = input ("Enter measurement of height: ")
      result = (((float(num1) * float(num3)) + (float(num2) * float(num3)) + (float(num1) * float(num2))) * float(2))
      print ("Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)      
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
    if jan == (gerri[2]):
     num1 = input ("Enter degrees of cylinder's circle: ")
     num2 = input ("Enter radius of cylinder's circle: ")  
     num3 = input ("Enter length of cylinder: ") 
     dia = (float(num2) * float(2))
     if num1 == ("360"):
      result = ((float(math.pi) * float(dia) * float(num3)) + (((float(math.pi) * float(num2) * float(num2))) * float(2)))
      print ("Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)      
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
     elif num1 != ("360"):
      result = (((float(num1)/360 * float(math.pi) * float(num2) * float(num2)) * float(2)) + ((float(num1)/360 * float(math.pi) * float(dia) + float(dia)) * float(num3)))
      print ("Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)      
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)   
    if jan == (gerri[3]):
     print("Get area of triangle using?")
     print("->(a):all three sides\n->(b):base and height\n->(c):two sides and included angle")
     options3 = ["a","b","c"]
     hawi = input ("Enter your answer(from the choices provided): ")
     if hawi == (options3[1]):
      num1 = input("Enter measuremnt of triangle's base: ")
      num2 = input("Enter measurment of triangle's height: ")
      num3 = input("Enter measurement of triangle's hypotenuse: ")
      num4 = input("Enter measurement of wedge's entire length: ")
      result = ((float(0.5) * float(num1) * float(num2)) * 2) + ((float(num1) + float(num2) + float(num3)) * float(num4))
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif hawi == (options3[0]):
      num1 = input ("Enter length of first side: ")
      num2 = input ("Enter length of second side: ")
      num3 = input ("Enter length of third side: ")
      num4 = input ("Enter measurement of wedge's entire length: ")
      queen = ((float(num1) + float(num2) + float(num3)))/2
      result = (((math.sqrt(float(queen) * (float(queen) - float(num1)) * (float(queen) - float(num2)) * (float(queen) - float(num3)))) * float(2))  + ((float(num1) + float(num2) + float(num3)) * float(num4)))
      print ("Your answer is = " + str(result)) 
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif hawi == (options3[2]): 
      num1 = input ("Enter measurement of one side: ")
      num2 = input ("Enter measurement of other side: ")
      num3 = input ("Enter value of included angle in degrees: ")
      num4 = input ("Enter measurement of third side: ")
      num5 = input ("Enter measurement of wedge's entire length: ")
      result = (((0.5 * (float(num1) * float(num2)) * (math.sin((math.radians (float(num3)))))) * float(2)) + ((float(num1) + float(num2) + float(num4)) * float(num5)))
      print("Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue 
    if jan == (gerri[4]):
     print("choose base of pyramid you want to calculate")
     print("(a):square based\n(b):rectangular based")
     opt = ["a","b"]
     ans = input("Enter your answer: ")
     if ans == (opt[0]):
      num1 = input("Enter measurement of square's side: ")
      skware = (float(num1) * float(num1))
      print ("choose method of calculating area of triangles")
      print ("using:")
      print("(a):All three sides\n(b):Base and height\n(c):Two sides and included angle")
      opt1 =  ["a","b","c"]   
      ans2 = input("Enter your answer(from the choices provided): ")
      if ans2 == (opt1[0]):
       tom = input("Enter length of first side: ")   
       tom1 = input("Enter length of second side: ")
       tom2 = input("Enter length of third side: ")
       queen = ((float(tom) + float(tom1) + float(tom2)))/2
       asult = ((math.sqrt(float(queen) * (float(queen) - float(tom)) * (float(queen) - float(tom1)) * (float(queen) - float(tom2)))) * float(4))
       result = (float(asult) + float(skware))
       print ("Your answer is = " + str(result))
       print()
       print ("Do you want to go to menu?")
       ans = input ("Enter your answer[y/n]: ")
       if ans == ("n"):
        x += 1
        print ("The program will close in ten seconds, Goodbye " + name)
        print ()
        print ("A       u","   R       e","v       o","i       r    Thank you" )
        print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
        print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
        print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
        print ("    G.  ","        B ","       Y ","       E                 very much")
        print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
        print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
        print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
        time.sleep(10)
       else:
        continue
      if ans2 == (opt1[1]):
       tom = input("Enter measurement of triangle's base: ") 
       tom1 = input("Enter measurement of triangle's height: ")
       bsult = ((0.5*float(tom) * float(tom1)) * float(4))
       result = (float(skware) + float(bsult))
       print ("Your answer is = " + str(result))
       print()
       print ("Do you want to go to menu?")
       ans = input ("Enter your answer[y/n]: ")
       if ans == ("n"):
        x += 1
        print ("The program will close in ten seconds, Goodbye " + name)
        print ()
        print ("A       u","   R       e","v       o","i       r    Thank you" )
        print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
        print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
        print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
        print ("    G.  ","        B ","       Y ","       E                 very much")
        print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
        print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
        print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
        time.sleep(10)
       else:
        continue
      if ans2 == (opt1[2]):
       tom = input ("Enter measurement of one side: ")
       tom1 = input ("Enter measurement of other side: ") 
       tom2 = input ("Enter value of included angle in degrees: ")  
       csult = ((0.5 * (float(tom) * float(tom1)) * (math.sin((math.radians (float(tom2)))))) * float(4))
       result = (float(csult) + float(skware))
       print ("Your answer is = " + str(result))
       print()
       print ("Do you want to go to menu?")
       ans = input ("Enter your answer[y/n]: ")
       if ans == ("n"):
        x += 1
        print ("The program will close in ten seconds, Goodbye " + name)
        print ()
        print ("A       u","   R       e","v       o","i       r    Thank you" )
        print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
        print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
        print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
        print ("    G.  ","        B ","       Y ","       E                 very much")
        print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
        print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
        print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
        time.sleep(10)
       else:
        continue
     if ans == (opt[1]):
      num1 = input("Enter length of rectangle: ")
      num2 = input("Enter width of rectangle: ") 
      rec = (float(num1) * float(num2))
      print ("Choose method of calculating area of first pair of triangles")
      print ("using:")
      print("(a):All three sides\n(b):Base and height\n(c):Two sides and included angle")    
      opt1 =  ["a","b","c"]  
      ans2 = input ("Enter your answer(from the choices provided): ")
      if ans2 == (opt1[0]):
       tom = input("Enter length of first side: ")   
       tom1 = input("Enter length of second side: ")
       tom2 = input("Enter length of third side: ")
       queen = ((float(tom) + float(tom1) + float(tom2)))/2
       asult = ((math.sqrt(float(queen) * (float(queen) - float(tom)) * (float(queen) - float(tom1)) * (float(queen) - float(tom2)))) * float(2))
       print ("choose method of calculating area of second pair of triangles")
       print ("Using:")
       print("(a):All three sides\n(b):Base and height\n(c):Two sides and included angle")    
       opt1 =  ["a","b","c"]
       ans3 = input("Enter your answer(from the choices provided): ")
       if ans3 == (opt1[0]):
        tom = input("Enter length of first side: ")   
        tom1 = input("Enter length of second side: ")
        tom2 = input("Enter length of third side: ")
        queen = ((float(tom) + float(tom1) + float(tom2)))/2
        asult = ((math.sqrt(float(queen) * (float(queen) - float(tom)) * (float(queen) - float(tom1)) * (float(queen) - float(tom2)))) * float(2))   
        result = (float(asult) + float(rec) + float(asult))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
       if ans3 == (opt1[1]):
        tom = input("Enter measurement of triangle's base: ") 
        tom1 = input("Enter measurement of triangle's height: ")
        bsult = ((0.5*float(tom) * float(tom1)) * float(2))
        result = (float(rec) + float(bsult) + float(asult))
        print ("Your answer is = " + str(result)) 
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue 
       if ans3 == (opt1[2]):
        tom = input ("Enter measurement of one side: ")
        tom1 = input ("Enter measurement of other side: ") 
        tom2 = input ("Enter value of included angle in degrees: ")  
        csult = ((0.5 * (float(tom) * float(tom1)) * (math.sin((math.radians (float(tom2)))))) * float(2))
        result = (float(csult) + float(rec) + float(asult))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
      if ans2 == (opt[1]):
       tom = input("Enter measurement of triangle's base: ")
       tom1 = input("Enter measurement of triangle's height: ")            
       bsult = ((0.5*float(tom) * float(tom1)) * float(2))
       print ("choose method of calculating area of second pair of triangles")
       print ("Using:")
       print("(a):All three sides\n(b):Base and height\n(c):Two sides and included angle")    
       opt1 =  ["a","b","c"]
       ans3 = input("Enter your answer(from the choices provided): ")
       if ans3 == (opt1[0]):
        tom = input("Enter length of first side: ")   
        tom1 = input("Enter length of second side: ")
        tom2 = input("Enter length of third side: ")
        queen = ((float(tom) + float(tom1) + float(tom2)))/2
        asult = ((math.sqrt(float(queen) * (float(queen) - float(tom)) * (float(queen) - float(tom1)) * (float(queen) - float(tom2)))) * float(2))   
        result = (float(asult) + float(rec) + float(bsult))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
       if ans3 == (opt1[1]):
        tom = input("Enter measurement of triangle's base: ") 
        tom1 = input("Enter measurement of triangle's height: ")
        bsult = ((0.5*float(tom) * float(tom1)) * float(2))
        result = (float(rec) + float(bsult) + float(bsult))
        print ("Your answer is = " + str(result)) 
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue 
       if ans3 == (opt1[2]):
        tom = input ("Enter measurement of one side: ")
        tom1 = input ("Enter measurement of other side: ") 
        tom2 = input ("Enter value of included angle in degrees: ")  
        csult = ((0.5 * (float(tom) * float(tom1)) * (math.sin((math.radians (float(tom2)))))) * float(2))
        result = (float(csult) + float(rec) + float(bsult))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
      if ans2 == (opt1[2]):
       tom = input ("Enter measurement of one side: ")
       tom1 = input ("Enter measurement of other side: ") 
       tom2 = input ("Enter value of included angle in degrees: ")  
       csult = ((0.5 * (float(tom) * float(tom1)) * (math.sin((math.radians (float(tom2)))))) * float(2))
       print ("choose method of calculating area of second pair of triangles")
       print ("Using:")
       print("(a):All three sides\n(b):Base and height\n(c):Two sides and included angle")    
       opt1 =  ["a","b","c"]
       ans3 = input("Enter your answer(from the choices provided): ")
       if ans3 == (opt1[0]):
        tom = input("Enter length of first side: ")   
        tom1 = input("Enter length of second side: ")
        tom2 = input("Enter length of third side: ")
        queen = ((float(tom) + float(tom1) + float(tom2)))/2
        asult = ((math.sqrt(float(queen) * (float(queen) - float(tom)) * (float(queen) - float(tom1)) * (float(queen) - float(tom2)))) * float(2))   
        result = (float(asult) + float(rec) + float(csult))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue
       if ans3 == (opt1[1]):
        tom = input("Enter measurement of triangle's base: ") 
        tom1 = input("Enter measurement of triangle's height: ")
        bsult = ((0.5*float(tom) * float(tom1)) * float(2))
        result = (float(rec) + float(csult) + float(bsult))
        print ("Your answer is = " + str(result))
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue  
       if ans3 == (opt1[2]):
        tom = input ("Enter measurement of one side: ")
        tom1 = input ("Enter measurement of other side: ") 
        tom2 = input ("Enter value of included angle in degrees: ")  
        csult = ((0.5 * (float(tom) * float(tom1)) * (math.sin((math.radians (float(tom2)))))) * float(2))
        result = (float(csult) + float(rec) + float(csult))
        print ("Your answer is = " + str(result)) 
        print()
        print ("Do you want to go to menu?")
        ans = input ("Enter your answer[y/n]: ")
        if ans == ("n"):
         x += 1
         print ("The program will close in ten seconds, Goodbye " + name)
         print ()
         print ("A       u","   R       e","v       o","i       r    Thank you" )
         print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
         print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
         print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
         print ("    G.  ","        B ","       Y ","       E                 very much")
         print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
         print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
         print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
         time.sleep(10)
        else:
         continue    
    if jan == (gerri[5]):
     num1 = input ("Enter measurement cone's slant height: ")
     num2 = input ("Enter radius of cone's circle: ")
     result = ((float(math.pi) * float(num2) * float(num2)) + (float(math.pi) * float(num2) * float(num1)))
     print ( "Your answer is = " + str(result))
     print()
     print ("Do you want to go to menu?")
     ans = input ("Enter your answer[y/n]: ")
     if ans == ("n"):
      x += 1
      print ("The program will close in ten seconds, Goodbye " + name)
      print ()
      print ("A       u","   R       e","v       o","i       r    Thank you" )
      print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
      print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
      print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
      print ("    G.  ","        B ","       Y ","       E                 very much")
      print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
      print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
      print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
      time.sleep(10)
     else:
      continue
    if jan == (gerri[6]):
     print("Using:")
     print("(a):Apothem\n(b):Triangles")
     finale = ["a","b"] 
     narok = input("Enter your answer(from the choices provided): ")
     if narok == (finale[0]):
      num = input ("Enter number of sides of polygon: ")
      apo = input ("Enter measurement of apothem: ")
      side = input ("Enter measurement of one side of polygon: ")
      num1 = input("Enter length of the entire prism: ")
      peri = (float(side) * float(num))
      result = (((float(peri) * float(apo))) + (float(num) * float(side) * float(num1)))
      print ( "Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif narok == (finale[1]):
      print ("Choose method of calculating area of triangle within polygon")
      print("->(a):All three sides\n->(b):Base and height\n->(c):Two sides and included angle")
      options3 = ["a","b","c"]
      answer4 = input ("Enter your answer(from the choices provided): ")
      if answer4 == (options3[1]):
       num1 = input ("Enter measurement of base: ")
       num2 = input ("Enter measurement of height: ")
       num3 = input ("Enter number of sides of polygon: ")
       num4 = input ("Enter length of prism: ")
       num5 = input ("Enter measurement of one side of the prism's face: ")
       result = ((((0.5*float(num1)*float(num2)) * float(num3)) * float(2)) + ((float(num5) * float(num3)) * float(num4)))
       print ("Your answer is = " + str(result))
       print()
       print ("Do you want to go to menu?")
       ans = input ("Enter your answer[y/n]: ")
       if ans == ("n"):
        x += 1
        print ("The program will close in ten seconds, Goodbye " + name)
        print ()
        print ("A       u","   R       e","v       o","i       r    Thank you" )
        print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
        print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
        print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
        print ("    G.  ","        B ","       Y ","       E                 very much")
        print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
        print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
        print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
        time.sleep(10)
       else:
        continue
      elif answer4 == (options3[0]):
       num1 = input ("Enter length of first side: ")
       num2 = input ("Enter length of second side: ")
       num3 = input ("Enter length of third side: ")
       num4 = input("Enter number of sides of polygon: ")
       num5 = input ("Enter measurement of one side of the prism's face: ")
       num6 = input ("Enter measurement of prism's entire length: ")
       queen = ((float(num1) + float(num2) + float(num3)))/2
       result = ((((math.sqrt(float(queen) * (float(queen) - float(num1)) * (float(queen) - float(num2)) * (float(queen) - float(num3)))) * float(num4)) * float(2)) + (float(num4) * float(num5)) * float(num6)) 
       print ("Your answer is = " + str(result)) 
       print()
       print ("Do you want to go to menu?")
       ans = input ("Enter your answer[y/n]: ")
       if ans == ("n"):
        x += 1
        print ("The program will close in ten seconds, Goodbye " + name)
        print ()
        print ("A       u","   R       e","v       o","i       r    Thank you" )
        print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
        print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
        print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
        print ("    G.  ","        B ","       Y ","       E                 very much")
        print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
        print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
        print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
        time.sleep(10)
       else:
        continue
      elif answer4 == (options3[2]):
       num1 = input ("Enter measurement of one side: ")
       num2 = input ("Enter measurement of other side: ")
       num3 = input ("Enter value of included angle in degrees: ")
       num4 = input ("Enter number of sides of polygon: ")
       num5 = input ("Enter measurement of one side of prism's face: ")
       num6 = input("Enter measurement of prism's entire length: ")
       result = ((((0.5 * (float(num1) * float(num2)) * (math.sin((math.radians (float(num3)))))) * float(num4)) * float(2)) + ((float(num4) * float(num5)) * float(num6)))
       print ("Your answer is = " + str(result)) 
       print()
       print ("Do you want to go to menu?")
       ans = input ("Enter your answer[y/n]: ")
       if ans == ("n"):
        x += 1
        print ("The program will close in ten seconds, Goodbye " + name)
        print ()
        print ("A       u","   R       e","v       o","i       r    Thank you" )
        print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
        print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
        print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
        print ("    G.  ","        B ","       Y ","       E                 very much")
        print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
        print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
        print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
        time.sleep(10)
       else:
        continue
    if jan == (gerri[7]):
     print ("->(a):half\n->(b):full") 
     steph = ["a","b"]
     leon = input("Enter your answer(from the choices provided): ")
     if leon == (steph[0]):
      num1 = input ("Enter radius of sphere: ")
      result = (float(3) * float(math.pi) * float(num1) * float(num1))
      print ("Your answer is = " + str(result))
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
     elif leon == (steph[1]):
      num1 = input ("Enter radius of sphere: ")
      result = (float(4) * (math.pi) * float(num1) * float(num1))
      print ("Your answer is = " + str(result)) 
      print()
      print ("Do you want to go to menu?")
      ans = input ("Enter your answer[y/n]: ")
      if ans == ("n"):
       x += 1
       print ("The program will close in ten seconds, Goodbye " + name)
       print ()
       print ("A       u","   R       e","v       o","i       r    Thank you" )
       print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
       print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
       print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
       print ("    G.  ","        B ","       Y ","       E                 very much")
       print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
       print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
       print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
       time.sleep(10)
      else:
       continue
elif answer == ("n"):
 print ("Why not?")
 answer2 = input ("Tell us why: ")
 print ("Thank you for your feedback " + name + " We appreciate you opening our application")
 print ("The program will close in ten seconds, Goodbye " + name)
 print ()
 print ("A       u","   R       e","v       o","i       r    Thank you" )
 print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
 print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
 print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
 print ("    G.  ","        B ","       Y ","       E                 very much")
 print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
 print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
 print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
 time.sleep(10)
else:
 print ("ERROR: input unrecognised!")
 print ("Restart program then")
 print ("Enter y or n in small letters")
 print ("The program will close in ten seconds, Goodbye " + name)
 print ()
 print ("A       u","   R       e","v       o","i       r    Thank you" )
 print (" \('=')/ ","    \('+')/ "," \('-')/ "," \('.')/       for your " )
 print ("  \   / ","      \   / ","   \   / ","   \   /          time here" )
 print ("   \ / ","        \ / ","     \ / ","     \ /              and you are")
 print ("    G.  ","        B ","       Y ","       E                 very much")
 print ("   / \ ","        / \ ","     / \ ","     / \                   welcomed ")
 print ("  /   \ ","      /   \ ","   /   \ ","   /   \                       back :)")
 print ("  ''''' ","      ||||| ","   ^^^^^ ","   !!!!!                       ==> " + name + " <==")
 time.sleep(10)
 

  

 




  


 
 

 

 
 

 
 
 

 


 
 