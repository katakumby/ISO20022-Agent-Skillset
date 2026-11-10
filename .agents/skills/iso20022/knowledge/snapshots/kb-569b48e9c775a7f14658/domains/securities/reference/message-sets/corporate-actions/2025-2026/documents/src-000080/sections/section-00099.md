---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.20 PeriodDetails <PrdDtls>", "3.4.11.20.3 ActionPeriod <ActnPrd>"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.20.3 ActionPeriod <ActnPrd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
ParallelTradingPeriod <ParllTradgPrd> contains one of the following elements (see
"Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
3.4.11.20.3  ActionPeriod <ActnPrd>
Presence: [0..1]
Definition: Period during which the specified option, or all options of the event, remains valid, for
example, offer period.
ActionPeriod <ActnPrd> contains one of the following elements (see "Period6Choice" on page 854 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 854
Or}   PeriodCode <PrdCd> [1..1] CodeSet 855
3.4.11.20.4  RevocabilityPeriod <RvcbltyPrd>
Presence: [0..1]
Definition: Period during which the shareholder can revoke, change or withdraw its instruction.
RevocabilityPeriod <RvcbltyPrd> contains one of the following elements (see "Period6Choice" on
page 854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 854
Or}   PeriodCode <PrdCd> [1..1] CodeSet 855
3.4.11.20.5  PrivilegeSuspensionPeriod <PrvlgSspnsnPrd>
Presence: [0..1]
Definition: Period during which the privilege is not available, for example, this can happen whenever a
meeting takes place or whenever a coupon payment is due.
PrivilegeSuspensionPeriod <PrvlgSspnsnPrd> contains one of the following elements (see
"Period6Choice" on page 854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 854
Or}   PeriodCode <PrdCd> [1..1] CodeSet 855
3.4.11.20.6  AccountServicerRevocabilityPeriod <AcctSvcrRvcbltyPrd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 154 February 2026
```

