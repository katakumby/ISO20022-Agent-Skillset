---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.28 TaxValuationPoint <TaxValtnPt>"]
file_pages: [1288]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.28 TaxValuationPoint <TaxValtnPt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1288 to 1288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1288

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
36.4.15.11.28  TaxValuationPoint <TaxValtnPt>
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
36.4.15.11.29  SettlementPartiesDetails <SttlmPtiesDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1288 May 2026
```

