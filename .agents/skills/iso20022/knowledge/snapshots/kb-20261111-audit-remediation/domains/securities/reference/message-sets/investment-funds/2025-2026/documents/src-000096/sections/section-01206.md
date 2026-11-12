---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.28 TaxValuationPoint <TaxValtnPt>"]
file_pages: [1671]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.28 TaxValuationPoint <TaxValtnPt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1671 to 1671.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1671

```text
CrystallisationDetails <CrstllstnDtls> contains the following elements (see "Crystallisation2" on
page 4766 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TrancheIdentification <TrchId> [1..1] Text 4766
   CrystallisedUnitsNumber <CrstllsdUnitsNb> [0..1] Quantity 4766
   UncrystallisedUnitsNumber <UcrstllsdUnitsNb> [0..1] Quantity 4766
   CrystallisedAmount <CrstllsdAmt> [0..1] Amount C1 4766
   UncrystallisedAmount <UcrstllsdAmt> [0..1] Amount C1 4767
   AdditionalInformation <AddtlInf> [0..*] ± 4767
40.4.15.11.28  TaxValuationPoint <TaxValtnPt>
Presence: [0..1]
Definition: Date or tax quarter used for the calculation of tax on the asset.
TaxValuationPoint <TaxValtnPt> contains the following elements (see "Tax36" on page 4464 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOrPeriod <DtOrPrd> [1..1]  4465
{Or     Date <Dt> [1..1] Date 4465
Or}     Period <Prd> [1..1] Text 4465
   AdditionalInformation <AddtlInf> [0..*] ± 4465
40.4.15.11.29  SettlementPartiesDetails <SttlmPtiesDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1671 May 2026
```

