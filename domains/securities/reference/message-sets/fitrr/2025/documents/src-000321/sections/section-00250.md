---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.26 AssetClassCommodity3Choice", "22.1.2.26.8 OtherC10 <OthrC10>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.26.8 OtherC10 <OthrC10>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
22.1.2.26.8  OtherC10 <OthrC10>
Presence: [1..1]
Definition: Other C10 commodities.
OtherC10 <OthrC10> contains one of the following elements (see
"AssetClassCommodityOtherC102Choice" on page 286 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Deliverable <Dlvrbl> [1..1]  286
     BaseProduct <BasePdct> [1..1] CodeSet 287
     SubProduct <SubPdct> [0..1] CodeSet 287
Or}   NonDeliverable <NonDlvrbl> [1..1]  287
     BaseProduct <BasePdct> [1..1] CodeSet 287
     SubProduct <SubPdct> [0..1] CodeSet 288
22.1.2.26.9  Paper <Ppr>
Presence: [1..1]
Definition: Paper commodities.
Paper <Ppr> contains one of the following elements (see "AssetClassCommodityPaper1Choice" on
page 312 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ContainerBoard <CntnrBrd> [1..1]  312
     BaseProduct <BasePdct> [1..1] CodeSet 312
     SubProduct <SubPdct> [0..1] CodeSet 312
Or   Newsprint <Nwsprnt> [1..1]  313
     BaseProduct <BasePdct> [1..1] CodeSet 313
     SubProduct <SubPdct> [0..1] CodeSet 313
Or   Pulp <Pulp> [1..1]  313
     BaseProduct <BasePdct> [1..1] CodeSet 313
     SubProduct <SubPdct> [0..1] CodeSet 314
Or}   RecoveredPaper <RcvrdPpr> [1..1]  314
     BaseProduct <BasePdct> [1..1] CodeSet 314
     SubProduct <SubPdct> [0..1] CodeSet 314
22.1.2.26.10  Polypropylene <Plprpln>
Presence: [1..1]
Definition: Polypropylene commodities.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
300 July 2025
```

