---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.44 AssetClassCommodityAgricultural1Choice", "22.1.2.44.7 Seafood <Sfd>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.44.7 Seafood <Sfd>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
Definition: Forestry agricultural commodity derivative.
Forestry <Frstry> contains the following elements (see "AgriculturalCommodityForestry1" on page 303
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 303
   SubProduct <SubPdct> [1..1] CodeSet 303
22.1.2.44.7  Seafood <Sfd>
Presence: [1..1]
Definition: Seafood agricultural commodity derivative.
Seafood <Sfd> contains the following elements (see "AgriculturalCommoditySeafood1" on page 296
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 296
   SubProduct <SubPdct> [1..1] CodeSet 296
22.1.2.44.8  LiveStock <LiveStock>
Presence: [1..1]
Definition: Livestock agricultural commodity derivative.
LiveStock <LiveStock> contains the following elements (see "AgriculturalCommodityLiveStock1" on
page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 276
   SubProduct <SubPdct> [1..1] CodeSet 277
22.1.2.44.9  Grain <Grn>
Presence: [1..1]
Definition: Grain agricultural commodity derivative.
Grain <Grn> contains the following elements (see "AgriculturalCommodityGrain1" on page 279 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 279
   SubProduct <SubPdct> [1..1] CodeSet 279
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 280
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
320 July 2025
```

