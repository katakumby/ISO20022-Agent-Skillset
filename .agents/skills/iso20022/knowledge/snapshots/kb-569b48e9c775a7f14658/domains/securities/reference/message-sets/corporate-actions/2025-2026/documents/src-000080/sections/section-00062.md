---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>", "3.4.10.1.31 EarlyThirdPartyDeadline <EarlyThrdPtyDdln>"]
file_pages: [108]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1.31 EarlyThirdPartyDeadline <EarlyThrdPtyDdln>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 108 to 108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 108

```text
ThirdPartyDeadline <ThrdPtyDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.31  EarlyThirdPartyDeadline <EarlyThrdPtyDdln>
Presence: [0..1]
Definition: Date/Time set by the issuer agent as a first early deadline by which the account owner must
instruct directly another party, possibly giving the holder eligibility to incentives. For example, to provide
documentation to an issuer agent.
EarlyThirdPartyDeadline <EarlyThrdPtyDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.32  MarketClaimTrackingEndDate <MktClmTrckgEndDt>
Presence: [0..1]
Definition: Date by which the depository stops monitoring activities of the event, for instance, accounting
and tracking activities for due bills end.
MarketClaimTrackingEndDate <MktClmTrckgEndDt> contains one of the following elements (see
"DateFormat30Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.33  LeadPlaintiffDeadline <LeadPlntffDdln>
Presence: [0..1]
Definition: Last day an investor can become a lead plaintiff.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 108 February 2026
```

