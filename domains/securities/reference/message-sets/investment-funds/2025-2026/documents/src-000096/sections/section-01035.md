---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.18 SettlementPartiesDetails <SttlmPtiesDtls>"]
file_pages: [1428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.18 SettlementPartiesDetails <SttlmPtiesDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1428 to 1428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1428

```text
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
38.4.15.8.18  SettlementPartiesDetails <SttlmPtiesDtls>
Presence: [0..*]
Definition: Chain of parties involved in the settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1428 May 2026
```

