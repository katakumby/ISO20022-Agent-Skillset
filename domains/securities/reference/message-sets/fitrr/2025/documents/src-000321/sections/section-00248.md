---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.26 AssetClassCommodity3Choice", "22.1.2.26.3 Environmental <Envttl>"]
file_pages: [298]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.26.3 Environmental <Envttl>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 298 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
Definition: Energy commodities.
Energy <Nrgy> contains one of the following elements (see "AssetClassCommodityEnergy1Choice" on
page 305 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Electricity <Elctrcty> [1..1] ± 306
Or   NaturalGas <NtrlGas> [1..1] ± 306
Or   Oil <Oil> [1..1] ± 306
Or   Coal <Coal> [1..1] ± 306
Or   InterEnergy <IntrNrgy> [1..1] ± 307
Or   RenewableEnergy <RnwblNrgy> [1..1] ± 307
Or   LightEnd <LghtEnd> [1..1] ± 307
Or}   Distillates <Dstllts> [1..1] ± 307
22.1.2.26.3  Environmental <Envttl>
Presence: [1..1]
Definition: Environmental commodities.
Environmental <Envttl> contains one of the following elements (see
"AssetClassCommodityEnvironmental1Choice" on page 291 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Emissions <Emssns> [1..1] ± 291
Or   Weather <Wthr> [1..1] ± 292
Or}   CarbonRelated <CrbnRltd> [1..1] ± 292
22.1.2.26.4  Fertilizer <Frtlzr>
Presence: [1..1]
Definition: Fertilizer commodities.
Fertilizer <Frtlzr> contains one of the following elements (see
"AssetClassCommodityFertilizer1Choice" on page 292 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Ammonia <Ammn> [1..1] ± 293
Or   DiammoniumPhosphate <DmmnmPhspht> [1..1] ± 293
Or   Potash <Ptsh> [1..1] ± 293
Or   Sulphur <Slphr> [1..1] ± 293
Or   Urea <Urea> [1..1] ± 294
Or}   UreaAndAmmoniumNitrate <UreaAndAmmnmNtrt> [1..1] ± 294
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
298 July 2025
```

