---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.7 Charges <Chrgs>", "2.4.2.15.18.2.7.2 Record <Rcrd>", "2.4.2.15.18.2.7.2.3 ChargeIncludedIndicator <ChrgInclInd>"]
file_pages: [129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.7.2.3 ChargeIncludedIndicator <ChrgInclInd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 129 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
2.4.2.15.18.2.7.2.3  ChargeIncludedIndicator <ChrgInclInd>
Presence: [0..1]
Definition: Indicates whether the charge should be included in the amount or is added as pre-advice.
Datatype: One of the following values must be used (see "ChargeIncludedIndicator" on page 911):
• Meaning When True: Included
• Meaning When False: Pre-advised
2.4.2.15.18.2.7.2.4  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of charge.
Type <Tp> contains one of the following ChargeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 129
Or}   Proprietary <Prtry> [1..1] ± 129
2.4.2.15.18.2.7.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Charge type, in a coded form.
Datatype: "ExternalChargeType1Code" on page 895
2.4.2.15.18.2.7.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of charge in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 838 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 839
   Issuer <Issr> [0..1] Text 839
2.4.2.15.18.2.7.2.5  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charge or fee.
Datatype: "PercentageRate" on page 913
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
129 March 2026
```

