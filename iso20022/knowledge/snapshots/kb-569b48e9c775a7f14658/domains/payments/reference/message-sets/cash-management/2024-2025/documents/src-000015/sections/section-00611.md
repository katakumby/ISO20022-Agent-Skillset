---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.2 Account Identification", "37.1.2.1 AccountIdentification4Choice", "37.1.2.1.2 Other <Othr>"]
file_pages: [788]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.2.1.2 Other <Othr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 788 to 788.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 788

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
37.1.2.1.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 786 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 786
   SchemeName <SchmeNm> [0..1]  786
{Or     Code <Cd> [1..1] CodeSet 787
Or}     Proprietary <Prtry> [1..1] Text 787
   Issuer <Issr> [0..1] Text 787
37.1.3 Amount
37.1.3.1  Amount2Choice
Definition: Choice between an amount with or without the currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
37.1.3.1.1  AmountWithoutCurrency <AmtWthtCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context.
Datatype: "ImpliedCurrencyAndAmount" on page 848
37.1.3.1.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is explicit.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 847
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 788 February 2025
```

