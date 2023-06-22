def matrix_multiply(matrix, vector):
    result = [0, 0]
    result[0] = (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26
    result[1] = (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26
    return result

def encrypt(message, key_matrix):
    alphabet = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    encrypted_message = ""
    if len(message) % 2 != 0:
        message += 'Z'
    for i in range(0, len(message), 2):
        vector = [alphabet.index(message[i]), alphabet.index(message[i+1])]
        result = matrix_multiply(key_matrix, vector)
        encrypted_message += alphabet[result[0]] + alphabet[result[1]]
    return encrypted_message

key_matrix = [[1, 3], [1, 2]]
message = input("Digite a mensagem para criptografar: ").upper()
encrypted_message = encrypt(message, key_matrix)
print("Mensagem criptografada: ", encrypted_message)
