---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.3 CreditorReferenceInformation <CdtrRefInf>", "4.4.3.8.9.11.2.3.1 Type <Tp>"]
file_pages: [367]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.3.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 367 to 367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 367

```text
CreditorReferenceInformation <CdtrRefInf> contains the following CreditorReferenceInformation3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  367
     CodeOrProprietary <CdOrPrtry> [1..1]  367
{Or       Code <Cd> [1..1] CodeSet 367
Or}       Proprietary <Prtry> [1..1] Text 367
     Issuer <Issr> [0..1] Text 368
   Reference <Ref> [0..1] Text 368
4.4.3.8.9.11.2.3.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of creditor reference.
Type <Tp> contains the following CreditorReferenceType3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  367
{Or     Code <Cd> [1..1] CodeSet 367
Or}     Proprietary <Prtry> [1..1] Text 367
   Issuer <Issr> [0..1] Text 368
4.4.3.8.9.11.2.3.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format creditor reference type.
CodeOrProprietary <CdOrPrtry> contains one of the following CreditorReferenceType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 367
Or}   Proprietary <Prtry> [1..1] Text 367
4.4.3.8.9.11.2.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of creditor reference, as published in an external creditor reference type code set.
Datatype: "ExternalCreditorReferenceType1Code" on page 593
4.4.3.8.9.11.2.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 367 March 2026
```

