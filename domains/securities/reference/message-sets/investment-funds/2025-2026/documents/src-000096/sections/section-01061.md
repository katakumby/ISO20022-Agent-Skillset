---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.4 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "39.4.15.4.1 LineIdentification <LineId>"]
file_pages: [1468]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.4.1 LineIdentification <LineId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1468 to 1468.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1468

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1487
   AdditionalInformation <AddtlInf> [0..*] ± 1487
39.4.15.4.1  LineIdentification <LineId>
Presence: [0..1]
Definition: Identification of the line of holding in the portfolio.
Datatype: "Max35Text" on page 5403
39.4.15.4.2  Instrument <Instrm>
Presence: [1..1]
Definition: Identification of the asset.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1468 May 2026
```

