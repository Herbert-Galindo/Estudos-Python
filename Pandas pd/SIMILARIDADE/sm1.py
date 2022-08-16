from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

text_1 = 'pso_visd_dh00072_bx1_bx2_0.00_6.96m_d.jpg'
text_2 = 'pso_visd_dh00072_bx1_bx2_6.96m_d.jpg'
#N-Gramas: uni, bidi ,trid
n = 1
#Instancia do contador de N-gramas
counts = CountVectorizer(analyzer='word', ngram_range=(n,n))
#matriz N-gramas para 2 textos
n_gramas = counts.fit_transform([text_1, text_2])
#dicionario
vocab2int = counts.fit([text_1, text_2]).vocabulary_

n_gramas_array = n_gramas.toarray()
#print('Vetor de N-Gramas: \n\n', n_gramas_array)
#print()
#print('Dicionario de N-Gramas(unigrama): \n\n', vocab2int)

n_gramas.toarray()

intersection_list = np.amin(n_gramas.toarray(), axis = 0)
print(intersection_list)

intersection_count = np.sum(intersection_list)
print(intersection_count)

index_A = 0
A_count = np.sum(n_gramas.toarray()[index_A])
print(A_count)