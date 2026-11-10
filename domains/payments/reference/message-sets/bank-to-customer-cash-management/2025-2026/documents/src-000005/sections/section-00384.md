---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.12 Interest <Intrst>", "4.4.2.12.1 Type <Tp>", "4.4.2.12.1.1 Code <Cd>"]
file_pages: [569]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.12.1.1 Code <Cd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 569 to 569.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 569

```text
Type <Tp> contains one of the following InterestType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 569
Or}   Proprietary <Prtry> [1..1] Text 569
4.4.2.12.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the type of interest.
Datatype: "InterestType1Code" on page 901
CodeName Name Definition
INDY IntraDay During or within a business day.
OVRN OverNight Period of time between the end of a
business day and the start of the next
business day (usually the day after).
4.4.2.12.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the type of interest in uncoded form.
Datatype: "Max35Text" on page 916
4.4.2.12.2  Rate <Rate>
Presence: [0..*]
Definition: Set of elements used to qualify the interest rate.
Rate <Rate> contains the following Rate4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 569
   ValidityRange <VldtyRg> [0..1] ± 569
4.4.2.12.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of interest rate.
Type <Tp> contains one of the following elements (see "RateType4Choice" on page 881 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Percentage <Pctg> [1..1] Rate 881
Or}   Other <Othr> [1..1] Text 881
4.4.2.12.2.2  ValidityRange <VldtyRg>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
569 March 2026
```

