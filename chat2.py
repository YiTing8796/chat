

lines = []
def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f :
		for line in f:
			lines.append(line.strip())
	return lines
			

def chat_ana(lines):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_img_count = 0
	viki_img_count = 0
	for line in lines:
		s = line.split(' ')
		if s[1] == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_img_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif s[1] == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_img_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)	
	print('Allen 說了', allen_word_count, '個字')
	print('Viki 說了', viki_word_count, '個字')
	print('Allen 發了', allen_img_count, '張圖')
	print('Viki 發了', viki_img_count, '張圖')
	print('Allen 發了', allen_sticker_count, '張貼圖')
	print('Viki 發了', viki_sticker_count, '張貼圖')


def write_file(filename, lines):
	with open(filename, 'w', encoding= 'utf-8-sig') as f:
		for line in lines:
			line.w(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = chat_ana(lines)
	# write_file('output.txt', lines)


main()