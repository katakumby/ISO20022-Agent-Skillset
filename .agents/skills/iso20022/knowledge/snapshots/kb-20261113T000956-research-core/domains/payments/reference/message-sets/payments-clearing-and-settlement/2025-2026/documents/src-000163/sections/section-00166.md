---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.3 CreditorReferenceInformation <CdtrRefInf>", "3.4.2.35.2.3.1 Type <Tp>"]
file_pages: [224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.3.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 224 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
CreditorReferenceInformation <CdtrRefInf> contains the following CreditorReferenceInformation3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  224
     CodeOrProprietary <CdOrPrtry> [1..1]  224
{Or       Code <Cd> [1..1] CodeSet 224
Or}       Proprietary <Prtry> [1..1] Text 224
     Issuer <Issr> [0..1] Text 225
   Reference <Ref> [0..1] Text 225
3.4.2.35.2.3.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of creditor reference.
Type <Tp> contains the following CreditorReferenceType3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  224
{Or     Code <Cd> [1..1] CodeSet 224
Or}     Proprietary <Prtry> [1..1] Text 224
   Issuer <Issr> [0..1] Text 225
3.4.2.35.2.3.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format creditor reference type.
CodeOrProprietary <CdOrPrtry> contains one of the following CreditorReferenceType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 224
Or}   Proprietary <Prtry> [1..1] Text 224
3.4.2.35.2.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of creditor reference, as published in an external creditor reference type code set.
Datatype: "ExternalCreditorReferenceType1Code" on page 1229
3.4.2.35.2.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
224 March 2026
```

