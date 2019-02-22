import preprocessor as p
import re

str_to_clean = 'Preprocessor is #awesome 👍 https://github.com/s/preprocessor';
clean_str = p.tokenize(str_to_clean);

#print([word for word in clean_str.split() if word.startswith('$') and word.endswith('$')])

new_str = [];
for word in clean_str.split():
	if word.startswith('$') and word.endswith('$'):
		word = '<' + word[1:len(word)-1] + '>';
	new_str.append(word);
new_str = " ".join(new_str);

#m = re.sub(r'/\$(URL|EMOJI)\$', r'<\1>', clean_str);
m = re.findall(r'\b\$\w*?\$\b', clean_str.rstrip());
print(m);

#print(clean_str);
#print(new_str);