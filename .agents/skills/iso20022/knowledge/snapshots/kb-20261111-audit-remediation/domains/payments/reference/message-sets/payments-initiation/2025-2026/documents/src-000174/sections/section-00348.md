---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.2.18.17.2.1.4 LineDetails <LineDtls>", "5.4.2.18.17.2.1.4.1 Identification <Id>", "5.4.2.18.17.2.1.4.1.1 Type <Tp>"]
file_pages: [497]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.1.4.1.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 497 to 497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 497

```text
Identification <Id> contains the following DocumentLineIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  497
     CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or       Code <Cd> [1..1] CodeSet 497
Or}       Proprietary <Prtry> [1..1] Text 497
     Issuer <Issr> [0..1] Text 498
   Number <Nb> [0..1] Text 498
   RelatedDate <RltdDt> [0..1] Date 498
5.4.2.18.17.2.1.4.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document line identification.
Type <Tp> contains the following DocumentLineType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or     Code <Cd> [1..1] CodeSet 497
Or}     Proprietary <Prtry> [1..1] Text 497
   Issuer <Issr> [0..1] Text 498
5.4.2.18.17.2.1.4.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the referred document line identification.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentLineType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 497
Or}   Proprietary <Prtry> [1..1] Text 497
5.4.2.18.17.2.1.4.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Line identification type in a coded form.
Datatype: "ExternalDocumentLineType1Code" on page 594
5.4.2.18.17.2.1.4.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 497 March 2026
```

