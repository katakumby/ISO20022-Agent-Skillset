---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.16 TransactionOverhead <TxOvrhd>", "50.4.4.9.16.3 IndividualTax <IndvTax>", "50.4.4.9.16.3.7 TaxCalculationDetails <TaxClctnDtls>"]
file_pages: [3088]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.16.3.7 TaxCalculationDetails <TaxClctnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3088 to 3088.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3088

```text
Definition: Party that receives the tax. The recipient of, and the party entitled to, the tax may be two
different parties.
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.9.16.3.7  TaxCalculationDetails <TaxClctnDtls>
Presence: [0..1]
Definition: Information used to calculate the tax.
TaxCalculationDetails <TaxClctnDtls> contains the following TaxCalculationInformation9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Basis <Bsis> [1..1]  3088
{Or     Code <Cd> [1..1] CodeSet 3088
Or}     Proprietary <Prtry> [1..1] ± 3088
50.4.4.9.16.3.7.1  Basis <Bsis>
Presence: [1..1]
Definition: Form of the rebate, for example, cash.
Basis <Bsis> contains one of the following TaxBasis1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3088
Or}   Proprietary <Prtry> [1..1] ± 3088
50.4.4.9.16.3.7.1.1  Code <Cd>
Presence: [1..1]
Definition: Tax basis expressed as a code.
Datatype: "TaxationBasis2Code" on page 5366
CodeName Name Definition
FLAT Flat Charge/tax basis is a lump sum.
PERU PerUnit Charges/tax basis is per unit of financial
instrument.
50.4.4.9.16.3.7.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Tax basis expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3088 May 2026
```

