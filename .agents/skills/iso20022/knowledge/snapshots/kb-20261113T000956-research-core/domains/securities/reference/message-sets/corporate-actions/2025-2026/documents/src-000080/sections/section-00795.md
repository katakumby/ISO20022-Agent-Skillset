---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.65 CorporateActionEventType112Choice", "16.1.15.65.2 Proprietary <Prtry>"]
file_pages: [995]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.65.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 995 to 995.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 995

```text
CodeName Name Definition
TREC TaxReclaim Event related to tax reclaim activities.
TEND Tender Offer made to holders by a third party,
requesting them to sell (tender) or
exchange their securities.
DLST TradingStatusDelisted Security is no longer able to comply with
the listing requirements of a stock
exchange and is removed from official
board quotation.
SUSP TradingStatusSuspended Trading in the security has been
suspended.
EXWA WarrantExercise Option offered to holders to buy (call
warrant) or to sell (put warrant) a specific
amount of stock, cash, or commodity, at
a predetermined price, during a
predetermined period of time (which
usually corresponds to the life of the
issue).
WTRC WithholdingTaxReliefCertification Certification process for withholding tax
reduction or exemption based on the tax
status of the holder.
WRTH Worthless Booking out of valueless securities.
ACCU Accumulation Funds related event in which the income
(for example accumulation units) that
accrues during an accounting period is
retained within the fund instead of being
paid away to investors. The retained
income is nonetheless deemed to have
been distributed to investors for tax
purposes.
16.1.15.65.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Event types expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.66  SafekeepingPlaceFormat41Choice
Definition: Choice between formats for the place of safekeeping.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 995 February 2026
```

