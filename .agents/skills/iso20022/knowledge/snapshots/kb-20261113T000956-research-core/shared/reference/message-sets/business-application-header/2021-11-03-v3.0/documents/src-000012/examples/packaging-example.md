---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "source-example"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
curated: true
file_pages: [5]
source_locations: ["§1.5 Link between a BAH and its Message"]
limitations: ["Source example retained; exact executable XML/cryptographic validity is not claimed."]
source_editions: ["Version 3.0 2021-11-03"]
---

# §1.5 Link between a BAH and its Message

[src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed page 5, §1.5 Link between a BAH and its Message.

The XSD screenshot and three callouts identify the envelope schema, BAH and ISO 20022 message. AppHdr precedes Document in this example. The narrative states that the standard does not specify their order and permits other packaging. The example uses head.001.001.03 and pacs.008.001.08, not the supplied V04 header schema.

[Complete original example rendered from PDF](../../../../../../../../evidence/omitted/52f2704b14078c94e8022e81.md)

## Preserved source text

This is the verbatim text extraction, including extraction spacing or replacement characters. Use the source page when exact lexical fidelity matters.

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

## Source components

- [fig-0005 original image component](../../../../../../../../evidence/omitted/0a8705975d0b3d478521dfb1.md).
- [fig-0006 original image component](../../../../../../../../evidence/omitted/b9bea46c31e0448c71871046.md).
- [fig-0007 original image component](../../../../../../../../evidence/omitted/ec0d1754638bfae5f51acdff.md).
- [fig-0008 original image component](../../../../../../../../evidence/omitted/920d8a26581be3090eb9b870.md).
