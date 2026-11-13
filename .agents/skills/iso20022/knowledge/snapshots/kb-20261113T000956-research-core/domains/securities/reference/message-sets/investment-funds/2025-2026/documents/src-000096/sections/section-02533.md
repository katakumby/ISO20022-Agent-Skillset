---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.9 TransactionOverhead <TxOvrhd>", "53.4.5.16.9.2 IndividualFee <IndvFee>", "53.4.5.16.9.2.2 Basis <Bsis>", "53.4.5.16.9.2.2.1 Code <Cd>"]
file_pages: [3570]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.9.2.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3570 to 3570.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3570

```text
Basis <Bsis> contains one of the following ChargeBasis2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3570
Or}   Proprietary <Prtry> [1..1] ± 3570
53.4.5.16.9.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Fee (charge/commission) basis expressed as a code.
Datatype: "TaxationBasis5Code" on page 5366
CodeName Name Definition
FLAT Flat Charge/tax basis is a lump sum.
GRAM GrossAmount Charge/Commission/tax basis is based
on the gross amount.
NEAM NetAmount Charge/commission/tax basis is based
on the net amount.
NAVP NetAssetValuePrice Charge/tax basis is the price.
PERU PerUnit Charges/tax basis is per unit of financial
instrument.
53.4.5.16.9.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Fee (charge/commission) basis expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
53.4.5.16.9.2.3  StandardAmount <StdAmt>
Presence: [0..1]
Definition: Standard fee (charge/commission) amount as specified in the fund prospectus or agreed for
the account.
Impacted by: C2 "ActiveCurrency", C7 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3570 May 2026
```

