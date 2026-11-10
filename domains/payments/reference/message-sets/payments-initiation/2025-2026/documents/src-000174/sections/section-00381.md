---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.2 Account Identification", "6.1.2.1 AccountIdentification4Choice", "6.1.2.1.2 Other <Othr>"]
file_pages: [532]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.2.1.2 Other <Othr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 532 to 532.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 532

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
6.1.2.1.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 530 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 530
   SchemeName <SchmeNm> [0..1]  530
{Or     Code <Cd> [1..1] CodeSet 531
Or}     Proprietary <Prtry> [1..1] Text 531
   Issuer <Issr> [0..1] Text 531
6.1.3 Amount
6.1.3.1  AmountType4Choice
Definition: Specifies the amount of money to be moved between the debtor and creditor, before
deduction of charges, expressed in the currency as ordered by the initiating party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructedAmount <InstdAmt> [1..1] Amount C2, C19 532
Or}   EquivalentAmount <EqvtAmt> [1..1]  533
     Amount <Amt> [1..1] Amount C2, C19 533
     CurrencyOfTransfer <CcyOfTrf> [1..1] CodeSet C2 533
6.1.3.1.1  InstructedAmount <InstdAmt>
Presence: [1..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
Impacted by: C2 "ActiveOrHistoricCurrency", C19 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 532 March 2026
```

