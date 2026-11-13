---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["1 Introduction", "1.5 Link between a Business Application Header and its Message"]
file_pages: [5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.03", "pacs.008.001.08"]
---

# 1.5 Link between a Business Application Header and its Message

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 5 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
5 ISO 20022 Business Application Header Message Usage Guide v3.0  
1.5  Link between  a Business Application Header and its  Message 
A Business Application Header is typically packaged with its ISO 20022 Message root element following 
the BAH’s root element in an XML envelope. Other packaging is possible, such as zip files, or mime 
multi part. 
Although the standard does not specify the order of the Business Application Header (AppHdr XML 
element) and the ISO 20022 Message (Document XML element), it is common best practice that the 
Business Application Header precedes the ISO 20022 message. 
EXAMPLE 
Below XML Schema describes an element RequestPayload (used on SWIFTNet) that contains two 
elements: AppHdr and any other element. 
 
 
 
A valid XML instance would be structured as follows: 
 
  
<?xml version="1.0" encoding="UTF-8"?> 
<n1:RequestPayload xmlns:n1="SWIFTNetBusinessEnvelope" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:n2="urn:iso:std:iso:20022:tech:xsd:head.001.001.03" 
xsi:schemaLocation="SWIFTNetBusinessEnvelope AppHdrBizMsg.xsd"> 
 <n2:AppHdr xmlns:n2="urn:iso:std:iso:20022:tech:xsd:head.001.001.03"> 
  ... 
 </n2:AppHdr> 
 <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"> 
  ... 
 </Document> 
</n1:RequestPayload> 
Refers to the 
envelope 
schema 
Ref ers to the ISO 
20022 Business 
Application Header 
Ref ers to the ISO 
20022 Message 
```

