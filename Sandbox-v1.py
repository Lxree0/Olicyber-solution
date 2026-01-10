flag{LOWER_upper_3scap3_Fr0m_j@il}

Per risolvere la sfida, è necessario utilizzare l'introspezione di Python per recuperare moduli o funzioni rimosse senza digitare le parole bloccate.

1. Navigazione delle Sottoclassi
Poiché l'ambiente locals è limitato, risaliamo alla gerarchia degli oggetti partendo da un tipo base (come una tupla ()) per trovare classi che importano internamente moduli pericolosi.

Python

# Recupera tutte le classi caricate in memoria
().__class__.__base__.__subclasses__()
2. Individuazione della Classe Target
Cercano classi come os._wrap_close o warnings.catch_warnings. In questa specifica istanza, l'indice di os._wrap_close è risultato essere 154.

3. Costruzione del Payload
Per aggirare la blacklist, utilizziamo la concatenazione di stringhe e l'accesso tramite dizionario:

Problema: import e os sono vietati.

Soluzione: Accedere a __globals__ di una classe esistente che ha già importato os.

Problema: system e flag sono vietati.

Soluzione: Usare 'sy' + 'stem' e wildcard come f*.

Soluzione Finale (Exploit)
Eseguire il seguente comando nella console per leggere la flag:

Python

# Esegue 'cat flag' usando popen dall'indice 154 (os._wrap_close)
print(().__class__.__base__.__subclasses__()[154].__init__.__globals__['po' + 'pen']('ca' + 't f*
