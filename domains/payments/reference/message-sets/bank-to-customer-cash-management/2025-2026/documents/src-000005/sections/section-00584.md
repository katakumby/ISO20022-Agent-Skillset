---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.5 Balance", "6.1.5.2 BalanceType13"]
file_pages: [817]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.5.2 BalanceType13

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 817 to 817.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 817

```text
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 826 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 826
Or}   DateTime <DtTm> [1..1] DateTime 826
6.1.5.2  BalanceType13
Definition: Set of elements used to define the balance type and sub-type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  817
{Or     Code <Cd> [1..1] CodeSet 817
Or}     Proprietary <Prtry> [1..1] Text 817
   SubType <SubTp> [0..1]  817
{Or     Code <Cd> [1..1] CodeSet 818
Or}     Proprietary <Prtry> [1..1] Text 818
6.1.5.2.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format balance type.
CodeOrProprietary <CdOrPrtry> contains one of the following BalanceType10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 817
Or}   Proprietary <Prtry> [1..1] Text 817
6.1.5.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Balance type, in a coded format.
Datatype: "ExternalBalanceType1Code" on page 893
6.1.5.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Balance type, in a proprietary format.
Datatype: "Max35Text" on page 916
6.1.5.2.2  SubType <SubTp>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
817 March 2026
```

