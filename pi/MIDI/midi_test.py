# play an embedded midi music file on your computer's sound card
# experiments with module pygame from: http://www.pygame.org/
# tested with Python25 and PyGame171      vegaseat      04sep2007
"""
# use this short program to create the base64 encoded midi music string
# (base64 encoding simply produces a readable string from binary data)
# then copy and paste the result into your pygame program ...
import base64
mid_file = "FishPolka.mid"
print "mid64='''\\\n" + base64.encodestring(open(mid_file, 'rb').read()) + "'''"
"""
import pygame
import base64
def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
mid64='''\
TVRoZAAAAAYAAQAFAGBNVHJrAAAAEwD/WAQEAmAIAP9RAwi4JAD/LwBNVHJrAAAJmQD/AxhTZXF1
ZW5jZWQgYnkgUC5KLiBCYXJuZXMAsAAAAMAaAP9YBAQCYAgA/1EDCLgkAJBMQBCATEAIkExAEIBM
QCCQTEAQgExAIJBIQBCASEAIkExAEIBMQCCQT0AQgE9AgTCQSEAQgEhAOJBDQBCAQ0A4kEBAEIBA
QDiQRUAQgEVAIJBHQBCAR0AgkEZAEIBGQAiQRUAQgEVAIJBDQBCAQ0AQkExAEIBMQBCQT0AQgE9A
EJBRQBCAUUAgkE1AEIBNQAiQT0AQgE9AIJBMQBCATEAgkEhAEIBIQAiQSkAQgEpACJBHQBCAR0A4
kEhAEIBIQDiQQ0AQgENAOJBAQBCAQEA4kEVAEIBFQCCQR0AQgEdAIJBGQBCARkAIkEVAEIBFQCCQ
Q0AQgENAEJBMQBCATEAQkE9AEIBPQBCQUUAQgFFAIJBNQBCATUAIkE9AEIBPQCCQTEAQgExAIJBI
QBCASEAIkEpAEIBKQAiQR0AQgEdAaJBPQBCAT0AIkE5AEIBOQAiQTUAQgE1ACJBLQBCAS0AgkExA
EIBMQCCQREAQgERACJBFQBCARUAIkEhAEIBIQCCQRUAQgEVACJBIQBCASEAIkEpAEIBKQDiQT0AQ
gE9ACJBOQBCATkAIkE1AEIBNQAiQS0AQgEtAIJBMQBCATEAgkFRAEIBUQCCQVEAQgFRACJBUQBCA
VECBAJBPQBCAT0AIkE5AEIBOQAiQTUAQgE1ACJBLQBCAS0AgkExAEIBMQCCQREAQgERACJBFQBCA
RUAIkEhAEIBIQCCQRUAQgEVACJBIQBCASEAIkEpAEIBKQDiQS0AQgEtAOJBKQBCASkA4kEhAEIBI
QIFgkE9AEIBPQAiQTkAQgE5ACJBNQBCATUAIkEtAEIBLQCCQTEAQgExAIJBEQBCAREAIkEVAEIBF
QAiQSEAQgEhAIJBFQBCARUAIkEhAEIBIQAiQSkAQgEpAOJBPQBCAT0AIkE5AEIBOQAiQTUAQgE1A
CJBLQBCAS0AgkExAEIBMQCCQVEAQgFRAIJBUQBCAVEAIkFRAEIBUQIEAkE9AEIBPQAiQTkAQgE5A
CJBNQBCATUAIkEtAEIBLQCCQTEAQgExAIJBEQBCAREAIkEVAEIBFQAiQSEAQgEhAIJBFQBCARUAI
kEhAEIBIQAiQSkAQgEpAOJBLQBCAS0A4kEpAEIBKQDiQSEAQgEhAgTCQSEAQgEhACJBIQBCASEAg
kEhAEIBIQCCQSEAQgEhACJBKQBCASkAgkExAEIBMQAiQSEAQgEhAIJBFQBCARUAIkENAEIBDQFCQ
SEAQgEhACJBIQBCASEAgkEhAEIBIQCCQSEAQgEhACJBKQBCASkAIkExAEIBMQIFIkEhAEIBIQAiQ
SEAQgEhAIJBIQBCASEAgkEhAEIBIQAiQSkAQgEpAIJBMQBCATEAIkEhAEIBIQCCQRUAQgEVACJBD
QBCAQ0BQkExAEIBMQAiQTEAQgExAIJBMQBCATEAgkEhAEIBIQAiQTEAQgExAIJBPQBCAT0CBMJBI
QBCASEA4kENAEIBDQDiQQEAQgEBAOJBFQBCARUAgkEdAEIBHQCCQRkAQgEZACJBFQBCARUAgkENA
EIBDQBCQTEAQgExAEJBPQBCAT0AQkFFAEIBRQCCQTUAQgE1ACJBPQBCAT0AgkExAEIBMQCCQSEAQ
gEhACJBKQBCASkAIkEdAEIBHQDiQSEAQgEhAOJBDQBCAQ0A4kEBAEIBAQDiQRUAQgEVAIJBHQBCA
R0AgkEZAEIBGQAiQRUAQgEVAIJBDQBCAQ0AQkExAEIBMQBCQT0AQgE9AEJBRQBCAUUAgkE1AEIBN
QAiQT0AQgE9AIJBMQBCATEAgkEhAEIBIQAiQSkAQgEpACJBHQBCAR0A4kExAEIBMQAiQSEAQgEhA
IJBDQBCAQ0A4kERAEIBEQCCQRUAQgEVACJBNQBCATUAgkE1AEIBNQAiQRUAQgEVAUJBHQBCAR0AQ
kFFAEIBRQBCQUUAQgFFAEJBRQBCAUUAQkE9AEIBPQBCQTUAQgE1AEJBMQBCATEAIkEhAEIBIQCCQ
RUAQgEVACJBDQBCAQ0BQkExAEIBMQAiQSEAQgEhAIJBDQBCAQ0A4kERAEIBEQCCQRUAQgEVACJBN
QBCATUAgkE1AEIBNQAiQRUAQgEVAUJBHQBCAR0AIkE1AEIBNQCCQTUAQgE1ACJBNQBCATUAQkExA
EIBMQBCQSkAQgEpAEJBIQBCASECBMJBMQBCATEAIkEhAEIBIQCCQQ0AQgENAOJBEQBCAREAgkEVA
EIBFQAiQTUAQgE1AIJBNQBCATUAIkEVAEIBFQFCQR0AQgEdAEJBRQBCAUUAQkFFAEIBRQBCQUUAQ
gFFAEJBPQBCAT0AQkE1AEIBNQBCQTEAQgExACJBIQBCASEAgkEVAEIBFQAiQQ0AQgENAUJBMQBCA
TEAIkEhAEIBIQCCQQ0AQgENAOJBEQBCAREAgkEVAEIBFQAiQTUAQgE1AIJBNQBCATUAIkEVAEIBF
QFCQR0AQgEdACJBNQBCATUAgkE1AEIBNQAiQTUAQgE1AEJBMQBCATEAQkEpAEIBKQBCQSEAQgEhA
gTCQSEAQgEhACJBIQBCASEAgkEhAEIBIQCCQSEAQgEhACJBKQBCASkAgkExAEIBMQAiQSEAQgEhA
IJBFQBCARUAIkENAEIBDQFCQSEAQgEhACJBIQBCASEAgkEhAEIBIQCCQSEAQgEhACJBKQBCASkAI
kExAEIBMQIFIkEhAEIBIQAiQSEAQgEhAIJBIQBCASEAgkEhAEIBIQAiQSkAQgEpAIJBMQBCATEAI
kEhAEIBIQCCQRUAQgEVACJBDQBCAQ0BQkExAEIBMQAiQTEAQgExAIJBMQBCATEAgkEhAEIBIQAiQ
TEAQgExAIJBPQBCAT0CBMJBMQBCATEAIkEhAEIBIQCCQQ0AQgENAOJBEQBCAREAgkEVAEIBFQAiQ
TUAQgE1AIJBNQBCATUAIkEVAEIBFQFCQR0AQgEdAEJBRQBCAUUAQkFFAEIBRQBCQUUAQgFFAEJBP
QBCAT0AQkE1AEIBNQBCQTEAQgExACJBIQBCASEAgkEVAEIBFQAiQQ0AQgENAUJBMQBCATEAIkEhA
EIBIQCCQQ0AQgENAOJBEQBCAREAgkEVAEIBFQAiQTUAQgE1AIJBNQBCATUAIkEVAEIBFQFCQR0AQ
gEdACJBNQBCATUAgkE1AEIBNQAiQTUAQgE1AEJBMQBCATEAQkEpAEIBKQBCQSEAQgEhAAP8vAE1U
cmsAAAnpAP8DDUNvdW50ZXJtZWxvZHkAsQAAAMEaAP9YBAQCYAgA/1EDCLgkAJFCQBCBQkAIkUJA
EIFCQCCRQkAQgUJAIJFCQBCBQkAIkUJAEIFCQCCRR0AQgUdAUJFDQBCBQ0BQkUBAEIFAQDiRPEAQ
gTxAOJE3QBCBN0A4kTxAEIE8QCCRPkAQgT5AIJE9QBCBPUAIkTxAEIE8QCCRPEAQgTxAEJFDQBCB
Q0AQkUdAEIFHQBCRSEAQgUhAIJFFQBCBRUAIkUdAEIFHQCCRRUAQgUVAIJFAQBCBQEAIkUFAEIFB
QAiRPkAQgT5AOJFAQBCBQEA4kTxAEIE8QDiRN0AQgTdAOJE8QBCBPEAgkT5AEIE+QCCRPUAQgT1A
CJE8QBCBPEAgkTxAEIE8QBCRQ0AQgUNAEJFHQBCBR0AQkUhAEIFIQCCRRUAQgUVACJFHQBCBR0Ag
kUVAEIFFQCCRQEAQgUBACJFBQBCBQUAIkT5AEIE+QGiRTEAQgUxACJFLQBCBS0AIkUpAEIFKQAiR
R0AQgUdAIJFIQBCBSEAgkUBAEIFAQAiRQUAQgUFACJFDQBCBQ0AgkTxAEIE8QAiRQEAQgUBACJFB
QBCBQUA4kUxAEIFMQAiRS0AQgUtACJFKQBCBSkAIkUdAEIFHQCCRSEAQgUhAIJFNQBCBTUAgkU1A
EIFNQAiRTUAQgU1AgQCRTEAQgUxACJFLQBCBS0AIkUpAEIFKQAiRR0AQgUdAIJFIQBCBSEAgkUBA
EIFAQAiRQUAQgUFACJFDQBCBQ0AgkTxAEIE8QAiRQEAQgUBACJFBQBCBQUA4kURAEIFEQDiRQUAQ
gUFAOJFAQBCBQECBYJFMQBCBTEAIkUtAEIFLQAiRSkAQgUpACJFHQBCBR0AgkUhAEIFIQCCRQEAQ
gUBACJFBQBCBQUAIkUNAEIFDQCCRPEAQgTxACJFAQBCBQEAIkUFAEIFBQDiRTEAQgUxACJFLQBCB
S0AIkUpAEIFKQAiRR0AQgUdAIJFIQBCBSEAgkU1AEIFNQCCRTUAQgU1ACJFNQBCBTUCBAJFMQBCB
TEAIkUtAEIFLQAiRSkAQgUpACJFHQBCBR0AgkUhAEIFIQCCRQEAQgUBACJFBQBCBQUAIkUNAEIFD
QCCRPEAQgTxACJFAQBCBQEAIkUFAEIFBQDiRREAQgURAOJFBQBCBQUA4kUBAEIFAQIEwkURAEIFE
QAiRREAQgURAIJFEQBCBREAgkURAEIFEQAiRRkAQgUZAIJFDQBCBQ0AIkUBAEIFAQCCRQEAQgUBA
CJE8QBCBPEBQkURAEIFEQAiRREAQgURAIJFEQBCBREAgkURAEIFEQAiRRkAQgUZACJFDQBCBQ0CB
SJFEQBCBREAIkURAEIFEQCCRREAQgURAIJFEQBCBREAIkUZAEIFGQCCRQ0AQgUNACJFAQBCBQEAg
kUBAEIFAQAiRPEAQgTxAUJFCQBCBQkAIkUJAEIFCQCCRQkAQgUJAIJFCQBCBQkAIkUJAEIFCQCCR
R0AQgUdAUJFDQBCBQ0BQkUBAEIFAQDiRPEAQgTxAOJE3QBCBN0A4kTxAEIE8QCCRPkAQgT5AIJE9
QBCBPUAIkTxAEIE8QCCRPEAQgTxAEJFDQBCBQ0AQkUdAEIFHQBCRSEAQgUhAIJFFQBCBRUAIkUdA
EIFHQCCRRUAQgUVAIJFAQBCBQEAIkUFAEIFBQAiRPkAQgT5AOJFAQBCBQEA4kTxAEIE8QDiRN0AQ
gTdAOJE8QBCBPEAgkT5AEIE+QCCRPUAQgT1ACJE8QBCBPEAgkTxAEIE8QBCRQ0AQgUNAEJFHQBCB
R0AQkUhAEIFIQCCRRUAQgUVACJFHQBCBR0AgkUVAEIFFQCCRQEAQgUBACJFBQBCBQUAIkT5AEIE+
QDiRSEAQgUhACJFFQBCBRUAgkUBAEIFAQDiRQEAQgUBAIJFBQBCBQUAIkUhAEIFIQCCRSEAQgUhA
CJFBQBCBQUBQkUNAEIFDQBCRTUAQgU1AEJFNQBCBTUAQkU1AEIFNQBCRTEAQgUxAEJFKQBCBSkAQ
kUhAEIFIQAiRRUAQgUVAIJFBQBCBQUAIkUBAEIFAQFCRSEAQgUhACJFFQBCBRUAgkUBAEIFAQDiR
QEAQgUBAIJFBQBCBQUAIkUhAEIFIQCCRSEAQgUhACJFBQBCBQUBQkUNAEIFDQAiRSkAQgUpAIJFK
QBCBSkAIkUpAEIFKQBCRSEAQgUhAEJFHQBCBR0AQkUNAEIFDQAiRQEAQgUBAIJFAQBCBQEAIkTxA
EIE8QFCRSEAQgUhACJFFQBCBRUAgkUBAEIFAQDiRQEAQgUBAIJFBQBCBQUAIkUhAEIFIQCCRSEAQ
gUhACJFBQBCBQUBQkUNAEIFDQBCRTUAQgU1AEJFNQBCBTUAQkU1AEIFNQBCRTEAQgUxAEJFKQBCB
SkAQkUhAEIFIQAiRRUAQgUVAIJFBQBCBQUAIkUBAEIFAQFCRSEAQgUhACJFFQBCBRUAgkUBAEIFA
QDiRQEAQgUBAIJFBQBCBQUAIkUhAEIFIQCCRSEAQgUhACJFBQBCBQUBQkUNAEIFDQAiRSkAQgUpA
IJFKQBCBSkAIkUpAEIFKQBCRSEAQgUhAEJFHQBCBR0AQkUNAEIFDQAiRQEAQgUBAIJFAQBCBQEAI
kTxAEIE8QFCRREAQgURACJFEQBCBREAgkURAEIFEQCCRREAQgURACJFGQBCBRkAgkUNAEIFDQAiR
QEAQgUBAIJFAQBCBQEAIkTxAEIE8QFCRREAQgURACJFEQBCBREAgkURAEIFEQCCRREAQgURACJFG
QBCBRkAIkUNAEIFDQIFIkURAEIFEQAiRREAQgURAIJFEQBCBREAgkURAEIFEQAiRRkAQgUZAIJFD
QBCBQ0AIkUBAEIFAQCCRQEAQgUBACJE8QBCBPEBQkUJAEIFCQAiRQkAQgUJAIJFCQBCBQkAgkUJA
EIFCQAiRQkAQgUJAIJFHQBCBR0BQkUNAEIFDQFCRSEAQgUhACJFFQBCBRUAgkUBAEIFAQDiRQEAQ
gUBAIJFBQBCBQUAIkUhAEIFIQCCRSEAQgUhACJFBQBCBQUBQkUNAEIFDQBCRTUAQgU1AEJFNQBCB
TUAQkU1AEIFNQBCRTEAQgUxAEJFKQBCBSkAQkUhAEIFIQAiRRUAQgUVAIJFBQBCBQUAIkUBAEIFA
QFCRSEAQgUhACJFFQBCBRUAgkUBAEIFAQDiRQEAQgUBAIJFBQBCBQUAIkUhAEIFIQCCRSEAQgUhA
CJFBQBCBQUBQkUNAEIFDQAiRSkAQgUpAIJFKQBCBSkAIkUpAEIFKQBCRSEAQgUhAEJFHQBCBR0AQ
kUNAEIFDQAiRQEAQgUBAIJFAQBCBQEAIkTxAEIE8QAD/LwBNVHJrAAAJPwD/AwlCYXNzIExpbmUA
sgAAAMIaAP9YBAQCYAgA/1EDCLgkAJIyQBCCMkAIkjJAEIIyQCCSMkAQgjJAIJIyQBCCMkAIkjJA
EIIyQCCSQ0AQgkNAUJI3QBCCN0BQkjdAEII3QDiSNEAQgjRAOJIwQBCCMEA4kjVAEII1QCCSN0AQ
gjdAIJI2QBCCNkAIkjVAEII1QCCSNEAQgjRAEJI8QBCCPEAQkkBAEIJAQBCSQUAQgkFAIJI+QBCC
PkAIkkBAEIJAQCCSPEAQgjxAIJI5QBCCOUAIkjtAEII7QAiSN0AQgjdAOJI3QBCCN0A4kjRAEII0
QDiSMEAQgjBAOJI1QBCCNUAgkjdAEII3QCCSNkAQgjZACJI1QBCCNUAgkjRAEII0QBCSPEAQgjxA
EJJAQBCCQEAQkkFAEIJBQCCSPkAQgj5ACJJAQBCCQEAgkjxAEII8QCCSOUAQgjlACJI7QBCCO0AI
kjdAEII3QDiSMEAQgjBAOJI3QBCCN0A4kjxAEII8QCCSNUAQgjVAOJI8QBCCPEAIkjxAEII8QCCS
NUAQgjVAIJIwQBCCMEA4kjRAEII0QDiSN0AQgjdACJI8QBCCPEAgkk9AEIJPQCCST0AQgk9ACJJP
QBCCT0AgkjdAEII3QCCSMEAQgjBAOJI3QBCCN0A4kjxAEII8QCCSNUAQgjVAOJI8QBCCPEAIkjxA
EII8QCCSNUAQgjVAIJIwQBCCMEAgkjhAEII4QDiSOkAQgjpAOJI8QBCCPEA4kjdAEII3QAiSN0AQ
gjdAIJIwQBCCMEAgkjBAEIIwQDiSN0AQgjdAOJI8QBCCPEAgkjVAEII1QDiSPEAQgjxACJI8QBCC
PEAgkjVAEII1QCCSMEAQgjBAOJI0QBCCNEA4kjdAEII3QAiSPEAQgjxAIJJPQBCCT0Agkk9AEIJP
QAiST0AQgk9AIJI3QBCCN0AgkjBAEIIwQDiSN0AQgjdAOJI8QBCCPEAgkjVAEII1QDiSPEAQgjxA
CJI8QBCCPEAgkjVAEII1QCCSMEAQgjBAIJI4QBCCOEA4kjpAEII6QDiSPEAQgjxAOJI3QBCCN0AI
kjdAEII3QCCSMEAQgjBAIJIsQBCCLEA4kjNAEIIzQDiSOEAQgjhAIJI3QBCCN0A4kjBAEIIwQDiS
K0AQgitAIJIsQBCCLEA4kjNAEIIzQDiSOEAQgjhAIJI3QBCCN0A4kjBAEIIwQDiSK0AQgitAIJIs
QBCCLEA4kjNAEIIzQDiSOEAQgjhAIJI3QBCCN0A4kjBAEIIwQDiSK0AQgitAIJIyQBCCMkAIkjJA
EIIyQCCSMkAQgjJAIJIyQBCCMkAIkjJAEIIyQCCSQ0AQgkNAUJI3QBCCN0BQkjdAEII3QDiSNEAQ
gjRAOJIwQBCCMEA4kjVAEII1QCCSN0AQgjdAIJI2QBCCNkAIkjVAEII1QCCSNEAQgjRAEJI8QBCC
PEAQkkBAEIJAQBCSQUAQgkFAIJI+QBCCPkAIkkBAEIJAQCCSPEAQgjxAIJI5QBCCOUAIkjtAEII7
QAiSN0AQgjdAOJI3QBCCN0A4kjRAEII0QDiSMEAQgjBAOJI1QBCCNUAgkjdAEII3QCCSNkAQgjZA
CJI1QBCCNUAgkjRAEII0QBCSPEAQgjxAEJJAQBCCQEAQkkFAEIJBQCCSPkAQgj5ACJJAQBCCQEAg
kjxAEII8QCCSOUAQgjlACJI7QBCCO0AIkjdAEII3QDiSMEAQgjBAOJI2QBCCNkAIkjdAEII3QCCS
PEAQgjxAIJI1QBCCNUAgkjVAEII1QCCSPEAQgjxACJI8QBCCPEAIkjVAEII1QCCSMkAQgjJAOJI1
QBCCNUAIkjdAEII3QCCSO0AQgjtAIJI3QBCCN0AgkjdAEII3QCCSPEAQgjxACJI8QBCCPEAIkjdA
EII3QCCSMEAQgjBAOJI2QBCCNkAIkjdAEII3QCCSPEAQgjxAIJI1QBCCNUAgkjVAEII1QCCSPEAQ
gjxACJI8QBCCPEAIkjVAEII1QCCSN0AQgjdACJI3QBCCN0AgkjdAEII3QAiSN0AQgjdAEJI5QBCC
OUAQkjtAEII7QBCSPEAQgjxAIJI3QBCCN0AgkjBAEIIwQFCSMEAQgjBAOJI2QBCCNkAIkjdAEII3
QCCSPEAQgjxAIJI1QBCCNUAgkjVAEII1QCCSPEAQgjxACJI8QBCCPEAIkjVAEII1QCCSMkAQgjJA
OJI1QBCCNUAIkjdAEII3QCCSO0AQgjtAIJI3QBCCN0AgkjdAEII3QCCSPEAQgjxACJI8QBCCPEAI
kjdAEII3QCCSMEAQgjBAOJI2QBCCNkAIkjdAEII3QCCSPEAQgjxAIJI1QBCCNUAgkjVAEII1QCCS
PEAQgjxACJI8QBCCPEAIkjVAEII1QCCSN0AQgjdACJI3QBCCN0AgkjdAEII3QAiSN0AQgjdAEJI5
QBCCOUAQkjtAEII7QBCSPEAQgjxAIJI3QBCCN0AgkjBAEIIwQFCSLEAQgixAOJIzQBCCM0A4kjhA
EII4QCCSN0AQgjdAOJIwQBCCMEA4kitAEIIrQCCSLEAQgixAOJIzQBCCM0A4kjhAEII4QCCSN0AQ
gjdAOJIwQBCCMEA4kitAEIIrQCCSLEAQgixAOJIzQBCCM0A4kjhAEII4QCCSN0AQgjdAOJIwQBCC
MEA4kitAEIIrQCCSMkAQgjJACJIyQBCCMkAgkjJAEIIyQCCSMkAQgjJACJIyQBCCMkAgkkNAEIJD
QFCSN0AQgjdAUJIwQBCCMEA4kjZAEII2QAiSN0AQgjdAIJI8QBCCPEAgkjVAEII1QCCSNUAQgjVA
IJI8QBCCPEAIkjxAEII8QAiSNUAQgjVAIJIyQBCCMkA4kjVAEII1QAiSN0AQgjdAIJI7QBCCO0Ag
kjdAEII3QCCSN0AQgjdAIJI8QBCCPEAIkjxAEII8QAiSN0AQgjdAIJIwQBCCMEA4kjZAEII2QAiS
N0AQgjdAIJI8QBCCPEAgkjVAEII1QCCSNUAQgjVAIJI8QBCCPEAIkjxAEII8QAiSNUAQgjVAIJI3
QBCCN0AIkjdAEII3QCCSN0AQgjdACJI3QBCCN0AQkjlAEII5QBCSO0AQgjtAEJI8QBCCPEAgkjdA
EII3QCCSMEAQgjBAAP8vAE1UcmsAAAv4AP8DClBlcmN1c3Npb24AuQAAAMkAAP9YBAQCYAgA/1ED
CLgkAJkqYCCJKkAQmSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAImSpgIIkqQBCZKmAgiSpAKJkqYCCJ
KkAQmSpgEIkqQAiZKmAQiSpACJkqYBCJKkAImSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkq
QBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpA
EJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAA
mSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZ
KmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkq
YBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpg
IIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQ
iSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJ
KkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkq
QCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpA
EJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAA
mSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZ
KmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkq
YBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpg
EIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQ
iSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJ
KkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkq
QBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpA
EJkqYBCJKkAAmSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAA
mSpgEIkqQCCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgEIkqQCCZ
KmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpAEJkqYBCJKkAAmSpgIIkqQBCZKmAQiSpACJkq
YCCJKkAQmSpgEIkqQAiZKmAgiSpAEJkqYCCJKkAomSpgIIkqQBCZKmAQiSpACJkqYBCJKkAImSpg
EIkqQAiZKmAgiSpAEJkqYBCJKkAImSpgIIkqQBCZKmAQiSpACJkqYCCJKkAQmSpgIIkqQCiZKmAg
iSpAEJkqYBCJKkAImSpgEIkqQAiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQAiZKmAgiSpAEJkqYBCJ
KkAImSpgIIkqQBCZKmAgiSpAKJkqYCCJKkAQmSpgEIkqQAiZKmAQiSpACJkqYBCJKkAImSpgIIkq
QBCZKmAQiSpACJkqYCCJKkAQmSpgEIkqQAiZKmAgiSpAEJkqYCCJKkAomSpgIIkqQBCZKmAQiSpA
CJkqYBCJKkAImSpgEIkqQAiZKmAQiSpAIJkqYBCJKkAQmSpgEIkqQACZKmAgiSpAEJkqYBCJKkAQ
mSpgEIkqQACZKmAQiSpAIJkqYBCJKkAQmSpgEIkqQACZKmAgiSpAEJkqYBCJKkAQmSpgEIkqQACZ
KmAQiSpAIJkqYBCJKkAQmSpgEIkqQACZKmAgiSpAEJkqYBCJKkAQmSpgEIkqQACZKmAQiSpAIJkq
YBCJKkAQmSpgEIkqQACZKmAgiSpAEJkqYBCJKkAQmSpgEIkqQACZKmAQiSpAIJkqYBCJKkAQmSpg
EIkqQACZKmAgiSpAEJkqYBCJKkAQmSpgEIkqQACZKmAQiSpAIJkqYBCJKkAQmSpgEIkqQACZKmAg
iSpAEJkqYBCJKkAQmSpgEIkqQACZKmAQiSpAIJkqYBCJKkAQmSpgEIkqQACZKmAgiSpAEJkqYBCJ
KkAQmSpgEIkqQACZKmAQiSpAIJkqYBCJKkAQmSpgEIkqQACZKmAgiSpAEJkqYBCJKkAQmSpgEIkq
QACZKmAQiSpAOJkqYBCJKkAImSpgIIkqQBCZKmAQiSpAIJkqYBCJKkA4mSpgEIkqQAiZKmAgiSpA
EJkqYBCJKkAgmSpgEIkqQDiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQCCZKmAQiSpAOJkqYBCJKkAI
mSpgIIkqQBCZKmAQiSpAIJkqYBCJKkA4mSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAgmSpgEIkqQDiZ
KmAQiSpACJkqYCCJKkAQmSpgEIkqQCCZKmAQiSpAOJkqYBCJKkAImSpgIIkqQBCZKmAQiSpAIJkq
YBCJKkA4mSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAgmSpgEIkqQDiZKmAQiSpACJkqYCCJKkAQmSpg
EIkqQCCZKmAQiSpAOJkqYBCJKkAImSpgIIkqQBCZKmAQiSpAIJkqYBCJKkA4mSpgEIkqQAiZKmAg
iSpAEJkqYBCJKkAgmSpgEIkqQDiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQCCZKmAQiSpAOJkqYBCJ
KkAImSpgIIkqQBCZKmAQiSpAIJkqYBCJKkA4mSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAgmSpgEIkq
QDiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQCCZKmAQiSpAOJkqYBCJKkAImSpgIIkqQBCZKmAQiSpA
IJkqYCCJKkAQmSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAImSpgIIkqQBCZKmAgiSpAKJkqYCCJKkAQ
mSpgEIkqQAiZKmAQiSpACJkqYBCJKkAImSpgIIkqQBCZKmAQiSpACJkqYCCJKkAQmSpgEIkqQAiZ
KmAgiSpAEJkqYCCJKkAomSpgIIkqQBCZKmAQiSpACJkqYBCJKkAImSpgEIkqQAiZKmAgiSpAEJkq
YBCJKkAImSpgIIkqQBCZKmAQiSpACJkqYCCJKkAQmSpgIIkqQCiZKmAgiSpAEJkqYBCJKkAImSpg
EIkqQAiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAImSpgIIkqQBCZKmAg
iSpAKJkqYCCJKkAQmSpgEIkqQAiZKmAQiSpACJkqYBCJKkAImSpgEIkqQDiZKmAQiSpACJkqYCCJ
KkAQmSpgEIkqQCCZKmAQiSpAOJkqYBCJKkAImSpgIIkqQBCZKmAQiSpAIJkqYBCJKkA4mSpgEIkq
QAiZKmAgiSpAEJkqYBCJKkAgmSpgEIkqQDiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQCCZKmAQiSpA
OJkqYBCJKkAImSpgIIkqQBCZKmAQiSpAIJkqYBCJKkA4mSpgEIkqQAiZKmAgiSpAEJkqYBCJKkAg
mSpgEIkqQDiZKmAQiSpACJkqYCCJKkAQmSpgEIkqQCCZKmAQiSpAOJkqYBCJKkAImSpgIIkqQBCZ
KmAQiSpAAP8vAA==
'''
music_file = "tmp.mid"
# convert back to a binary midi and save to a file in the working directory
fish = base64.b64decode(mid64)
fout = open(music_file,"wb")
fout.write(fish)
fout.close()
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
try:
    # use the midi file you just saved
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit