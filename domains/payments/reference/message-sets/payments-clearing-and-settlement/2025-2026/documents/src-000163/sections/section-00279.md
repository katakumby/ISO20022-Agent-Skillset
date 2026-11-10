---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.2 Structured <Strd>", "4.4.3.27.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.27.11.2.1.4 LineDetails <LineDtls>", "4.4.3.27.11.2.1.4.1 Identification <Id>", "4.4.3.27.11.2.1.4.1.1 Type <Tp>"]
file_pages: [404]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.2.1.4.1.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 404 to 404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 404

```text
Identification <Id> contains the following DocumentLineIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  404
     CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or       Code <Cd> [1..1] CodeSet 404
Or}       Proprietary <Prtry> [1..1] Text 404
     Issuer <Issr> [0..1] Text 405
   Number <Nb> [0..1] Text 405
   RelatedDate <RltdDt> [0..1] Date 405
4.4.3.27.11.2.1.4.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document line identification.
Type <Tp> contains the following DocumentLineType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or     Code <Cd> [1..1] CodeSet 404
Or}     Proprietary <Prtry> [1..1] Text 404
   Issuer <Issr> [0..1] Text 405
4.4.3.27.11.2.1.4.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the referred document line identification.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentLineType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 404
Or}   Proprietary <Prtry> [1..1] Text 404
4.4.3.27.11.2.1.4.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Line identification type in a coded form.
Datatype: "ExternalDocumentLineType1Code" on page 1229
4.4.3.27.11.2.1.4.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
404 March 2026
```

