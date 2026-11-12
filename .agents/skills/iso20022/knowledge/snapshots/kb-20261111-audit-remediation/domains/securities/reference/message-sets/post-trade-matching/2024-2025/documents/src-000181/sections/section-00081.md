---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.39 PreFundedIndicator <PreFnddInd>"]
file_pages: [106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.39 PreFundedIndicator <PreFnddInd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 106 to 106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 106

```text
3.4.8.39  PreFundedIndicator <PreFnddInd>
Presence: [0..1]
Definition: Indicates whether an interest bearing instrument is deposited in a fund that will be used to
pay debt service on refunded securities.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.40  EscrowedIndicator <EscrwdInd>
Presence: [0..1]
Definition: Indicates whether an interest bearing instrument is being escrowed or collateralized either by
direct obligations guaranteed by the US government, or by other types of securities. The maturity
schedules of the securities in the escrow fund are determined in such a way to pay the maturity value,
coupon, and premium payments (if any) of the refunded bonds.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.41  PerpetualIndicator <PerptlInd>
Presence: [0..1]
Definition: Indicates whether the security has no maturity date.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.9 ConfirmationParties <ConfPties>
Presence: [1..*]
Definition: Parties involved in the confirmation of the details of a trade.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 106 February 2025
```

