/*
  La mia rubrica
  Scrivi un programma per la gestione di una rubrica telefonica.

  Definisci un oggetto che rappresenti un contatto e, visto che stai diventando bravo/a, le proprietà dell'oggetto sono a tua discrizione.
  L'unico vincolo che hai è di inserire almeno il nome e il numero di telefono come stringhe.

  Definisci un altro oggetto che rappresenti la lista dei contatti, quindi sarà formato da un array di contatti.
  Implementa i metodi dell'oggetto per le seguenti operazioni:
      - Visualizzazione dell'intera lista contatti
      - Inserimento di un nuovo contatto
      - Modifica di uno contatto passando in input l'indice dell'array
      - Cancellazione di un contatto passando in input l'indice dell'array
      - Ricerca passando il nome e restituendo il singolo contatto.

  Variante:
  Migliora i metodi di Modifica e Cancellazione, al posto di prendere in input l'indice dell'array passa in input il nome
  e ricava l'indice sul quale applicare l'operazione.

  http://www.imparareaprogrammare.it
*/
//CONTACT LIST DATABASE
var ContactList = {
  Bill_Gates: {
    COMPLETE_NAME: "Bill Gates",
    NAME: "Bill",
    SURNAME: "Gates",
    PHONE_NUMBER: "206-200-0337",
    ADDRESS: "Evergreen Point Road,Seattle,WA"
  },
  Elon_Musk: {
    COMPLETE_NAME: "Elon Musk",
    NAME: "Elon",
    SURNAME: "Musk",
    PHONE_NUMBER: "213-220-9553",
    ADRESS: "Chalon Rd,Los Angeles,CA"
  },
  Jeff_Bezos: {
   COMPLETE_NAME: "Jeff Bezos",
   NAME: "Jeff",
   SURNAME: "Bezos",
   PHONE_NUMBER: "202-555-0194",
   ADDRESS: "Evergreen Point Road,Seattle,WA"
  },
  Steve_Jobs: {
    NAME: "Steve",
    SURNAME: "Jobs",
    PHONE_NUMBER: "650-248-5015",
    ADRESS: "Santa RIta Avenue,Palo Alto,CA"
  }
}

var ContactName = [
  "Bill Gates","Elon Musk","Jeff Bezos","Steve Jobs" 
]

function SeeAllList () {
   var SupportSee = true 
   if (SupportSee)
     return ContactList
}

function AddNewContact() { 
 var SupportAdd = true
  if (SupportAdd)
    return ContactList.Mark_Zuckerberg = {
    COMPLETE_NAME: "Mark Zuckerberg",
    NAME: "Mark",
    SURNAME: "ZuCkerberg",
    PHONE_NUMBER: "650-468-0039",
    ADDRESS: ",Palo Alto,CA"
 }
}

function SupportName() {
 if (SupportAdd = true)
   return ContactList.Murk_Zuckerberg.COMPLETE_NAME
}
function EditContact() {
var SupportEdit = 2
if (SupportEdit >= 0)
  return ContactList.Bill_Gatesa = {
    COMPLETE_NAME: "Bill Gates",
    NAME: "Bill",
    SURNAME: "Gates",
    PHONE_NUMBER: "206-200-0337",
    ADDRESS: "Evergreen Point Road,Seattle,WA"
  }
  
if (SupportEdit >= 1)
  return ContactList.Elon_Musk = {
    COMPLETE_NAME: "Elon Musk",
    NAME: "Elon",
    SURNAME: "Musk",
    PHONE_NUMBER: "213-220-9553",
    ADRESS: "Chalon Rd,Los Angeles,CA"
  }
  
if (SupportEdit >= 2)
  return ContactList.Jeff_Besos = {
   COMPLETE_NAME: "Jeff Besos",
   NAME: "Jeff",
   SURNAME: "Bezos",
   PHONE_NUMBER: "202-555-0194",
   ADDRESS: "Evergreen Point Road,Seattle,WA"
  }

if (SupportEdit >= 3)
  return ContactLit.Steve_Jobs = {
   COMPLETE_NAME: "Steve Jobs",
   NAME: "Steve",
   SURNAME: "Jobs",
   PHONE_NUMBER: "650-248-5015",
   ADRESS: "Santa RIta Avenue,Palo Alto,CA"
  }
  
 if (SupportEdit >= 4)
   return ContactList.Mark_Zuckerberg = {
    NAME: "Mark",
    SURNAME: "ZuCkerberg",
    PHONE_NUMBER: "650-468-0039",
    ADDRESS: ",Palo Alto,CA"
   }
}

function DeleteContact() {
 var SupportDelete = false
  if (SupportDelete) 
    return delete ContactList ["Bill_Gates"]
}

function SearchSingleContact() {
  var Request = "Bill Gates"
  if (Request = ContactName[0])
    console.log(ContactList.Bill_Gates) 
}
 
var AddressBook  = {   
  ADD_NEW_CONTACT: AddNewContact(),
  EDIT_CONTACT: EditContact(),
  DELETE_CONTACT: DeleteContact(),
  SEARCH_SNGLE_CONTACTS: SearchSingleContact(),
  ALL_CONTACT: SeeAllList()
  
} 

console.log(AddressBook.SEARCH_SINGLE_CONTACT)
