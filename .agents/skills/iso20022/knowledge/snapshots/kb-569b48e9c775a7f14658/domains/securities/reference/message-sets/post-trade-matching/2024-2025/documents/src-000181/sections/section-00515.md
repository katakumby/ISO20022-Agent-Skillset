---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.6 RejectionReason52Choice", "7.1.28.6.2 Proprietary <Prtry>"]
file_pages: [592]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.6.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 592 to 592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

```text
CodeName Name Definition
trade amount, etc., values that differ
from the buy-side's calculations. Buy-
side may reject the trade if they feel that
the difference in calculations is too high.
CPTY UnknownDealExposure Deal or exposure is unknown.
DISC DisagreeWithCallAmount Party does not agree with the call
amount.
DISE DisagreeWithExposureAmount Party does not agree with the exposure
amount.
RESU MissingResultingAmount Resulting amount must be filled in as
exchange rate is present.
XRAT MissingExchangeRate Resulting amount is not allowed without
an exchange rate.
ACRU UnexpectedAccruedInterest Accrued interest is not applicable for this
type of security.
GAMN GrossAmountLessThanNetAmount Gross amount is less than net amount.
DFLT MissingDefaultOption One option must be marked as the
default.
FAIL FailedValidation Validation of the advice/instruction/
request failed.
INDT InvalidDetails Message details specified in the
instruction/request are inconsistent with
those that were specified in the relating
original message.
OTHR Other Other. See Narrative.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
7.1.28.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.7  MatchingReason6Choice
Definition: Choice of format for the matching processing status.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 592 February 2025
```

