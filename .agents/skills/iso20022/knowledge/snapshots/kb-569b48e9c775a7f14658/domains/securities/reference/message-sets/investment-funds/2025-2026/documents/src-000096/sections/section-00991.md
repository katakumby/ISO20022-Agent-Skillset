---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.1 LineIdentification <LineId>"]
file_pages: [1378]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.1 LineIdentification <LineId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1378 to 1378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1378

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C32,
C33,
C34,
C35,
C40
       Depository <Dpstry> [0..1] ± 1432
       Party1 <Pty1> [0..1] ± 1433
       Party2 <Pty2> [0..1] ± 1433
       Party3 <Pty3> [0..1] ± 1434
       Party4 <Pty4> [0..1] ± 1434
       Party5 <Pty5> [0..1] ± 1435
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C17,
C32,
C33,
C34,
C35,
C40
1435
       Depository <Dpstry> [0..1] ± 1437
       Party1 <Pty1> [0..1] ± 1438
       Party2 <Pty2> [0..1] ± 1438
       Party3 <Pty3> [0..1] ± 1438
       Party4 <Pty4> [0..1] ± 1439
       Party5 <Pty5> [0..1] ± 1439
   AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1440
   TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1440
   AdditionalInformation <AddtlInf> [0..*] ± 1440
Constraints
• AssetQuantity1Guideline
If Instrument/Security is present, then Quantity/Unit or Quantity/FaceAmount or Quantity/
AmortisedValue must be present.
• AssetQuantity2Guideline
If Instrument/CashAsset is present, then Quantity/CashAmount must be present.
38.4.15.8.1  LineIdentification <LineId>
Presence: [0..1]
Definition: Identification of the line of holding in the portfolio.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1378 May 2026
```

