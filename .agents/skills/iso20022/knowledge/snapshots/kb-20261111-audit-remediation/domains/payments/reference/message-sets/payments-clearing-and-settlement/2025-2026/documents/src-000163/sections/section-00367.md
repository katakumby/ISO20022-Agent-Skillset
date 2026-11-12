---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.3 CreditorReferenceInformation <CdtrRefInf>", "4.4.3.27.23.30.2.3.1 Type <Tp>"]
file_pages: [509]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.3.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 509 to 509.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 509

```text
CreditorReferenceInformation <CdtrRefInf> contains the following CreditorReferenceInformation3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  509
     CodeOrProprietary <CdOrPrtry> [1..1]  509
{Or       Code <Cd> [1..1] CodeSet 509
Or}       Proprietary <Prtry> [1..1] Text 509
     Issuer <Issr> [0..1] Text 510
   Reference <Ref> [0..1] Text 510
4.4.3.27.23.30.2.3.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of creditor reference.
Type <Tp> contains the following CreditorReferenceType3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  509
{Or     Code <Cd> [1..1] CodeSet 509
Or}     Proprietary <Prtry> [1..1] Text 509
   Issuer <Issr> [0..1] Text 510
4.4.3.27.23.30.2.3.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format creditor reference type.
CodeOrProprietary <CdOrPrtry> contains one of the following CreditorReferenceType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 509
Or}   Proprietary <Prtry> [1..1] Text 509
4.4.3.27.23.30.2.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of creditor reference, as published in an external creditor reference type code set.
Datatype: "ExternalCreditorReferenceType1Code" on page 1229
4.4.3.27.23.30.2.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
509 March 2026
```

