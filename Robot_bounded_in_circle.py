def solve(inst):

	# L = True = -1
	# LL = True = -2
	# LLL = True = -3
	# LLLLR = True = -4 + 1 = -3
	# LLLL = False = -4

	# CHECKS:
	# -> The count of L and R must be unbalanced (dir must change)
	# -> Robot should be able to return in <=4 steps

	dir = 0
	x = 0
	y = 0

	print(f"Start pos ({x},{y})")

	for j in range(4):
		dir_init = dir
		# single instruction cycle
		for i, step in enumerate(inst):
			# dir <=3
			if step == "L":
				dir = (dir + 1) % 4
				print(f"Turned left, dir:{dir}")
			elif step == "R":
				dir = (dir - 1) % 4
				print(f"Turned right, dir:{dir}")
			elif step == "G":
				# dir unchanged
				if dir == 0:
					y += 1
				elif dir == 1:
					x -= 1
				elif dir == 2:
					y -= 1
				elif dir == 3:
					x += 1
				print(f"Moved in dir:{dir}, ({x},{y})")

			# check for completion
			if x == 0 and y == 0:
				print("RETURNED TO ORIGIN")
				return True

		print("> Cycle end")
		# unchanging direction
		if dir_init == dir:
			print("DOES NOT CHANGE DIR")
			return False

	return False


# take input
# -> force upper
# -> remove whitespace
#inp = input("instructions:").upper().strip()
inp = "GLLL"
print(solve(inp))
