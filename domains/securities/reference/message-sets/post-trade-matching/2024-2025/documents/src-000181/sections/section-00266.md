---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.1 FutureAndOptionContractType <FutrAndOptnCtrctTp>"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.1 FutureAndOptionContractType <FutrAndOptnCtrctTp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a
time in the future.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FutureAndOptionContractType <FutrAndOptnCtrctTp> [0..1] CodeSet 324
   LastDeliveryDate <LastDlvryDt> [0..1] DateTime 325
   UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 325
   FutureDate <FutrDt> [0..1] DateTime 326
   MinimumSize <MinSz> [0..1] Amount C1, C9 326
   AnnouncementDate <AnncmntDt> [0..1] DateTime 327
   Appearance <Apprnc> [0..1] CodeSet 327
   StrippableIndicator <StrpblInd> [0..1] Indicator 327
   PositionLimit <PosLmt> [0..1] Quantity 327
   NearTermPositionLimit <NearTermPosLmt> [0..1] Quantity 328
   MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 328
   Purpose <Purp> [0..1] Text 328
   ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 328
   FirstDealingDate <FrstDealgDt> [0..1] ± 328
   Ratio <Ratio> [0..*] ± 328
   Rating <Ratg> [0..*] ± 329
   IssuePrice <IssePric> [0..1] ± 329
   OptionRights <OptnRghts> [0..1] ± 329
   LastTransaction <LastTx> [0..1] Indicator 330
   SpreadTransaction <SprdTx> [0..1] Indicator 330
7.1.19.35.1  FutureAndOptionContractType <FutrAndOptnCtrctTp>
Presence: [0..1]
Definition: Specifies the type of the contract for futures and options.
Datatype: "FutureAndOptionContractType1Code" on page 628
CodeName Name Definition
ORDY Ordinary Ordinary future and option contract.
INDX Index Future and option contract on an index
as opposed to an underlying equity.
EXFU ExercisedFuture Receipt of future contract when an
option on a future is exercised.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 324 February 2025
```

