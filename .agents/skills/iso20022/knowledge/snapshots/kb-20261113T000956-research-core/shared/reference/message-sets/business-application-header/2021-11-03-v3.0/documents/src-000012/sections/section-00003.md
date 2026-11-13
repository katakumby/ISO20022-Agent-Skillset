---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["1 Introduction", "1.4 Separation of layers"]
file_pages: [4]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 1.4 Separation of layers

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 4 to 4.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
4 ISO 20022 Business Application Header Message Usage Guide v3.0  
1.4  Separation of layers 
ISO 20022 messages and the BAH are designed to be transport protocol independent. The ISO 20022 
standard does not provide any message transport conventions of its own (including header or trailer). 
The Business Application Header is a business heade r and should not be confused with a file or 
transport header. The Business Application Header is created and applied to its ISO 20022 Message 
to form a Business Message. Subsequently, a file or transport routing header, if any, is applied to the 
Business Message. 
So, any parties between the two business applications that do not perform a business function are 
not mentioned in the BAH. Such 'technical' middle men do not open or change the Business Message; 
they only forward it to the correct business application. 
So, a transport scenario like below 
is from a business point of view the same as a transport scenario like this: 
because the technical middle man is forwarding the message, without changing the contents. 
However, as soon as a Business Application is in the middle (i.e. an Application that processes the 
Business Message), it is identified in the BAH of the first message as the recipient, and in the BAH of 
the second message as the sender, and therefore sends a different business message. 
 
Although the BAH is not the transport header, data in the BAH, as data in the ISO 20022 message 
itself, can be used by transport applications to determine the routing header since it does contain the 
business sender, receiver and document details. It can also be used by the business applications to 
determine the appropriate process to perform on the business message.  
  

```

