---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.4 CorporateActionDetails <CorpActnDtls>", "11.4.4.1 DateDetails <DtDtls>"]
file_pages: [713]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.4.1 DateDetails <DtDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 713 to 713.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 713

```text
CorporateActionDetails <CorpActnDtls> contains the following CorporateAction72 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateDetails <DtDtls> [0..1]  713
     RecordDate <RcrdDt> [0..1] ± 713
     ExDividendDate <ExDvddDt> [0..1] ± 713
   EventStage <EvtStag> [0..1] ± 714
   AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 714
   LotteryType <LtryTp> [0..1] ± 714
11.4.4.1  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action event.
DateDetails <DtDtls> contains the following CorporateActionDate86 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RecordDate <RcrdDt> [0..1] ± 713
   ExDividendDate <ExDvddDt> [0..1] ± 713
11.4.4.1.1  RecordDate <RcrdDt>
Presence: [0..1]
Definition: Date/time at which positions are struck at the end of the day to note which parties will receive
the relevant amount of entitlement, due to be distributed on payment date.
RecordDate <RcrdDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
11.4.4.1.2  ExDividendDate <ExDvddDt>
Presence: [0..1]
Definition: Date/time as from which trading (including exchange and OTC trading) occurs on the
underlying security without the benefit.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 713 February 2026
```

