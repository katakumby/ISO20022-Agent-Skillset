---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>", "10.4.4.17 RemainingAmountToBeSettled <RmngAmtToBeSttld>"]
file_pages: [314, 315]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.4.17 RemainingAmountToBeSettled <RmngAmtToBeSttld>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 314 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
SettlementAmount <SttlmAmt> contains the following elements (see AmountAndDirection27 on
page 379 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C1,
  'C7
379
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 380
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount   'C2,
  'C6
380
   ForeignExchangeDetails <FXDtls> [0..1] ± 381
10.4.4.17  RemainingAmountToBeSettled <RmngAmtToBeSttld>
Presence: [0..1]
Definition: Provides the remaining amount to be settled.
RemainingAmountToBeSettled <RmngAmtToBeSttld> contains the following elements (see
AmountAndDirection27 on page 379 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C1,
  'C7
379
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 380
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount   'C2,
  'C6
380
   ForeignExchangeDetails <FXDtls> [0..1] ± 381
10.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C13 SupplementaryDataRule
SupplementaryData <SplmtryData> contains the following elements (see SupplementaryData1 on
page 440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 441
   Envelope <Envlp> [1..1] (External Schema) 441
Constraints
• SupplementaryDataRule
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 314
```

## File page 315

```text
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 315
```

