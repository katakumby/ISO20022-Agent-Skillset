---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.35.2.1.4 LineDetails <LineDtls>", "3.4.2.35.2.1.4.1 Identification <Id>", "3.4.2.35.2.1.4.1.1 Type <Tp>"]
file_pages: [216]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.1.4.1.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 216 to 216.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
Identification <Id> contains the following DocumentLineIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  216
     CodeOrProprietary <CdOrPrtry> [1..1]  216
{Or       Code <Cd> [1..1] CodeSet 216
Or}       Proprietary <Prtry> [1..1] Text 216
     Issuer <Issr> [0..1] Text 217
   Number <Nb> [0..1] Text 217
   RelatedDate <RltdDt> [0..1] Date 217
3.4.2.35.2.1.4.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document line identification.
Type <Tp> contains the following DocumentLineType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  216
{Or     Code <Cd> [1..1] CodeSet 216
Or}     Proprietary <Prtry> [1..1] Text 216
   Issuer <Issr> [0..1] Text 217
3.4.2.35.2.1.4.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the referred document line identification.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentLineType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 216
Or}   Proprietary <Prtry> [1..1] Text 216
3.4.2.35.2.1.4.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Line identification type in a coded form.
Datatype: "ExternalDocumentLineType1Code" on page 1229
3.4.2.35.2.1.4.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
216 March 2026
```

