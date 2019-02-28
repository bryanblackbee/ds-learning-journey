import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def token_normalise_token(token):
	"""
		Given a token, return the basic form of the word.
		Return empty string if word is invalid
	"""

	if re.fullmatch('\d+', token) is not None:
		return "NUMERIC"
	elif token in stopwords.words('english'):
		return ""
	elif len(token) < 2:
		return ""

	wnl = WordNetLemmatizer()
	return wnl.lemmatize(token)

def token_clean_token(token):
	"""
		Given a token, remove special characters (before, after, surrounding).
	"""
	cleaned_token = token

	#Remove hashtag before string
	if re.search('#[a-zA-Z0-9]+', cleaned_token) is not None:
		cleaned_token = cleaned_token[1:]

	#Remove double quotes, parenthesis, square brackets
	if re.search('\"[-.,\$a-zA-Z0-9]+\"', cleaned_token) is not None:
		cleaned_token = cleaned_token[1:-1]
	elif re.search('\([-.,$a-zA-Z0-9]+\)', cleaned_token) is not None:
		cleaned_token = cleaned_token[1:-1]
	elif re.search('\[[-.,$a-zA-Z0-9]+\]', cleaned_token) is not None:
		cleaned_token = cleaned_token[1:-1]        
	elif re.search('[-.,$a-zA-Z0-9]+\)', cleaned_token) is not None:
		cleaned_token = cleaned_token[:-1]
	elif re.search('\([-.,$a-zA-Z0-9]+', cleaned_token) is not None:
		cleaned_token = cleaned_token[1:] 

	#Remove beginning and ending special characters
	while re.search('[-.,$a-zA-Z0-9]+\W$', cleaned_token) is not None:
		cleaned_token = cleaned_token[:-1]
	while re.search('^â€˜[a-zA-Z0-9]+', cleaned_token) is not None:
		cleaned_token = cleaned_token[1:]        
	return cleaned_token

def clean_token_workflow(x):
    x2 = token_clean_token(x) 
    x3 = token_normalise_token(x2)    
    return x3

def clean_document_workflow(d):
    d_list = d.split()
    d0 = [t.lower() for t in d_list]
    d1 = [clean_token_workflow(t) for t in d0]
    d2 = [t2 for t2 in d1 if len(t2) > 0]
    return ' '.join(d2)