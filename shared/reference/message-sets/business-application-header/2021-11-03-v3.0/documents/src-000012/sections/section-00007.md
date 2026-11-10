---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.1 Business Application Header deployment options"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.1 Business Application Header deployment options

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
8 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
2.1  Business Application Header deployment  options 
The choice of whether to send a BAH with a given message is taken by each implementing community. 
Depending on how a given message was originally designed and/or any maintenance changes that 
may have occurred over time, an implementing community can be confronted with the following 
deployment options: 
 
Message 
deployment 
ISO 20022 message … 
with duplicated BAH elements without duplicated BAH 
elements1 
with BAH Business rules and market practice 
should determine the use of BAH 
elements in the BAH itself and any 
duplicated BAH elements in the ISO 
20022 message 
Only BAH elements within BAH are 
available for use 
without BAH Only BAH elements duplicated within 
ISO 20022 message are available for 
use 
BAH elements are not available for use, 
neither in ISO 20022 message nor 
through the BAH 
 
In the case of ISO 20022 messages without duplicated BAH elements, message deployment without 
the BAH can produce challenging situations (i.e. bottom right scenario in above table). 
 
In these scenarios, essential BAH elements like the unique message identifier (BAH element: 
BusinessMessageIdentifier) or the message creation date (BAH element: CreationDate) cannot be 
conveyed through the ISO 20022 message, nor through the BAH. 
 
If for certain implementation communities the deployment of the BAH does not constitute a valid 
choice, implementation communities are requested to get in contact with the ISO 20022 Registration 
Authority (RA) for advice on how to proceed in order to employ a fully ISO 20022 -compliant 
implementation (e-mail: iso20022ra@iso20022.org). 
 
Implementation communities may have alternative means to carry this information through non-ISO 
20022 mechanisms (e.g. a network header). It should be noted that, in case of non -ISO 20022 
mechanisms, not all scenarios covered in this BAH MUG could  be fully implemented. For further 
information, see chapter 2.3. 
 
1 ISO 20022 messages without duplicated BAH elements are labelled, in the Business domain 
catalogues on the ISO 20022 web-site, with the sentence “The message definitions below are intended 
for use with the Business Application Header.”. 
```

