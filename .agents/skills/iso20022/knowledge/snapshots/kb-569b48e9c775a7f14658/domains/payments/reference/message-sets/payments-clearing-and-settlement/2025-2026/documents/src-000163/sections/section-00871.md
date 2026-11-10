---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.2 Account Identification", "10.1.2.1 AccountIdentification4Choice", "10.1.2.1.2 Other <Othr>"]
file_pages: [1166]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.2.1.2 Other <Othr>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1166 to 1166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1166

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
10.1.2.1.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 1164 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1164
   SchemeName <SchmeNm> [0..1]  1164
{Or     Code <Cd> [1..1] CodeSet 1165
Or}     Proprietary <Prtry> [1..1] Text 1165
   Issuer <Issr> [0..1] Text 1165
10.1.3 Amount
10.1.3.1  AmountType4Choice
Definition: Specifies the amount of money to be moved between the debtor and creditor, before
deduction of charges, expressed in the currency as ordered by the initiating party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructedAmount <InstdAmt> [1..1] Amount C2, C12 1166
Or}   EquivalentAmount <EqvtAmt> [1..1]  1167
     Amount <Amt> [1..1] Amount C2, C12 1167
     CurrencyOfTransfer <CcyOfTrf> [1..1] CodeSet C2 1167
10.1.3.1.1  InstructedAmount <InstdAmt>
Presence: [1..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1166 March 2026
```

