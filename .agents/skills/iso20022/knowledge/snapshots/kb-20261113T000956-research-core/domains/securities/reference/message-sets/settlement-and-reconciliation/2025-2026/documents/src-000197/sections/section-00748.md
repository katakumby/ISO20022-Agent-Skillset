---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.12 Reporting <Rptg>"]
file_pages: [1114]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.12 Reporting <Rptg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1114 to 1114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1114

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 1453
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 1453
   ExercisePrice <ExrcPric> [0..1] ± 1453
   SubscriptionPrice <SbcptPric> [0..1] ± 1454
   ConversionPrice <ConvsPric> [0..1] ± 1454
   StrikePrice <StrkPric> [0..1] ± 1454
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 1454
   ContractSize <CtrctSz> [0..1] ± C12 1455
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C10,
C11,
C14,
C15,
C16
1455
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 1456
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
31.4.6.12  Reporting <Rptg>
Presence: [0..*]
Definition: Specifies that a trade is to be reported to a third party.
Reporting <Rptg> contains one of the following elements (see "Reporting7Choice" on page 1612 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1612
Or}   Proprietary <Prtry> [1..1] ± 1612
31.4.6.13  QuantityDetails <QtyDtls>
Presence: [1..1]
Definition: Details about the financial instrument quantity involved in the transfer.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1114 March 2026
```

