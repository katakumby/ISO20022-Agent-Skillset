---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount"]
file_pages: [802]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3 Amount

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 802 to 802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 802

```text
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 799 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 799
   SchemeName <SchmeNm> [0..1]  799
{Or     Code <Cd> [1..1] CodeSet 800
Or}     Proprietary <Prtry> [1..1] Text 800
   Issuer <Issr> [0..1] Text 800
6.1.3 Amount
6.1.3.1  AmountAndCurrencyExchange4
Definition: Set of elements used to provide information on the original amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructedAmount <InstdAmt> [0..1] ± 802
   TransactionAmount <TxAmt> [0..1] ± 803
   CounterValueAmount <CntrValAmt> [0..1] ± 803
   AnnouncedPostingAmount <AnncdPstngAmt> [0..1] ± 804
   ProprietaryAmount <PrtryAmt> [0..*] ± 804
6.1.3.1.1  InstructedAmount <InstdAmt>
Presence: [0..1]
Definition: Identifies the amount of money to be moved between the debtor and creditor, before
deduction of charges, expressed in the currency as ordered by the initiating party and provides currency
exchange information in case the instructed amount and/or currency is/are different from the entry
amount and/or currency.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
802 March 2026
```

