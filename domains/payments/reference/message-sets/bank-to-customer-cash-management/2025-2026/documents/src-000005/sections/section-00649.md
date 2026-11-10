---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.23 Securities Quantity", "6.1.23.1 OriginalAndCurrentQuantities1", "6.1.23.1.1 FaceAmount <FaceAmt>"]
file_pages: [882]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.23.1.1 FaceAmount <FaceAmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 882 to 882.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 882

```text
6.1.23.1.1  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 886
6.1.23.1.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 886
6.1.24 Status
6.1.24.1  EntryStatus1Choice
Definition: Specifies the status of an entry on the books of the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 882
Or}   Proprietary <Prtry> [1..1] Text 882
6.1.24.1.1  Code <Cd>
Presence: [1..1]
Definition: Entry status, in a coded form.
Datatype: "ExternalEntryStatus1Code" on page 897
6.1.24.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Entry status, in a proprietary form.
Datatype: "Max35Text" on page 916
6.1.25 System Identification
6.1.25.1  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 883
Or}   Proprietary <Prtry> [1..1] Text 883
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
882 March 2026
```

