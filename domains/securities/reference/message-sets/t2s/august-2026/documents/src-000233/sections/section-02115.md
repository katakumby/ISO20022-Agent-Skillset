---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.2 BalanceForAccount <BalForAcct>", "82.1.5.16.2.4 InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>"]
file_pages: [2873]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.2.4 InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2873 to 2873.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2873

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 2931
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 2931
   ExercisePrice <ExrcPric> [0..1] ± 2931
   SubscriptionPrice <SbcptPric> [0..1] ± 2932
   ConversionPrice <ConvsPric> [0..1] ± 2932
   StrikePrice <StrkPric> [0..1] ± 2932
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 2932
   ContractSize <CtrctSz> [0..1] ± 2933
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C3, C4,
C5, C6,
C7
2933
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 2934
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and a ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
82.1.5.16.2.4  InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising an investment funds financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2873 August 2026
```

