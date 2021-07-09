# Trabalhando com Número de Telefone
# Referência: https://pypi.org/project/phonenumbers/

import phonenumbers

## Ajuste do telefone
telefone = "++5511999999999"
telefone_ajustado = phonenumbers.parse(telefone)
# telefone = "11971153763"
# telefone_ajustado = phonenumbers.parse(telefone, "BR")
print(telefone_ajustado)


## Descobrir a localização do telefone
from phonenumbers import geocoder

local = geocoder.description_for_number(telefone_ajustado, "pt-br")
print("Localização:", local)


## Descobrir operadora do telefone
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
print("Operadora:", operadora)


## Formatar telefone
# telefone_formulario = "11999999999" -> (11)99999-9999
telefone_formulario = "11999999999"
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")
telefone_formulario_formatado = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
# telefone_formulario_formatado = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)
print("\nTelefone antes:", telefone_formulario)
print("Telefone ajustado:", telefone_formulario_formatado)


## Retirar telefone de um texto
corpo_email = """
Prezados,

Quando tiverem uma resposta da proposta, favor entrar em contato.

Abs,
Lira
(21)99999-9999
"""
print("\nExtraindo telefones do e-mail...")
for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, "BR"):
    print(telefone)