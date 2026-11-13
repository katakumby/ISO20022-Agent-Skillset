---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.3 CreditorReferenceInformation <CdtrRefInf>", "4.4.2.14.18.2.15.2.3.1 Type <Tp>"]
file_pages: [705]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.3.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 705 to 705.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 705

```text
CreditorReferenceInformation <CdtrRefInf> contains the following CreditorReferenceInformation3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  705
     CodeOrProprietary <CdOrPrtry> [1..1]  705
{Or       Code <Cd> [1..1] CodeSet 705
Or}       Proprietary <Prtry> [1..1] Text 705
     Issuer <Issr> [0..1] Text 706
   Reference <Ref> [0..1] Text 706
4.4.2.14.18.2.15.2.3.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of creditor reference.
Type <Tp> contains the following CreditorReferenceType3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  705
{Or     Code <Cd> [1..1] CodeSet 705
Or}     Proprietary <Prtry> [1..1] Text 705
   Issuer <Issr> [0..1] Text 706
4.4.2.14.18.2.15.2.3.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format creditor reference type.
CodeOrProprietary <CdOrPrtry> contains one of the following CreditorReferenceType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 705
Or}   Proprietary <Prtry> [1..1] Text 705
4.4.2.14.18.2.15.2.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of creditor reference, as published in an external creditor reference type code set.
Datatype: "ExternalCreditorReferenceType1Code" on page 896
4.4.2.14.18.2.15.2.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
705 March 2026
```

