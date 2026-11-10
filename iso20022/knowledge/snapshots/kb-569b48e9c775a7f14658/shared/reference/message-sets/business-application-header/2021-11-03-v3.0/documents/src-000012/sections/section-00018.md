---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.12 Business Application A sends a signed Business Message  to BusinessApplication B"]
file_pages: [21, 22, 23]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.12 Business Application A sends a signed Business Message  to BusinessApplication B

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 21 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
21 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
2.12  Business Application A sends a signed Business Message  
to BusinessApplication  B 
The signature must be structured as per the W3C XML Signature specification and any additional 
constraints stated for the service / market practice / business area within which this BusinessMessage 
is exchanged. 
Refer to the Signature Annex for more information. 
 
Following MessageElements must be used: 
 
MessageElement 
Name 
Usage 
CharacterSet  
From Id of BusinessApplication A 
To Id of BusinessApplication B 
BusinessMessageIdentifier Identification of the BusinessMessage A 
MessageDefinitionIdentifier Identification of the MessageDefinition 
BusinessService  
MarketPractice  
CreationDate Date (and time) of the creation of this BusinessApplicationHeader 
(and BusinessMessage) 
BusinessProcessingDate  
CopyDuplicate  
PossibleDuplicate  
Priority  
Signature Signature specification containing the signature of the 
Sending Business Entity 
Related  
 
2.13  Business Application B sends a Business Message B  
that relates to Business Message A 
In this type of scenario, BusinessMessage B is neither a copy nor a duplicate of BusinessMessage A. 
This scenario can be witnessed in a number of ISO 20022 domains. Whenever an ISO 20022 business 
process foresees that multiple business messages of potentially different message definitions are 
employed, a particular business message may refer, for instance, to a message previously received 
and/or a message previously sent.  
This pattern is particularly common when a business process extends over a chain of multiple 
intermediaries, for example, a chain of investment funds order execution intermediaries, a chain of 
securities settlement agents, a securities custody chain or a chain of payment correspondent banks. 
  
```

## File page 22

```text
22 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
 
As depicted in the diagram, this scenario is used when it is relevant for the recipient  of 
BusinessMessage B to know about the underlying BusinessMessage A which triggered the creation of 
this BusinessMessage B. BusinessMessage B will indicated in its Related element all details of the 
Business Application Header of BusinessMessage A, for instance, the entity who created the original 
BusinessMessage A (in the From element of the Related element). 
CopyDuplicate and PossibleDuplicate are not used in this scenario. 
 
MessageElement 
Name 
Usage 
CharacterSet  
From Id of BusinessApplication A 
To Id of BusinessApplication B 
BusinessMessageIdentifier Identification of the BusinessMessage A 
MessageDefinitionIdentifier Identification of the MessageDefinition 
BusinessService  
MarketPractice  
CreationDate Date (and time) of the creation of this BusinessApplicationHeader 
(and BusinessMessage) 
BusinessProcessingDate  
CopyDuplicate  
PossibleDuplicate  
Priority  
Signature  
Related Copy of the relevant MessageElements of the 
BusinessApplicationHeader of BusinessMessage A 
 
As a business message may be related to multiple other business messages, it is necessary to be able 
to distinguish the function of each of the business messages referred to. For this purpose, th e 
MessageDefinitionIdentifier of the business messages referred to can be used. 
EXAMPLE 
Consider the following scenario of the investment funds order execution business process.  
The SubscriptionOrderConfirmationCancellationInstruction (setr.047) cancels a previously sent 
SubscriptionOrderConfirmation (setr.012) and is related to a previously received SubscriptionOrder 
(setr.010). 

```

## File page 23

```text
23 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
If in this example the three messages involved are used with the BAH, one instance of the Related 
element of the BAH with the setr.047 message can be used to identify the previously sent business 
message (setr.012) and the other instance can be used to identify the previously received business 
message (setr.010). 
The mandatory MessageDefinitionIdentifier, which is indicated for each of the two business messages 
in their respective Related element, can be used to distinguish the function of the two related business 
messages. 
EXAMPLE 
In the payments domain, consider the ResolutionOfInvestigationV08 message (camt.029). The 
elements OriginalGroupInformationAndStatus / OriginalMessageIdentification and 
OriginalGroupInformation / OriginalMessageIdentification refer to other linked messages, i.e. the 
FIToFIPaymentCancellationRequestV07 message (camt.056) and the 
FIToFICustomerCreditTransferV07 message (pacs.008), respectively. These messages are used for 
exceptions and investigations. 
 
 
 

```

