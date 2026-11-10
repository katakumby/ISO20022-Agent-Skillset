---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.10 MovementDetails <MvmntDtls>", "74.4.3.4.10.5 SettlementQuantity <SttlmQty>"]
file_pages: [2634]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.10.5 SettlementQuantity <SttlmQty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2634 to 2634.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2634

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CallableIndicator <CllblInd> [0..1] Indicator 2942
   PutableIndicator <PutblInd> [0..1] Indicator 2942
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 2942
   ExercisePrice <ExrcPric> [0..1] ± 2943
   SubscriptionPrice <SbcptPric> [0..1] ± 2943
   ConversionPrice <ConvsPric> [0..1] ± 2943
   StrikePrice <StrkPric> [0..1] ± 2943
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 2944
   ContractSize <CtrctSz> [0..1] ± 2944
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C3, C4,
C5, C6,
C7
2944
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 2945
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
74.4.3.4.10.5  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
74.4.3.4.10.6  SettledQuantity <SttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument effectively settled.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2634 August 2026
```

