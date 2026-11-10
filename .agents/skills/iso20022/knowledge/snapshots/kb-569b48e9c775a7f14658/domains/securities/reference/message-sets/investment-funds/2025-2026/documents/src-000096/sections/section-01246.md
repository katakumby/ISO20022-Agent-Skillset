---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.15 TransactionOverhead <TxOvrhd>", "41.4.4.8.15.2 IndividualFee <IndvFee>", "41.4.4.8.15.2.2 Basis <Bsis>", "41.4.4.8.15.2.2.1 Code <Cd>"]
file_pages: [1751]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.15.2.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1751 to 1751.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1751

```text
Basis <Bsis> contains one of the following ChargeBasis2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1751
Or}   Proprietary <Prtry> [1..1] ± 1751
41.4.4.8.15.2.2.1  Code <Cd>
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
41.4.4.8.15.2.2.2  Proprietary <Prtry>
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
41.4.4.8.15.2.3  StandardAmount <StdAmt>
Presence: [0..1]
Definition: Standard fee (charge/commission) amount as specified in the fund prospectus or agreed for
the account.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1751 May 2026
```

