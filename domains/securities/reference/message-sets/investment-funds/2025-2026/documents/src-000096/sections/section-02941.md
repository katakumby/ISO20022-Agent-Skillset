---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>"]
file_pages: [4127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4127 to 4127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4127

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  4199
             Identification <Id> [1..1] Text 4200
             IdentificationSource <IdSrc> [1..1] ± 4200
         Name <Nm> [0..1] Text 4200
         ShortName <ShrtNm> [0..1] Text 4200
         SupplementaryIdentification <SplmtryId> [0..1] Text 4200
         ClassType <ClssTp> [0..1] Text 4200
         SecuritiesForm <SctiesForm> [0..1] CodeSet 4201
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4201
         ProductGroup <PdctGrp> [0..1] Text 4201
         SeriesIdentification <SrsId> [0..1]  C19 4201
           SeriesDate <SrsDt> [0..1] ± 4202
           SeriesName <SrsNm> [0..1] Text 4202
     StatusInitiator <StsInitr> [0..1] ± 4202
     OrderData <OrdrData> [0..1] ± C20 4202
     NewDetails <NewDtls> [0..1]  4203
       ExpectedTradeDateTime <XpctdTradDtTm> [0..1] ± 4203
       ExpectedCashSettlementDate <XpctdCshSttlmDt> [0..1] Date 4203
56.4.3.1  OrderDetailsReport <OrdrDtlsRpt>
Presence: [1..1]
Definition: Status report details of all the individual orders conveyed in a bulk or multiple order message.
Can be used if all the individual orders conveyed in a bulk or multiple order message have the same
status.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4127 May 2026
```

