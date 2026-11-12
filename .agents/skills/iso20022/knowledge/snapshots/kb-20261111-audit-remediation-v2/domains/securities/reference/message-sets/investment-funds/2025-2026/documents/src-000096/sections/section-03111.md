---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.8 AccountIdentificationFormatChoice"]
file_pages: [4335]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.8 AccountIdentificationFormatChoice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4335 to 4335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4335

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4382
Constraints
• AccruedInterestAmountSignRule
if AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
• AggregateQuantityGuideline
The AggregateQuantity should be the sum of AvailableQuantity and NotAvailableQuantity if
AvailableQuantity and NotAvailableQuantity are both present.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
66.1.2.8  AccountIdentificationFormatChoice
Definition: Choice between formats for account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SimpleIdentification <SmplId> [1..1] ± 4335
Or   IdentificationAndPurpose <IdAndPurp> [1..1]  4335
     Identification <Id> [1..1] ± 4336
     Purpose <Purp> [1..1] CodeSet 4336
Or}   IdentificationAsDSS <IdAsDSS> [1..1] ± 4336
66.1.2.8.1  SimpleIdentification <SmplId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
SimpleIdentification <SmplId> contains the following elements (see "AccountIdentification1" on
page 4328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1] ± 4329
66.1.2.8.2  IdentificationAndPurpose <IdAndPurp>
Presence: [1..1]
Definition: Identification of the account expressed with an account number and a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4335 May 2026
```

