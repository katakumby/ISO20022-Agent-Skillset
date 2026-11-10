---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["3 Mapping of the BAH to other headers"]
file_pages: [24, 25]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3 Mapping of the BAH to other headers

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 24 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
24 ISO 20022 Business Application Header Message Usage Guide v3.0  
3 Mapping of the BAH to other headers 
In a number of situations, ISO 20022 (business) messages are employed in heterogeneous 
environments where the end-to-end use of the BAH cannot be taken for granted or where over time 
the migration from proprietary headers to the BAH is foreseen. 
In these situations, it can be useful to understand the equivalencies of the elements of the various 
headers in use. 
3.1  Introduction  
Below list contains all MessageElements of the BusinessApplicationHeader. 
For reference, this table lists the top MessageElement names of the BAH and their 
equivalent XML abbreviation. 
 
MessageElement 
Name 
abbreviation 
CharacterSet CharSet 
From Fr 
To To 
BusinessMessageIdentifier BizMsgIdr 
MessageDefinitionIdentifier MsgDefIdr 
BusinessService BizSvc 
MarketPractice MktPrctc 
CreationDate CreDt 
BusinessProcessingDate BizPrcgDt 
CopyDuplicate CpyDplct 
PossibleDuplicate PssblDplct 
Priority Prty 
Signature Sgntr 
Related Rltd 
 
3.2  BAH to SWIFTNet Application  Header  
The table below states the equivalencies of the BAH elements in comparison to the elements of the 
proprietary SWIFTNet Application Header. 
This mapping can be useful in a number of cases: 
a) Introducing the BAH for ISO 20022 message sets modelled for use with and without 
the BAH 
As such message sets do not require the use of the BAH, it is often the case that such message 
sets are deplo yed with a non -ISO 20022 header, for instance, the SWIFTNet Application 
Header.  
As and when such communities decide to migrate from the proprietary header to the BAH, the 
mapping table can be employed as a migration support tool. 
b) ISO 20022 message sets employed in a multiple network environment 
It is not uncommon that in an end-to-end scenario the exchange of ISO 20022 message sets 
spans multiple underlying networks, amongst others, SWIFTNet. SWIFTNet may still foresee 
its own proprietary Application Header whilst others may already have migrated to using the 
BAH. 
```

## File page 25

```text
25 ISO 20022 Business Application Header Message Usage Guide v3.0  
In order to ensure that the business information of the BAH elements can be correctly conveyed 
to and from their sibling elements of the SWIFTNet Application Headers, the mapping table can 
be used to support the implementation of the information exchange at the gateways between 
SWIFTNet and the other networks. 
 
Business Application Header MessageElement SWIFTNet Application 
Header 
character set 
the additionally used character set(s) in the BusinessMessage for Text 
datatypes 
- 
Sending Business Entity 
the Business Entity that created the BusinessMessage 
<RequestorDN> 
Receiving Business Entity 
the Business Entity that will process the BusinessMessage 
<ResponderDN> 
BusinessMessageIdentifier 
the identification of the BusinessMessage, unique to the 
SendingBusinessEntity 
<MessageReference> 
MessageDefinitionIdentifier 
the identification of MessageDefinition 
<MessageIdentifier> 
BusinessService Example: EnI <ServiceName> 
Market Practice 
Set of rules agreed between parties that restricts the usage of 
the messages in order to achieve better STP (Straight Through 
Processing) rates. 
- 
CreationDate 
Creation date (and time) of the Business Message 
<CreationDate> 
Business Processing Date 
Processing date and time indicated by the sender for the receiver 
of the business message. 
- 
Copy / Duplicate / 
Functionality to indicate this message is a copy / duplicate of another 
<SnFCopy> 
Possible Duplicate 
The BusinessMessage may have been sent before. 
<PossibleDuplicate> 
Priority 
Relative indication of the processing precedence of the message over 
a (set of) BusinessMessages with assigned priorities 
<Priority> 
Signature 
Contains the digital signature of the person authorised to sign this 
BusinessMessage (based on W3C’s XML Signature standard) 
<Signed> 
Related Reference 
Reference of the original BusinessMessage 
<Related> 
BusinessMessage  
```

