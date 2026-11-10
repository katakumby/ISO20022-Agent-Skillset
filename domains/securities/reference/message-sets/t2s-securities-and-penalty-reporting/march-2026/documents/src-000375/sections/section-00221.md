---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.3 SubAccountDetails <SubAcctDtls>", "7.1.5.14.3.4 BalanceForSubAccount <BalForSubAcct>", "7.1.5.14.3.4.4 InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>"]
file_pages: [297]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.3.4.4 InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 297 to 297.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 297

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 333
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 333
   ExercisePrice <ExrcPric> [0..1] ± 333
   SubscriptionPrice <SbcptPric> [0..1] ± 334
   ConversionPrice <ConvsPric> [0..1] ± 334
   StrikePrice <StrkPric> [0..1] ± 334
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 334
   ContractSize <CtrctSz> [0..1] ± 335
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C4, C5,
C7, C8,
C9
335
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 336
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and a ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
7.1.5.14.3.4.4  InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising an investment funds financial instrument.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 297 March 2026
```

