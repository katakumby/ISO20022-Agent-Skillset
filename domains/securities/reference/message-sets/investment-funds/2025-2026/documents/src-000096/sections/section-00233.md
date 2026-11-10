---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.21 LocalMarketAnnex <LclMktAnx>", "15.4.5.21.1 Country <Ctry>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.21.1 Country <Ctry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
LocalMarketAnnex <LclMktAnx> contains the following LocalMarketAnnex6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..*] CodeSet C6 335
   LocalOrderDesk <LclOrdrDsk> [1..1] ± 336
   SubscriptionProcessingCharacteristics
<SbcptPrcgChrtcs>
[0..1] ± C8 336
   RedemptionProcessingCharacteristics
<RedPrcgChrtcs>
[0..1] ± C11 338
   SwitchProcessingCharacteristics <SwtchPrcgChrtcs> [0..1] ± C10 339
   CashSettlementDetails <CshSttlmDtls> [0..*]  340
     Currency <Ccy> [0..1] CodeSet C1 341
     PrimaryAccount <PmryAcct> [0..1]  341
       AccountIdentification <AcctId> [1..1]  342
         Identification <Id> [1..1] ± 342
         Name <Nm> [0..1] Text 342
       Servicer <Svcr> [0..1] IdentifierSet C2 342
       AccountTypeDescription <AcctTpDesc> [0..1] Text 343
     SecondaryAccount <ScndryAcct> [0..1]  343
       AccountIdentification <AcctId> [1..1]  343
         Identification <Id> [1..1] ± 343
         Name <Nm> [0..1] Text 344
       Servicer <Svcr> [0..1] IdentifierSet C2 344
       AccountTypeDescription <AcctTpDesc> [0..1] Text 344
   AdditionalInformation <AddtlInf> [0..*] ± 344
15.4.5.21.1  Country <Ctry>
Presence: [1..*]
Definition: Country of the local fund order desk.
Impacted by: C6 "Country"
Datatype: "CountryCode" on page 5290
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 335 May 2026
```

