---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.10 MovementDetails <MvmntDtls>", "3.4.3.4.10.5 SettlementQuantity <SttlmQty>"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.10.5 SettlementQuantity <SttlmQty>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CallableIndicator <CllblInd> [0..1] Indicator 217
   PutableIndicator <PutblInd> [0..1] Indicator 217
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 217
   ExercisePrice <ExrcPric> [0..1] ± 218
   SubscriptionPrice <SbcptPric> [0..1] ± 218
   ConversionPrice <ConvsPric> [0..1] ± 218
   StrikePrice <StrkPric> [0..1] ± 218
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 219
   ContractSize <CtrctSz> [0..1] ± 219
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C8, C9,
C11,
C12,
C14
219
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 220
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
3.4.3.4.10.5  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 221
Or   FaceAmount <FaceAmt> [1..1] Amount 221
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 221
3.4.3.4.10.6  SettledQuantity <SttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument effectively settled.
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 79 September 2025
```

