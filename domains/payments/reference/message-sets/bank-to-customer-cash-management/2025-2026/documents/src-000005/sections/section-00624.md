---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.9 YieldedOrValueType1Choice", "6.1.15.9.1 Yielded <Yldd>"]
file_pages: [857]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.9.1 Yielded <Yldd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 857 to 857.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 857

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 857
Or}   ValueType <ValTp> [1..1] CodeSet 857
6.1.15.9.1  Yielded <Yldd>
Presence: [1..1]
Definition: Indicates whether the price is expressed as a yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 911):
• Meaning When True: Yes
• Meaning When False: No
6.1.15.9.2  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType1Code" on page 903
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
6.1.15.10  NumberAndSumOfTransactions1
Definition: Set of elements providing the total sum of entries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 857
   Sum <Sum> [0..1] Quantity 857
6.1.15.10.1  NumberOfEntries <NbOfNtries>
Presence: [0..1]
Definition: Number of individual entries included in the report.
Datatype: "Max15NumericText" on page 915
6.1.15.10.2  Sum <Sum>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
857 March 2026
```

