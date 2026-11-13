---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.7 Charges <Chrgs>", "4.4.2.14.18.2.7.2 Record <Rcrd>", "4.4.2.14.18.2.7.2.3 ChargeIncludedIndicator <ChrgInclInd>"]
file_pages: [647]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.7.2.3 ChargeIncludedIndicator <ChrgInclInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 647 to 647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 647

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
4.4.2.14.18.2.7.2.3  ChargeIncludedIndicator <ChrgInclInd>
Presence: [0..1]
Definition: Indicates whether the charge should be included in the amount or is added as pre-advice.
Datatype: One of the following values must be used (see "ChargeIncludedIndicator" on page 911):
• Meaning When True: Included
• Meaning When False: Pre-advised
4.4.2.14.18.2.7.2.4  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of charge.
Type <Tp> contains one of the following ChargeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 647
Or}   Proprietary <Prtry> [1..1] ± 647
4.4.2.14.18.2.7.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Charge type, in a coded form.
Datatype: "ExternalChargeType1Code" on page 895
4.4.2.14.18.2.7.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of charge in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 838 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 839
   Issuer <Issr> [0..1] Text 839
4.4.2.14.18.2.7.2.5  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charge or fee.
Datatype: "PercentageRate" on page 913
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
647 March 2026
```

