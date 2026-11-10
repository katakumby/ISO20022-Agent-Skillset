---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.2 Account Identification", "17.1.2.1 AccountIdentification4Choice", "17.1.2.1.2 Other <Othr>"]
file_pages: [392]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.2.1.2 Other <Othr>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 392 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 392

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
17.1.2.1.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 389 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 389
   SchemeName <SchmeNm> [0..1]  390
{Or     Code <Cd> [1..1] CodeSet 390
Or}     Proprietary <Prtry> [1..1] Text 390
   Issuer <Issr> [0..1] Text 390
17.1.3 Amount
17.1.3.1  Amount2Choice
Definition: Choice between an amount with or without the currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
17.1.3.1.1  AmountWithoutCurrency <AmtWthtCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context.
Datatype: "ImpliedCurrencyAndAmount" on page 474
17.1.3.1.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is explicit.
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 473
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
392 March 2024
```

