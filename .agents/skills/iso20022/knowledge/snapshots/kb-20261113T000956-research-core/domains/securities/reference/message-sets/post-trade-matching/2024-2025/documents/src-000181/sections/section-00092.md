---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.15 ClearingDetails <ClrDtls>", "3.4.15.2 ClearingSegment <ClrSgmt>"]
file_pages: [122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.15.2 ClearingSegment <ClrSgmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 122 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 122

```text
3.4.15.2  ClearingSegment <ClrSgmt>
Presence: [0..1]
Definition: Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, Clearing Member Firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
ClearingSegment <ClrSgmt> contains one of the following elements (see
"PartyIdentification127Choice" on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 390
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 390
3.4.16 SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities. The amount
includes the principal with any commissions and fees or accrued interest.
SettlementAmount <SttlmAmt> contains the following AmountAndDirection28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 122
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 122
   Amount <Amt> [1..1] Amount C1, C13 123
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 123
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C14 123
   ForeignExchangeDetails <FXDtls> [0..1] ± 124
   ValueDate <ValDt> [0..1] ± 124
3.4.16.1  AccruedInterestIndicator <AcrdIntrstInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include interest accrued on the financial instrument.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.16.2  StampDutyIndicator <StmpDtyInd>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 122 February 2025
```

