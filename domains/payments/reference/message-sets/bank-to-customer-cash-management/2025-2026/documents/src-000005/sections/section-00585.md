---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.5 Balance", "6.1.5.2 BalanceType13", "6.1.5.2.2 SubType <SubTp>", "6.1.5.2.2.1 Code <Cd>"]
file_pages: [818]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.5.2.2.1 Code <Cd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 818 to 818.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 818

```text
Definition: Specifies the balance sub-type.
SubType <SubTp> contains one of the following BalanceSubType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 818
Or}   Proprietary <Prtry> [1..1] Text 818
6.1.5.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Balance sub-type, as published in an external balance sub-type code list.
Datatype: "ExternalBalanceSubType1Code" on page 893
6.1.5.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a proprietary code for the balance type.
Datatype: "Max35Text" on page 916
6.1.5.3  CashBalance8
Definition: Set of elements used to define the balance details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 818
   CreditLine <CdtLine> [0..*] ± 819
   Amount <Amt> [1..1] Amount C1, C5 819
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 820
   Date <Dt> [1..1] ± 820
   Availability <Avlbty> [0..*] ± 820
Constraints
• ForwardBalanceAndAvailabilityRule
If Type is equal to ForwardAvailable, Availability is not allowed.
6.1.5.3.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the nature of a balance.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
818 March 2026
```

